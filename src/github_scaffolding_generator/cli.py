import typer
from .validator import validate_all, ValidationError
from .generator import Generator

app = typer.Typer(name="github-scaffolding-generator", rich_markup_mode="markdown")


# Mapping simplifié pour les novices
ACTIVITY_MAPPING = {
    "1": ("cli", "Python 3.12 + Poetry", "lint,test", "Un outil en ligne de commande (terminal)"),
    "2": ("webapp", "Node 20 + pnpm", "lint,test", "Un site web ou application"),
    "3": ("library", "Python 3.12 + Poetry", "lint,test,build", "Une bibliothèque à partager"),
    "4": ("github-action", "Node 20 + pnpm", "lint,test", "Un automate GitHub"),
    "5": ("docs", "Node 20 + pnpm", "lint,test", "De la documentation"),
    "6": ("monorepo", "Node 20 + pnpm", "lint,test,build", "Plusieurs projets ensemble"),
}


@app.command()
def init():
    """Lance le menu interactif (novice ou expert)."""
    typer.echo("\n=== GitHub Scaffolding Generator ===\n")
    typer.echo("Choisissez votre mode :")
    typer.echo("  1 - 🟢 Mode NOVICE (5 questions simples)")
    typer.echo("  2 - 🔵 Mode EXPERT (toutes les options)\n")
    
    mode = typer.prompt("Votre choix (1-2)", default="1")
    
    if mode == "1":
        _novice_mode()
    elif mode == "2":
        _expert_mode()
    else:
        typer.echo("Erreur : Choix invalide")
        raise typer.Exit(1)


def _novice_mode():
    """Mode simplifié pour les novices."""
    typer.echo("\n--- Mode NOVICE ---\n")
    
    project_name = typer.prompt("Nom du projet ? (ex: mon-outil)")
    
    typer.echo("\nTu fais quoi ?")
    typer.echo("  1 - Un outil en ligne de commande (terminal)")
    typer.echo("  2 - Un site web ou application")
    typer.echo("  3 - Une bibliothèque à partager")
    typer.echo("  4 - Un automate GitHub")
    typer.echo("  5 - De la documentation")
    typer.echo("  6 - Plusieurs projets ensemble")
    activity = typer.prompt("Choix (1-6)")
    
    if activity not in ACTIVITY_MAPPING:
        typer.echo("Erreur : Choix invalide (1-6)")
        raise typer.Exit(1)
    
    project_type, stack, ci_targets, activity_desc = ACTIVITY_MAPPING[activity]
    typer.echo(f"\n✓ Je configure pour : {activity_desc}")
    
    description = typer.prompt("Description courte ? (une phrase)")
    author = typer.prompt("Pseudo GitHub ?")
    license = typer.prompt("Licence ?", default="MIT")
    output_dir = typer.prompt("Dossier de sortie ?", default="output")
    
    _generate_files(project_name, project_type, stack, description, author, license, "public", ci_targets, output_dir, False)


def _expert_mode():
    """Mode complet pour les experts."""
    typer.echo("\n--- Mode EXPERT ---\n")
    
    project_name = typer.prompt("Nom du projet ?")
    project_type = typer.prompt("Type de projet ? (cli/webapp/library/github-action/docs/monorepo)")
    stack = typer.prompt("Stack technique ? (Python 3.12 + Poetry / Node 20 + pnpm / Go 1.22 / Java 21 + Maven / Rust 1.70 + Cargo)")
    description = typer.prompt("Description ?")
    author = typer.prompt("Pseudo GitHub ?")
    license = typer.prompt("Licence ?", default="MIT")
    visibility = typer.prompt("Visibilité ? (public/private)", default="public")
    ci_targets = typer.prompt("CI targets ? (lint,test,build,release)", default="lint,test")
    output_dir = typer.prompt("Dossier de sortie ?", default="output")
    quick = typer.prompt("Mode rapide ? (yes/no)", default="no")
    
    _generate_files(project_name, project_type, stack, description, author, license, visibility, ci_targets, output_dir, quick == "yes")


def _generate_files(project_name, project_type, stack, description, author, license, visibility, ci_targets, output_dir, quick):
    """Génère les fichiers avec les paramètres donnés."""
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
