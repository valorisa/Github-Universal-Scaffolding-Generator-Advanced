import sys
import os

if sys.platform == "win32":
    os.system("")  # enables ANSI/VT100 sequences on Windows terminal
    if sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        sys.stdin.reconfigure(encoding="utf-8")

import typer
from .validator import validate_all, ValidationError
from .generator import Generator

app = typer.Typer(name="github-scaffolding-generator", rich_markup_mode="markdown")

ACTIVITY_MAPPING = {
    "1": ("cli", "Python 3.12 + Poetry", "lint,test", "Un outil en ligne de commande (terminal)"),
    "2": ("webapp", "Node 20 + pnpm", "lint,test", "Un site web ou application"),
    "3": ("library", "Python 3.12 + Poetry", "lint,test,build", "Une bibliothèque à partager"),
    "4": ("github-action", "Node 20 + pnpm", "lint,test", "Un automate GitHub"),
    "5": ("docs", "Node 20 + pnpm", "lint,test", "De la documentation"),
    "6": ("monorepo", "Node 20 + pnpm", "lint,test,build", "Plusieurs projets ensemble"),
}

INTERMEDIATE_LABELS = {
    "1": "CLI (outil en ligne de commande)",
    "2": "Webapp (site web ou application)",
    "3": "Library (bibliothèque à partager)",
    "4": "GitHub Action (automate)",
    "5": "Docs (documentation)",
    "6": "Monorepo (plusieurs projets)",
}

LICENSE_MAP = {"1": "MIT", "2": "Apache-2.0", "3": "GPL-3.0", "4": "proprietary"}
CI_MAP = {"1": "lint,test", "2": "lint,test,build", "3": "lint,test,build,release"}


def _prompt_activity(question: str, labels: dict) -> tuple:
    typer.echo(f"\n{question}")
    for key, label in labels.items():
        typer.echo(f"  {key} - {label}")
    choice = typer.prompt("Choix (1-6)")
    if choice not in ACTIVITY_MAPPING:
        typer.echo("Erreur : Choix invalide (1-6)")
        raise typer.Exit(1)
    return ACTIVITY_MAPPING[choice]


def _prompt_license() -> str:
    typer.echo("\nLicence ?")
    typer.echo("  1 - MIT (libre, permissive)")
    typer.echo("  2 - Apache-2.0 (libre, protection brevet)")
    typer.echo("  3 - GPL-3.0 (libre, copyleft)")
    typer.echo("  4 - Propriétaire (non libre)")
    choice = typer.prompt("Choix (1-4)", default="1")
    return LICENSE_MAP.get(choice, "MIT")


def _prompt_ci() -> str:
    typer.echo("\nCI (intégration continue) ?")
    typer.echo("  1 - Basique (lint + test)")
    typer.echo("  2 - Complet (lint + test + build)")
    typer.echo("  3 - Avancé (lint + test + build + release)")
    choice = typer.prompt("Choix (1-3)", default="1")
    return CI_MAP.get(choice, "lint,test")


@app.command()
def init():
    """Lance le menu interactif (novice, intermédiaire ou expert)."""
    typer.echo("\n=== GitHub Scaffolding Generator ===\n")
    typer.echo("Choisissez votre mode :")
    typer.echo("  1 - 🟢 Mode NOVICE (5 questions simples)")
    typer.echo("  2 - 🟡 Mode INTERMÉDIAIRE (6-7 questions)")
    typer.echo("  3 - 🔵 Mode EXPERT (toutes les options)\n")

    mode = typer.prompt("Votre choix (1-3)", default="1")

    modes = {"1": _novice_mode, "2": _intermediate_mode, "3": _expert_mode}
    handler = modes.get(mode)
    if handler is None:
        typer.echo("Erreur : Choix invalide")
        raise typer.Exit(1)
    handler()


def _novice_mode():
    typer.echo("\n--- Mode NOVICE ---\n")

    project_name = typer.prompt("Nom du projet ? (ex: mon-outil)")

    novice_labels = {k: v[3] for k, v in ACTIVITY_MAPPING.items()}
    project_type, stack, ci_targets, activity_desc = _prompt_activity("Tu fais quoi ?", novice_labels)
    typer.echo(f"\n✓ Je configure pour : {activity_desc}")

    description = typer.prompt("Description courte ? (une phrase)")
    author = typer.prompt("Pseudo GitHub ?")
    license_name = typer.prompt("Licence ?", default="MIT")
    output_dir = typer.prompt("Dossier de sortie ?", default="output")

    _generate_files(project_name, project_type, stack, description, author, license_name, "public", ci_targets, output_dir, False)


def _intermediate_mode():
    typer.echo("\n--- Mode INTERMÉDIAIRE ---\n")

    project_name = typer.prompt("Nom du projet ? (ex: mon-outil)")

    project_type, stack, _, activity_desc = _prompt_activity("Type de projet ?", INTERMEDIATE_LABELS)
    typer.echo(f"\n✓ Type détecté : {activity_desc}")

    description = typer.prompt("Description courte ? (une phrase)")
    author = typer.prompt("Pseudo GitHub ?")
    license_name = _prompt_license()
    visibility = typer.prompt("Visibilité ? (public/private)", default="public")
    ci_targets = _prompt_ci()
    output_dir = typer.prompt("Dossier de sortie ?", default="output")

    _generate_files(project_name, project_type, stack, description, author, license_name, visibility, ci_targets, output_dir, False)


def _expert_mode():
    typer.echo("\n--- Mode EXPERT ---\n")

    project_name = typer.prompt("Nom du projet ?")
    project_type = typer.prompt("Type de projet ? (cli/webapp/library/github-action/docs/monorepo)")
    stack = typer.prompt("Stack technique ? (Python 3.12 + Poetry / Node 20 + pnpm / Go 1.22 / Java 21 + Maven / Rust 1.70 + Cargo)")
    description = typer.prompt("Description ?")
    author = typer.prompt("Pseudo GitHub ?")
    license_name = typer.prompt("Licence ?", default="MIT")
    visibility = typer.prompt("Visibilité ? (public/private)", default="public")
    ci_targets = typer.prompt("CI targets ? (lint,test,build,release)", default="lint,test")
    output_dir = typer.prompt("Dossier de sortie ?", default="output")
    quick = typer.prompt("Mode rapide ? (yes/no)", default="no")

    _generate_files(project_name, project_type, stack, description, author, license_name, visibility, ci_targets, output_dir, quick == "yes")


def _generate_files(project_name, project_type, stack, description, author, license_name, visibility, ci_targets, output_dir, quick):
    try:
        context = validate_all(
            project_name=project_name,
            project_type=project_type,
            stack=stack,
            license_name=license_name,
            visibility=visibility,
            ci_targets=ci_targets,
        )
    except ValidationError as e:
        typer.echo(f"\nErreur : {e}")
        raise typer.Exit(1)

    context["description"] = description
    context["author"] = author
    context["quick"] = quick

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
