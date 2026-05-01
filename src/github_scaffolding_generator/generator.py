"""Generation engine using Jinja2 templates."""

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
        project_name = context["project_name"]
        project_dir = self.output_dir / project_name
        project_dir.mkdir(parents=True, exist_ok=True)

        generated_files = []

        generated_files.extend(self._generate_community_standards(project_dir, context))
        generated_files.extend(self._generate_github_files(project_dir, context))
        generated_files.extend(self._generate_ci(project_dir, context))
        generated_files.extend(self._generate_project_files(project_dir, context))

        return generated_files

    def _generate_community_standards(self, project_dir: Path, context: Dict) -> List[str]:
        files = []
        template_map = {
            "README.md": "community_standards/README.md.j2",
            "LICENSE": "community_standards/LICENSE.md.j2",
            "CODE_OF_CONDUCT.md": "community_standards/CODE_OF_CONDUCT.md.j2",
            "CONTRIBUTING.md": "community_standards/CONTRIBUTING.md.j2",
            "SECURITY.md": "community_standards/SECURITY.md.j2",
            "CHANGELOG.md": "community_standards/CHANGELOG.md.j2",
        }
        for output_name, template_name in template_map.items():
            content = self.env.get_template(template_name).render(**context)
            out_path = project_dir / output_name
            out_path.write_text(content)
            files.append(str(out_path))
        return files

    def _generate_github_files(self, project_dir: Path, context: Dict) -> List[str]:
        files = []
        github_dir = project_dir / ".github"
        github_dir.mkdir(exist_ok=True)

        template_map = {
            ".github/CODEOWNERS": "github/CODEOWNERS.j2",
            ".github/dependabot.yml": "github/dependabot.yml.j2",
            ".github/PULL_REQUEST_TEMPLATE.md": "github/PULL_REQUEST_TEMPLATE.md.j2",
        }
        for output_name, template_name in template_map.items():
            content = self.env.get_template(template_name).render(**context)
            out_path = project_dir / output_name
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content)
            files.append(str(out_path))

        issue_dir = github_dir / "ISSUE_TEMPLATE"
        issue_dir.mkdir(exist_ok=True)
        for tmpl in ["bug_report.yml.j2", "feature_request.yml.j2"]:
            content = self.env.get_template(f"github/{tmpl}").render(**context)
            out_path = issue_dir / tmpl.replace(".j2", "")
            out_path.write_text(content)
            files.append(str(out_path))

        return files

    def _generate_ci(self, project_dir: Path, context: Dict) -> List[str]:
        files = []
        workflow_dir = project_dir / ".github" / "workflows"
        workflow_dir.mkdir(parents=True, exist_ok=True)

        content = self.env.get_template("ci/ci.yml.j2").render(**context)
        out_path = workflow_dir / "ci.yml"
        out_path.write_text(content)
        files.append(str(out_path))
        return files

    def _generate_project_files(self, project_dir: Path, context: Dict) -> List[str]:
        files = []
        template_map = {
            ".gitignore": "gitignore.j2",
            ".gitattributes": "gitattributes.j2",
            ".editorconfig": "editorconfig.j2",
        }
        if context.get("stack", "").startswith("Python"):
            template_map["pyproject.toml"] = "pyproject.toml.j2"

        for output_name, template_name in template_map.items():
            content = self.env.get_template(template_name).render(**context)
            out_path = project_dir / output_name
            out_path.write_text(content)
            files.append(str(out_path))
        return files
