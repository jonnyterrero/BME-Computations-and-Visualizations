import datetime as dt
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import worklog  # noqa: E402

COURSES = {
    "circuits": worklog.Course("circuits", "Circuits"),
    "biomechanics": worklog.Course("biomechanics", "Biomechanics"),
}


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    for slug in COURSES:
        for dirname in worklog.KIND_DIRS.values():
            (tmp_path / slug / dirname).mkdir(parents=True)
    return tmp_path


def test_slugify():
    assert worklog.slugify("Thévenin & Norton: Equivalents!") == "th-venin-norton-equivalents"
    with pytest.raises(ValueError):
        worklog.slugify("!!!")


def test_parse_front_matter():
    meta, body = worklog.parse_front_matter("---\ntitle: RC filter\ntags: [rc, filters]\n---\n\n# Body\n")
    assert meta == {"title": "RC filter", "tags": ["rc", "filters"]}
    assert body == "# Body\n"
    assert worklog.parse_front_matter("# No front matter") == ({}, "# No front matter")


def test_new_entry_scaffolds_files(repo: Path):
    path = worklog.new_entry(repo, COURSES, "circuits", "in-class", "RC low-pass", dt.date(2026, 10, 20), ["rc"])
    assert path == repo / "circuits" / "in-class" / "2026-10-20-rc-low-pass"
    assert (path / "main.py").exists()
    meta, _ = worklog.parse_front_matter((path / "README.md").read_text(encoding="utf-8"))
    assert meta["title"] == "RC low-pass"
    assert meta["tags"] == ["rc"]
    with pytest.raises(FileExistsError):
        worklog.new_entry(repo, COURSES, "circuits", "in-class", "RC low-pass", dt.date(2026, 10, 20), [])


def test_new_entry_rejects_unknown_course(repo: Path):
    with pytest.raises(ValueError):
        worklog.new_entry(repo, COURSES, "nope", "in-class", "x", dt.date(2026, 1, 1), [])


def test_build_orders_newest_first_and_check_detects_staleness(repo: Path):
    worklog.new_entry(repo, COURSES, "circuits", "computation", "Older", dt.date(2026, 9, 1), [])
    worklog.new_entry(repo, COURSES, "biomechanics", "in-class", "Newer", dt.date(2026, 10, 1), [])
    (repo / "circuits" / "computations" / "not-dated").mkdir()

    assert worklog.build(repo, COURSES, check=True) == 1
    assert worklog.build(repo, COURSES) == 0
    assert worklog.build(repo, COURSES, check=True) == 0

    log = (repo / "LOG.md").read_text(encoding="utf-8")
    assert log.index("Newer") < log.index("Older")
    assert "not-dated" not in log
    index = (repo / "circuits" / "computations" / "README.md").read_text(encoding="utf-8")
    assert "[Older](2026-09-01-older/)" in index


def test_summary_comes_from_problem_section(repo: Path):
    path = worklog.new_entry(repo, COURSES, "circuits", "in-class", "Divider", dt.date(2026, 10, 2), [])
    readme = path / "README.md"
    text = readme.read_text(encoding="utf-8").replace(
        "<!-- What was asked or what you set out to model. One or two sentences; this becomes the summary in the course index. -->",
        "Find V_out | loaded divider.",
    )
    readme.write_text(text, encoding="utf-8")
    worklog.build(repo, COURSES)
    index = (repo / "circuits" / "in-class" / "README.md").read_text(encoding="utf-8")
    assert "Find V_out \\| loaded divider." in index
