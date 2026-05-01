import typer
from .validator import validate_all, ValidationError
from .generator import Generator

app = typer.Typer(name="github-scaffolding-generator", rich_markup_mode="markdown")


@app.command()
def generate(
    project_name: str = typer.Option(..., help="Project name"),
    project_type: str = typer.Option(..., help="Project type (cli, library, webapp, github-action, docs, monorepo)"),
    stack: str = typer.Option(..., help="Technology stack"),
    description: str = typer.Option(..., help="Project description"),
    author: str = typer.Option(..., help="GitHub username or organization"),
    license: str = typer.Option("MIT", help="License (MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, proprietary)"),
    visibility: str = typer.Option("public", help="Repository visibility (public, private)"),
    ci_targets: str = typer.Option("lint,test", help="CI targets (lint,test,build,release)"),
    output_dir: str = typer.Option("output", help="Output directory"),
    quick: str = typer.Option("no", help="Quick mode (yes/no): generate only README, LICENSE, .gitignore"),
):
    """Generate GitHub repository scaffolding."""
    try:
        context = validate_all(
            project_name=project_name,
            project_type=project_type,
            stack=stack,
            license_name=license,
            visibility=visibility,
            ci_targets=ci_targets,
        )
    except ValidationError as e:
        typer.echo(f"Validation error: {e}")
        raise typer.Exit(1)

    context["description"] = description
    context["author"] = author
    context["quick"] = quick == "yes"

    typer.echo(f"Generating {project_name}...")
    gen = Generator(output_dir=output_dir)
    files = gen.generate(context)

    typer.echo(f"Generated {len(files)} files:")
    for f in files:
        typer.echo(f"  - {f}")
    typer.echo(f"Done! Files are in {output_dir}/{project_name}/")


@app.command()
def version():
    """Show version."""
    from . import __version__
    typer.echo(f"github-scaffolding-generator {__version__}")


if __name__ == "__main__":
    app()
