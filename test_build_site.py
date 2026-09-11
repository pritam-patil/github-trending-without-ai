"""Tests for the static-site renderer: baked-in content, escaping, and the
one-item-per-day RSS digest."""

import json
from pathlib import Path

import build_site

FIXTURE = Path(__file__).parent / "tests" / "fixtures" / "trending.json"


def load_fixture() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def test_index_bakes_content_into_html():
    page = build_site.render_index(load_fixture())
    assert "example/mailer" in page
    assert "12,345" in page
    assert "Updated daily" in page


def test_index_escapes_html_in_descriptions():
    dataset = load_fixture()
    dataset["repositories"][0]["description"] = "<script>alert(1)</script>"
    page = build_site.render_index(dataset)
    assert "<script>alert(1)</script>" not in page
    assert "&lt;script&gt;" in page


def test_index_is_deterministic():
    dataset = load_fixture()
    assert build_site.render_index(dataset) == build_site.render_index(dataset)


def test_feed_is_a_single_daily_item():
    feed = build_site.render_feed(load_fixture())
    assert feed.count("<item>") == 1
    assert "September 11, 2026" in feed
    assert "example/mailer" in feed


def test_build_writes_site_and_data_copy(tmp_path):
    build_site.build(str(FIXTURE), str(tmp_path))
    assert (tmp_path / "index.html").exists()
    assert (tmp_path / "feed.xml").exists()
    copied = json.loads((tmp_path / "data" / "trending.json").read_text())
    assert copied["schema_version"] == 1
