"""Tests for the trending pipeline: filter word boundaries, normalization
of missing GitHub fields, and deterministic marker-based rendering."""

import json
from pathlib import Path

import pytest

import trending

FIXTURE = Path(__file__).parent / "tests" / "fixtures" / "trending.json"


def make_repo(**overrides) -> dict:
    repo = {
        "name": "example",
        "full_name": "owner/example",
        "url": "https://github.com/owner/example",
        "description": "A perfectly ordinary project",
        "stars": 500,
        "language": "Rust",
        "updated_at": "2026-09-10",
        "created_at": "2020-01-01",
        "topics": [],
    }
    repo.update(overrides)
    return repo


# --- filter ---------------------------------------------------------------


@pytest.mark.parametrize(
    "name",
    ["ai-toolkit", "llm-server", "agent-framework", "gpt-wrapper"],
)
def test_filter_matches_keywords_in_name(name):
    assert trending.is_ai_repo(make_repo(name=name))


@pytest.mark.parametrize(
    "name",
    ["email-server", "maintain-tools", "management-app", "first-aid-kit"],
)
def test_filter_respects_word_boundaries(name):
    assert not trending.is_ai_repo(make_repo(name=name))


def test_filter_matches_description():
    repo = make_repo(description="An LLM inference engine")
    assert trending.is_ai_repo(repo)


def test_filter_matches_topics():
    repo = make_repo(topics=["cli", "agents"])
    assert trending.is_ai_repo(repo)


def test_filter_matches_multiword_keywords():
    repo = make_repo(description="Fast large language model runtime")
    assert trending.is_ai_repo(repo)


def test_filter_allows_plain_repo():
    repos = trending.filter_repositories(
        [make_repo(), make_repo(name="llm-lab")]
    )
    assert [r["name"] for r in repos] == ["example"]


# --- normalization --------------------------------------------------------


def test_normalize_fills_missing_optional_fields():
    repo = trending.normalize_repository(
        {
            "name": "bare",
            "full_name": "owner/bare",
            "html_url": "https://github.com/owner/bare",
            "description": None,
            "stargazers_count": 150,
            "language": None,
            "pushed_at": "2026-09-10T12:00:00Z",
        }
    )
    assert repo["description"] == ""
    assert repo["language"] == "Unknown"
    assert repo["topics"] == []
    assert repo["updated_at"] == "2026-09-10"


def test_normalize_tolerates_absent_keys():
    repo = trending.normalize_repository({"full_name": "owner/sparse"})
    assert repo["stars"] == 0
    assert repo["url"] == ""
    assert repo["updated_at"] == ""
    assert repo["created_at"] == ""


def test_normalize_fills_created_at():
    repo = trending.normalize_repository(
        {"full_name": "owner/x", "created_at": "2026-01-02T03:04:05Z"}
    )
    assert repo["created_at"] == "2026-01-02"


# --- ranking & dataset ----------------------------------------------------


def test_rank_sorts_by_stars_with_deterministic_ties():
    repos = trending.rank_repositories(
        [
            make_repo(full_name="b/tied", stars=100),
            make_repo(full_name="c/small", stars=50),
            make_repo(full_name="a/tied", stars=100),
        ]
    )
    assert [(r["rank"], r["full_name"]) for r in repos] == [
        (1, "a/tied"),
        (2, "b/tied"),
        (3, "c/small"),
    ]


def test_build_dataset_is_deterministic_given_fixed_timestamp():
    repos = trending.rank_repositories([make_repo()])
    a = trending.build_dataset(repos, generated_at="2026-09-11T00:00:00Z")
    b = trending.build_dataset(repos, generated_at="2026-09-11T00:00:00Z")
    assert json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)
    assert a["schema_version"] == trending.SCHEMA_VERSION


def test_build_dataset_defaults_fresh_repositories_to_empty():
    repos = trending.rank_repositories([make_repo()])
    dataset = trending.build_dataset(repos, generated_at="2026-09-11T00:00:00Z")
    assert dataset["fresh_repositories"] == []
    assert dataset["criteria"]["fresh_days"] == trending.FRESH_DAYS


def test_build_dataset_includes_fresh_repositories():
    repos = trending.rank_repositories([make_repo()])
    fresh = trending.rank_repositories(
        [make_repo(full_name="new/thing", created_at="2026-01-01")]
    )
    dataset = trending.build_dataset(
        repos, generated_at="2026-09-11T00:00:00Z", fresh=fresh
    )
    assert len(dataset["fresh_repositories"]) == 1
    assert dataset["fresh_repositories"][0]["full_name"] == "new/thing"
    assert dataset["fresh_repositories"][0]["created_at"] == "2026-01-01"
    assert dataset["fresh_repositories"][0]["rank"] == 1


# --- rendering ------------------------------------------------------------


def load_fixture() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def test_render_table_is_deterministic():
    dataset = load_fixture()
    assert trending.render_table(dataset) == trending.render_table(dataset)


