from typer.testing import CliRunner
from github_scaffolding_generator.cli import app

def test_generate():
    runner = CliRunner()
    result = runner.invoke(app, ["generate", "--project-name", "test", "--project-type", "cli", "--stack", "Python 3.12"])
    assert result.exit_code == 0
