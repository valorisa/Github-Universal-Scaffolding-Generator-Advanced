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
def generate(
    project_name: str = typer.Option(..., prompt="Nom du projet ? (ex: mon-outil)"),
    activity: str = typer.Option(..., prompt="""Tu fais quoi ?
  1 - Un outil en ligne de commande (terminal)
  2 - Un site web ou application
  3 - Une bibliothèque à partager
  4 - Un automate GitHub
  5 - De la documentation
  6 - Plusieurs projets ensemble
Choix (1-6)""", help="Type of activity"),
    description: str = typer.Option(..., prompt="Description courte ? (une phrase)"),
    author: str = typer.Option(..., prompt="Pseudo GitHub ?"),
    license: str = typer.Option("MIT", prompt="Licence ? (MIT=libre et simple, Apache-2.0=pour entreprises, GPL-3.0=tout doit rester libre, proprietary=code privé)"),
    output_dir: str = typer.Option("output", prompt="Dossier de sortie ? (Entrée pour 'output')"),
):
    """Génère la structure d'un dépôt GitHub conforme aux Community Standards."""
    # Déduire le type, stack et CI à partir de l'activité
    if activity not in ACTIVITY_MAPPING:
        typer.echo("Erreur : Choix invalide (1-6)")
        raise typer.Exit(1)
    
    project_type, stack, ci_targets, activity_desc = ACTIVITY_MAPPING[activity]
    
    typer.echo(f"\nOk ! Je configure pour : {activity_desc}")
    
    try:
        context = validate_all(
            project_name=project_name,
            project_type=project_type,
            stack=stack,
            license_name=license,
            visibility="public",
            ci_targets=ci_targets,
        )
    except ValidationError as e:
        typer.echo(f"Erreur : {e}")
        raise typer.Exit(1)

    context["description"] = description
    context["author"] = author
    context["quick"] = False

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