def test_render_table_escapes_pipes_and_fills_empty_description():
    table = trending.render_table(load_fixture())
    assert "\\|" in table
    assert "No description provided." in table


def test_splice_inserts_between_markers():
    readme = (
        "# Title\n\n"
        f"{trending.START_MARKER}\nold content\n{trending.END_MARKER}\n\n"
        "## Footer\n"
    )
    result = trending.splice_markers(readme, "new content")
    assert "new content" in result
    assert "old content" not in result
    assert result.startswith("# Title")
    assert result.endswith("## Footer\n")


def test_splice_is_idempotent():
    readme = f"intro\n{trending.START_MARKER}\nx\n{trending.END_MARKER}\noutro"
    table = trending.render_table(load_fixture())
    once = trending.splice_markers(readme, table)
    twice = trending.splice_markers(once, table)
    assert once == twice
    assert once.count(trending.START_MARKER) == 1


def test_splice_fails_loudly_without_markers():
    with pytest.raises(SystemExit):
        trending.splice_markers("no markers here", "table")


# --- fresh (new & rising) section -----------------------------------------


def test_fresh_section_renders_between_markers():
    section = trending.render_fresh_section(load_fixture())
    assert "example/newcomer" in section
    assert "2026-03-12" in section


def test_fresh_section_handles_no_fresh_repos():
    dataset = load_fixture()
    dataset["fresh_repositories"] = []
    section = trending.render_fresh_section(dataset)
    assert "No repositories" in section


def test_fresh_section_respects_row_cap():
    fresh = [
        {
            "rank": i,
            "full_name": f"o/repo{i}",
            "url": f"https://github.com/o/repo{i}",
            "description": "",
            "stars": 100 - i,
            "language": "Go",
            "updated_at": "2026-09-10",
            "created_at": "2026-01-01",
        }
        for i in range(1, 21)
    ]
    dataset = {"fresh_repositories": fresh}
    section = trending.render_fresh_section(dataset, max_rows=5)
    assert section.count("| [o/repo") == 5


def test_readme_splices_fresh_section():
    readme = (
        f"intro\n{trending.FRESH_START_MARKER}\nold\n"
        f"{trending.FRESH_END_MARKER}\noutro"
    )
    result = trending.splice_markers(
        readme,
        trending.render_fresh_section(load_fixture()),
        start=trending.FRESH_START_MARKER,
        end=trending.FRESH_END_MARKER,
    )
    assert "example/newcomer" in result
    assert "old" not in result


# --- history & rank movement ----------------------------------------------


def write_snapshot_file(directory, date, snapshot):
    (directory / f"{date}.json").write_text(json.dumps(snapshot))


def test_no_history_means_no_change_column(tmp_path):
    assert trending.load_previous_ranks("2026-09-11", str(tmp_path)) is None
    table = trending.render_table(load_fixture())
    assert "Change" not in table
    assert "NEW" not in table


def test_previous_ranks_come_from_latest_earlier_snapshot(tmp_path):
    write_snapshot_file(tmp_path, "2026-09-09", {"a/old": 10})
    write_snapshot_file(tmp_path, "2026-09-10", {"a/x": 200, "b/y": 100})
    write_snapshot_file(tmp_path, "2026-09-11", {"a/x": 999})  # today: ignored
    ranks = trending.load_previous_ranks("2026-09-11", str(tmp_path))
    assert ranks == {"a/x": 1, "b/y": 2}


def test_rank_change_rendering_up_down_new(tmp_path):
    dataset = load_fixture()
    # Previous day: kernel-tools led, mailer was second, mystery absent.
    write_snapshot_file(
        tmp_path,
        "2026-09-10",
        {"example/kernel-tools": 99999, "example/mailer": 12000},
    )
    previous = trending.load_previous_ranks("2026-09-11", str(tmp_path))
    trending.annotate_previous_ranks(dataset, previous)
    table = trending.render_table(dataset)
    assert "| Change |" in table
    rows = {r["full_name"]: trending.format_rank_change(r)
            for r in dataset["repositories"]}
    assert rows["example/mailer"] == "↑ 1"
    assert rows["example/kernel-tools"] == "↓ 1"
    assert rows["example/mystery"] == "NEW"  # absent = unknown, not zero


# --- language sections ----------------------------------------------------


def test_language_sections_group_and_skip_unknown():
    sections = trending.render_language_sections(load_fixture())
    assert "### Rust" in sections
    assert "### C" in sections
    assert "Unknown" not in sections
    assert "example/mystery" not in sections


def test_language_sections_respect_caps():
    repos = trending.rank_repositories(
        [
            make_repo(full_name=f"o/repo{i}", language=f"Lang{i % 8}",
                      stars=1000 - i)
            for i in range(40)
        ]
    )
    dataset = trending.build_dataset(
        repos, generated_at="2026-09-11T00:00:00Z"
    )
    sections = trending.render_language_sections(
        dataset, max_languages=3, max_repos=2
    )
    assert sections.count("### ") == 3
    assert sections.count("| [o/") == 6
