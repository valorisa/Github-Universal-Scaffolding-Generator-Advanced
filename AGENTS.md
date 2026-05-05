# AGENTS.md

## Commands

```bash
poetry install                        # Install dependencies
poetry run ruff check .               # Lint (CI runs this first)
poetry run pytest tests/              # Run tests
poetry run github-scaffolding-generator init  # Run the CLI tool
```

Markdown lint (requires `npm install -g markdownlint-cli2`):
```bash
markdownlint-cli2 "**/*.md" --config .markdownlint-cli2.yaml
```

## Architecture

This is a **code generator** that creates GitHub repository scaffolding for other projects. It does not build/test itself as a traditional library.

- **Entry point**: `src/github_scaffolding_generator/cli.py` → Typer CLI
- **Core logic**: `cli.py` (modes + prompts), `generator.py` (file generation), `validator.py` (input validation)
- **Templates**: `src/github_scaffolding_generator/templates/` (Jinja2 `.j2` files)
- **Output**: Generated files go to `output/` by default, not the repo root

## Key Details

- Python 3.12+ required (enforced in `pyproject.toml` and CI)
- Poetry manages dependencies (`pyproject.toml` + `poetry.lock`)
- Stack detection maps project types to defaults:
  - `cli/library` → Python+Poetry
  - `webapp/docs/github-action/monorepo` → Node+pnpm
  - `powershell-script` → PowerShell 7 + Pester
  - `shell-script` → Bash/Zsh
- CI runs three jobs in parallel: `ruff check`, `markdownlint-cli2`, `pytest`
- Single test file: `tests/test_cli.py` (validates validator + generator with temp dirs)
- `.markdownlint-cli2.yaml` ignores `output/**` (generated files)

## Supported Project Types

### Standard Types
- `cli` - Command-line tools (default: Python + Poetry)
- `webapp` - Web applications (default: Node + pnpm)
- `library` - Reusable libraries (default: Python + Poetry)
- `github-action` - GitHub Actions (default: Node + pnpm)
- `docs` - Documentation sites (default: Node + pnpm)
- `monorepo` - Monorepo projects (default: Node + pnpm)

### Script Types (NEW)
- `powershell-script` - PowerShell modules (Windows/Linux/macOS)
  - Generates: `.psm1` module, `.psd1` manifest, `.Tests.ps1` (Pester tests)
  - Stack: PowerShell 7 + Pester
  - Custom README with cross-platform PowerShell installation instructions
- `shell-script` - Bash/Zsh scripts (Linux/macOS)
  - Generates: `.sh` script (executable), `.bats` tests (BATS framework)
  - Stack: Bash/Zsh
  - Custom README with BATS and ShellCheck setup instructions

## Available Stacks

1. Python 3.12 + Poetry
2. Node 20 + pnpm
3. Go 1.22
4. Java 21 + Maven
5. Rust 1.70 + Cargo
6. PHP 8.3 + Composer
7. C# / .NET 8
8. Ruby 3.3 + Bundler
9. PowerShell 7 + Pester *(NEW)*
10. Bash/Zsh *(NEW)*
