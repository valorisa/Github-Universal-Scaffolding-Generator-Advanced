import typer
from rich.console import Console

app = typer.Typer(name="github-scaffolding-generator")
console = Console()

@app.command()
def generate(
    project_name: str = typer.Option(..., help="Project name"),
    project_type: str = typer.Option(..., help="Project type (cli, library, etc.)"),
    stack: str = typer.Option(..., help="Technology stack"),
):
    """Generate GitHub repository scaffolding."""
    console.print(f"Generating {project_name} ({project_type}, {stack})...")
    # TODO: Implement generation logic
    console.print("Done!")

if __name__ == "__main__":
    app()
