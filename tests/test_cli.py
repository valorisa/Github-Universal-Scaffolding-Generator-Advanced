import tempfile

import pytest

from github_scaffolding_generator.validator import (
    ValidationError,
    validate_all,
    validate_ci_targets,
    validate_license,
    validate_project_name,
    validate_project_type,
    validate_stack,
    validate_visibility,
)
from github_scaffolding_generator.generator import Generator
from github_scaffolding_generator.cli import ACTIVITY_MAPPING, LICENSE_MAP, CI_MAP


# ---------------------------------------------------------------------------
# validate_project_name
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("name", ["my-project", "my_project", "project123", "a"])
def test_validate_project_name_valid(name):
    assert validate_project_name(name) == name


@pytest.mark.parametrize("name", ["", "bad name!", "proj@ect", "foo/bar"])
def test_validate_project_name_invalid(name):
    with pytest.raises(ValidationError):
        validate_project_name(name)


# ---------------------------------------------------------------------------
# validate_project_type
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("ptype", ["cli", "library", "webapp", "github-action", "docs", "monorepo"])
def test_validate_project_type_valid(ptype):
    assert validate_project_type(ptype) == ptype


def test_validate_project_type_invalid():
    with pytest.raises(ValidationError):
        validate_project_type("invalid")


# ---------------------------------------------------------------------------
# validate_stack
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("stack", [
    "Python 3.12 + Poetry",
    "Node 20 + pnpm",
    "Go 1.22",
    "Java 21 + Maven",
    "Rust 1.70 + Cargo",
])
def test_validate_stack_valid(stack):
    assert validate_stack(stack) == stack


def test_validate_stack_invalid():
    with pytest.raises(ValidationError):
        validate_stack("PHP 8")


# ---------------------------------------------------------------------------
# validate_license
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("license_name,expected", [
    ("MIT", "MIT"),
    ("Apache-2.0", "Apache-2.0"),
    ("GPL-3.0", "GPL-3.0"),
    ("BSD-3-Clause", "BSD-3-Clause"),
    ("proprietary", "proprietary"),
    ("Proprietary", "proprietary"),  # case-insensitive
    ("mit", "MIT"),  # case-insensitive
    (None, "MIT"),  # default
])
def test_validate_license_valid(license_name, expected):
    assert validate_license(license_name) == expected


def test_validate_license_invalid():
    with pytest.raises(ValidationError):
        validate_license("WTFPL")


# ---------------------------------------------------------------------------
# validate_visibility
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("vis,expected", [
    ("public", "public"),
    ("private", "private"),
    (None, "public"),
])
def test_validate_visibility_valid(vis, expected):
    assert validate_visibility(vis) == expected


def test_validate_visibility_invalid():
    with pytest.raises(ValidationError):
        validate_visibility("internal")


# ---------------------------------------------------------------------------
# validate_ci_targets
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("targets,expected", [
    ("lint,test", ["lint", "test"]),
    ("lint,test,build", ["lint", "test", "build"]),
    ("lint,test,build,release", ["lint", "test", "build", "release"]),
    (None, ["lint", "test"]),
])
def test_validate_ci_targets_valid(targets, expected):
    assert validate_ci_targets(targets) == expected


def test_validate_ci_targets_invalid():
    with pytest.raises(ValidationError):
        validate_ci_targets("lint,deploy")


# ---------------------------------------------------------------------------
# validate_all
# ---------------------------------------------------------------------------

def test_validate_all_valid():
    context = validate_all(
        project_name="test-project",
        project_type="cli",
        stack="Python 3.12 + Poetry",
        license_name="MIT",
        visibility="public",
        ci_targets="lint,test",
    )
    assert context["project_name"] == "test-project"
    assert context["project_type"] == "cli"
    assert context["license"] == "MIT"
    assert context["ci_targets"] == ["lint", "test"]


def test_validate_all_defaults():
    context = validate_all(
        project_name="proj",
        project_type="webapp",
        stack="Node 20 + pnpm",
    )
    assert context["license"] == "MIT"
    assert context["visibility"] == "public"
    assert context["ci_targets"] == ["lint", "test"]


def test_validate_all_invalid_project_type():
    with pytest.raises(ValidationError):
        validate_all(
            project_name="test",
            project_type="invalid",
            stack="Python 3.12 + Poetry",
        )


# ---------------------------------------------------------------------------
# CLI constants coherence
# ---------------------------------------------------------------------------

def test_activity_mapping_keys_are_contiguous():
    assert set(ACTIVITY_MAPPING.keys()) == {"1", "2", "3", "4", "5", "6"}


def test_license_map_values_are_valid():
    for v in LICENSE_MAP.values():
        validate_license(v)


def test_ci_map_values_are_valid():
    for v in CI_MAP.values():
        validate_ci_targets(v)


# ---------------------------------------------------------------------------
# Generator
# ---------------------------------------------------------------------------

def _make_context(**overrides):
    base = {
        "project_name": "test-project",
        "project_type": "cli",
        "stack": "Python 3.12 + Poetry",
        "license": "MIT",
        "visibility": "public",
        "ci_targets": ["lint", "test"],
        "description": "Test project",
        "author": "testuser",
        "quick": False,
    }
    base.update(overrides)
    return base


def test_generator_creates_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        gen = Generator(output_dir=tmpdir)
        files = gen.generate(_make_context())
        assert len(files) > 0
        assert any("README.md" in f for f in files)


def test_generator_creates_expected_structure():
    with tempfile.TemporaryDirectory() as tmpdir:
        gen = Generator(output_dir=tmpdir)
        files = gen.generate(_make_context())
        names = [f.split("test-project")[-1].replace("\\", "/") for f in files]
        assert "/README.md" in names
        assert "/LICENSE" in names
        assert "/.github/CODEOWNERS" in names
        assert "/.github/workflows/ci.yml" in names
        assert "/.gitignore" in names


def test_generator_python_stack_includes_pyproject():
    with tempfile.TemporaryDirectory() as tmpdir:
        gen = Generator(output_dir=tmpdir)
        files = gen.generate(_make_context(stack="Python 3.12 + Poetry"))
        assert any("pyproject.toml" in f for f in files)


def test_generator_node_stack_excludes_pyproject():
    with tempfile.TemporaryDirectory() as tmpdir:
        gen = Generator(output_dir=tmpdir)
        files = gen.generate(_make_context(stack="Node 20 + pnpm"))
        assert not any("pyproject.toml" in f for f in files)
