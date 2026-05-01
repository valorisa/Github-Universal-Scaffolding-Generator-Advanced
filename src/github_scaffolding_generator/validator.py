"""Validation module for project inputs."""

from typing import Optional

VALID_PROJECT_TYPES = ["cli", "library", "webapp", "github-action", "docs", "monorepo"]
VALID_LICENSES = ["MIT", "Apache-2.0", "GPL-3.0", "BSD-3-Clause", "proprietary"]
VALID_VISIBILITIES = ["public", "private"]
VALID_CI_TARGETS = ["lint", "test", "build", "release"]

VALID_STACKS = [
    "Python 3.12 + Poetry",
    "Node 20 + pnpm",
    "Go 1.22",
    "Java 21 + Maven",
    "Rust 1.70 + Cargo",
]


class ValidationError(ValueError):
    """Custom exception for validation errors."""


def validate_project_name(name: str) -> str:
    if not name:
        raise ValidationError("Project name is required")
    if not name.replace("-", "").replace("_", "").isalnum():
        raise ValidationError("Project name must be alphanumeric with dashes/underscores only")
    return name


def validate_project_type(project_type: str) -> str:
    if project_type not in VALID_PROJECT_TYPES:
        raise ValidationError(f"Invalid project type. Must be one of: {', '.join(VALID_PROJECT_TYPES)}")
    return project_type


def validate_stack(stack: str) -> str:
    if stack not in VALID_STACKS:
        raise ValidationError(f"Invalid stack. Must be one of: {', '.join(VALID_STACKS)}")
    return stack


def validate_license(license_name: Optional[str]) -> str:
    if license_name is None:
        return "MIT"
    if license_name not in VALID_LICENSES:
        raise ValidationError(f"Invalid license. Must be one of: {', '.join(VALID_LICENSES)}")
    return license_name


def validate_visibility(visibility: Optional[str]) -> str:
    if visibility is None:
        return "public"
    if visibility not in VALID_VISIBILITIES:
        raise ValidationError(f"Invalid visibility. Must be one of: {', '.join(VALID_VISIBILITIES)}")
    return visibility


def validate_ci_targets(ci_targets: Optional[str]) -> list:
    if ci_targets is None:
        return ["lint", "test"]
    targets = [t.strip() for t in ci_targets.split(",")]
    for t in targets:
        if t not in VALID_CI_TARGETS:
            raise ValidationError(f"Invalid CI target: {t}. Must be one of: {', '.join(VALID_CI_TARGETS)}")
    return targets


def validate_all(
    project_name: str,
    project_type: str,
    stack: str,
    license_name: Optional[str] = None,
    visibility: Optional[str] = None,
    ci_targets: Optional[str] = None,
) -> dict:
    return {
        "project_name": validate_project_name(project_name),
        "project_type": validate_project_type(project_type),
        "stack": validate_stack(stack),
        "license": validate_license(license_name),
        "visibility": validate_visibility(visibility),
        "ci_targets": validate_ci_targets(ci_targets),
    }
