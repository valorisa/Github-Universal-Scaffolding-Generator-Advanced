"""Generation engine using Jinja2 templates.

IMPORTANT REQUIREMENT FOR README.md:
The generated README.md content MUST be systematically and rigorously:
- Verbose (detailed explanations)
- Detailed (comprehensive coverage)
- Complete (highest possible quality)

All generated documentation should prioritize completeness and detail over brevity.
"""

import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import ClassVar

from jinja2 import Environment, FileSystemLoader

from .stacks import STACK_BY_LABEL

TEMPLATE_DIR = Path(__file__).parent / "templates"


class Generator:
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.env = Environment(
            loader=FileSystemLoader(str(TEMPLATE_DIR)),
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def generate(self, context: dict) -> list[str]:
        today = datetime.now(tz=timezone.utc).date()
        context.setdefault("today", today.isoformat())
        context.setdefault("year", str(today.year))

        stack_label = context.get("stack", "")
        stack_config = STACK_BY_LABEL.get(stack_label)
        if stack_config:
            context.setdefault("ecosystem", stack_config.ecosystem)
            context.setdefault("install_cmd", stack_config.install_cmd)
            context.setdefault("lint_cmd", stack_config.lint_cmd)
            context.setdefault("test_cmd", stack_config.test_cmd)
            context.setdefault("build_cmd", stack_config.build_cmd)
            context.setdefault("setup_action", stack_config.setup_action)
            context.setdefault("setup_action_version", stack_config.setup_action_version)

        project_name = context["project_name"]
        project_dir = self.output_dir / project_name
        project_dir.mkdir(parents=True, exist_ok=True)

        generated_files = []
        generated_files.extend(self._generate_community_standards(project_dir, context))
        generated_files.extend(self._generate_github_files(project_dir, context))
        generated_files.extend(self._generate_ci(project_dir, context))
        generated_files.extend(self._generate_project_files(project_dir, context))

        if sys.platform != "win32":
            setup_sh = project_dir / "setup.sh"
            if setup_sh.exists():
                os.chmod(setup_sh, 0o755)

            shell_script = project_dir / f"{project_name}.sh"
            if shell_script.exists():
                os.chmod(shell_script, 0o755)

        return generated_files

    def _render_template_map(self, base_dir: Path, template_map: dict[str, str], context: dict) -> list[str]:
        files = []
        for output_name, template_name in template_map.items():
            content = self.env.get_template(template_name).render(**context)
            out_path = base_dir / output_name
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding="utf-8")
            files.append(str(out_path))
        return files

    def _generate_community_standards(self, project_dir: Path, context: dict) -> list[str]:
        project_type = context.get("project_type", "")

        if project_type == "powershell-script":
            readme_template = "powershell-README.md.j2"
        elif project_type == "shell-script":
            readme_template = "shell-README.md.j2"
        else:
            readme_template = "community_standards/README.md.j2"

        template_map = {
            "README.md": readme_template,
            "LICENSE": "community_standards/LICENSE.md.j2",
            "CODE_OF_CONDUCT.md": "community_standards/CODE_OF_CONDUCT.md.j2",
            "CONTRIBUTING.md": "community_standards/CONTRIBUTING.md.j2",
            "SECURITY.md": "community_standards/SECURITY.md.j2",
            "CHANGELOG.md": "community_standards/CHANGELOG.md.j2",
        }
        return self._render_template_map(project_dir, template_map, context)

    def _generate_github_files(self, project_dir: Path, context: dict) -> list[str]:
        template_map = {
            ".github/CODEOWNERS": "github/CODEOWNERS.j2",
            ".github/dependabot.yml": "github/dependabot.yml.j2",
            ".github/PULL_REQUEST_TEMPLATE.md": "github/PULL_REQUEST_TEMPLATE.md.j2",
            ".github/ISSUE_TEMPLATE/bug_report.yml": "github/bug_report.yml.j2",
            ".github/ISSUE_TEMPLATE/feature_request.yml": "github/feature_request.yml.j2",
        }
        return self._render_template_map(project_dir, template_map, context)

    def _generate_ci(self, project_dir: Path, context: dict) -> list[str]:
        template_map = {
            ".github/workflows/ci.yml": "ci/ci.yml.j2",
        }
        return self._render_template_map(project_dir, template_map, context)

    _MANIFEST_TEMPLATES: ClassVar[dict[str, tuple]] = {
        "Python": ("pyproject.toml", "pyproject.toml.j2"),
        "Node": ("package.json", "package.json.j2"),
        "Go": ("go.mod", "go.mod.j2"),
        "Java": ("pom.xml", "pom.xml.j2"),
        "Rust": ("Cargo.toml", "Cargo.toml.j2"),
        "PHP": ("composer.json", "composer.json.j2"),
        ".NET": ("{project_name}.csproj", "project.csproj.j2"),
        "Ruby": ("Gemfile", "Gemfile.j2"),
        "PowerShell": ("{project_name}.psd1", "module.psd1.j2"),
    }

    def _generate_project_files(self, project_dir: Path, context: dict) -> list[str]:
        template_map = {
            ".gitignore": "gitignore.j2",
            ".gitattributes": "gitattributes.j2",
            ".editorconfig": "editorconfig.j2",
            ".markdownlint-cli2.yaml": "markdownlint-cli2.yaml.j2",
            "setup.sh": "setup.sh.j2",
            "setup.ps1": "setup.ps1.j2",
        }

        project_type = context.get("project_type", "")
        project_name = context.get("project_name", "project")

        if project_type == "powershell-script":
            template_map[f"{project_name}.psm1"] = "powershell-module.psm1.j2"
            template_map[f"{project_name}.psd1"] = "module.psd1.j2"
            template_map[f"{project_name}.Tests.ps1"] = "powershell-tests.Tests.ps1.j2"
        elif project_type == "shell-script":
            template_map[f"{project_name}.sh"] = "shell-script.sh.j2"
            template_map[f"{project_name}.bats"] = "shell-tests.bats.j2"
        else:
            stack_label = context.get("stack", "")
            stack_config = STACK_BY_LABEL.get(stack_label)
            if stack_config and stack_config.template_key in self._MANIFEST_TEMPLATES:
                filename_pattern, template_file = self._MANIFEST_TEMPLATES[stack_config.template_key]
                filename = filename_pattern.format(project_name=project_name)
                template_map[filename] = template_file

        return self._render_template_map(project_dir, template_map, context)
