"""Generation engine using Jinja2 templates.

IMPORTANT REQUIREMENT FOR README.md:
The generated README.md content MUST be systematically and rigorously:
- Verbose (detailed explanations)
- Detailed (comprehensive coverage)
- Complete (highest possible quality)

All generated documentation should prioritize completeness and detail over brevity.
"""

from datetime import date
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from typing import Dict, List

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

    def generate(self, context: Dict) -> List[str]:
        today = date.today()
        context.setdefault("today", today.isoformat())
        context.setdefault("year", str(today.year))

        project_name = context["project_name"]
        project_dir = self.output_dir / project_name
        project_dir.mkdir(parents=True, exist_ok=True)

        generated_files = []
        generated_files.extend(self._generate_community_standards(project_dir, context))
        generated_files.extend(self._generate_github_files(project_dir, context))
        generated_files.extend(self._generate_ci(project_dir, context))
        generated_files.extend(self._generate_project_files(project_dir, context))

        return generated_files

    def _render_template_map(self, base_dir: Path, template_map: Dict[str, str], context: Dict) -> List[str]:
        files = []
        for output_name, template_name in template_map.items():
            content = self.env.get_template(template_name).render(**context)
            out_path = base_dir / output_name
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding="utf-8")
            files.append(str(out_path))
        return files

    def _generate_community_standards(self, project_dir: Path, context: Dict) -> List[str]:
        template_map = {
            "README.md": "community_standards/README.md.j2",
            "LICENSE": "community_standards/LICENSE.md.j2",
            "CODE_OF_CONDUCT.md": "community_standards/CODE_OF_CONDUCT.md.j2",
            "CONTRIBUTING.md": "community_standards/CONTRIBUTING.md.j2",
            "SECURITY.md": "community_standards/SECURITY.md.j2",
            "CHANGELOG.md": "community_standards/CHANGELOG.md.j2",
        }
        return self._render_template_map(project_dir, template_map, context)

    def _generate_github_files(self, project_dir: Path, context: Dict) -> List[str]:
        template_map = {
            ".github/CODEOWNERS": "github/CODEOWNERS.j2",
            ".github/dependabot.yml": "github/dependabot.yml.j2",
            ".github/PULL_REQUEST_TEMPLATE.md": "github/PULL_REQUEST_TEMPLATE.md.j2",
            ".github/ISSUE_TEMPLATE/bug_report.yml": "github/bug_report.yml.j2",
            ".github/ISSUE_TEMPLATE/feature_request.yml": "github/feature_request.yml.j2",
        }
        return self._render_template_map(project_dir, template_map, context)

    def _generate_ci(self, project_dir: Path, context: Dict) -> List[str]:
        template_map = {
            ".github/workflows/ci.yml": "ci/ci.yml.j2",
        }
        return self._render_template_map(project_dir, template_map, context)

    def _generate_project_files(self, project_dir: Path, context: Dict) -> List[str]:
        template_map = {
            ".gitignore": "gitignore.j2",
            ".gitattributes": "gitattributes.j2",
            ".editorconfig": "editorconfig.j2",
            ".markdownlint-cli2.yaml": "markdownlint-cli2.yaml.j2",
        }
        stack = context.get("stack", "")
        if "Python" in stack:
            template_map["pyproject.toml"] = "pyproject.toml.j2"
        elif "Node" in stack:
            template_map["package.json"] = "package.json.j2"
        elif "Go" in stack:
            template_map["go.mod"] = "go.mod.j2"
        elif "Java" in stack:
            template_map["pom.xml"] = "pom.xml.j2"
        elif "Rust" in stack:
            template_map["Cargo.toml"] = "Cargo.toml.j2"

        return self._render_template_map(project_dir, template_map, context)
