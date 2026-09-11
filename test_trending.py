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
