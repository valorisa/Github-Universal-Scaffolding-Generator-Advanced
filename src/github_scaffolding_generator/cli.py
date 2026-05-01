import typer
from .validator import validate_all, ValidationError
from .generator import Generator

app = typer.Typer(name="github-scaffolding-generator", rich_markup_mode="markdown")


@app.command()
def generate(
    project_name: str = typer.Option(..., prompt="Nom du projet ? (ex: mon-outil)", help="Project name"),
    project_type: str = typer.Option(..., prompt="Type de projet ? (cli/library/webapp/github-action/docs/monorepo)", help="Project type"),
    stack: str = typer.Option(..., prompt="Stack technique ? (Python 3.12 + Poetry / Node 20 + pnpm / Go 1.22 / Java 21 + Maven / Rust 1.70 + Cargo)", help="Technology stack"),
    description: str = typer.Option(..., prompt="Description courte ? (une phrase)", help="Project description"),
    author: str = typer.Option(..., prompt="Pseudo GitHub ?", help="GitHub username or organization"),
    license: str = typer.Option("MIT", prompt="Licence ? (MIT/Apache-2.0/GPL-3.0/BSD-3-Clause/proprietary)", help="License"),
    visibility: str = typer.Option("public", prompt="Visible ? (public/private)", help="Repository visibility"),
    ci_targets: str = typer.Option("lint,test", prompt="CI targets ? (lint,test,build,release)", help="CI targets"),
    output_dir: str = typer.Option("output", prompt="Dossier de sortie ?", help="Output directory"),
    quick: str = typer.Option("no", prompt="Mode rapide ? (yes/no - génère seulement README, LICENSE, .gitignore)", help="Quick mode"),
):
    """Génère la structure d'un dépôt GitHub conforme aux Community Standards."""
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
        typer.echo(f"Erreur : {e}")
        raise typer.Exit(1)

    context["description"] = description
    context["author"] = author
    context["quick"] = quick == "yes"

    typer.echo(f"\nGénération de {project_name} en cours...")
    gen = Generator(output_dir=output_dir)
    files = gen.generate(context)

    typer.echo(f"\n{len(files)} fichiers générés :")
    for f in files:
        typer.echo(f"  ✓ {f}")
    typer.echo(f"\nTerminé ! Les fichiers sont dans {output_dir}/{project_name}/\n")


@app.command()
def version():
    """Show version."""
    from . import __version__
    typer.echo(f"github-scaffolding-generator {__version__}")


if __name__ == "__main__":
    app()
