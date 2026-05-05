"""Centralized stack registry — single source of truth for all stack definitions."""

from dataclasses import dataclass


@dataclass(frozen=True)
class StackConfig:
    key: str
    label: str
    language: str
    default_project_type: str
    default_ci_targets: str
    novice_description: str
    template_key: str
    ecosystem: str
    install_cmd: str
    lint_cmd: str
    test_cmd: str
    build_cmd: str
    setup_action: str
    setup_action_version: str


STACKS: list[StackConfig] = [
    StackConfig(
        key="1",
        label="Python 3.12 + Poetry",
        language="Python",
        default_project_type="cli",
        default_ci_targets="lint,test",
        novice_description="Un outil en ligne de commande (terminal)",
        template_key="Python",
        ecosystem="pip",
        install_cmd="pip install poetry && poetry install",
        lint_cmd="ruff check .",
        test_cmd="pytest tests/",
        build_cmd="poetry build",
        setup_action="actions/setup-python@v5",
        setup_action_version="3.12",
    ),
    StackConfig(
        key="2",
        label="Node 20 + pnpm",
        language="JavaScript / Node.js",
        default_project_type="webapp",
        default_ci_targets="lint,test",
        novice_description="Un site web ou application",
        template_key="Node",
        ecosystem="npm",
        install_cmd="npm install -g pnpm && pnpm install",
        lint_cmd="pnpm lint",
        test_cmd="pnpm test",
        build_cmd="pnpm build",
        setup_action="actions/setup-node@v4",
        setup_action_version="20",
    ),
    StackConfig(
        key="3",
        label="Go 1.22",
        language="Go",
        default_project_type="cli",
        default_ci_targets="lint,test",
        novice_description="Un outil en ligne de commande (terminal)",
        template_key="Go",
        ecosystem="gomod",
        install_cmd="go mod download",
        lint_cmd="golangci-lint run",
        test_cmd="go test ./...",
        build_cmd="go build ./...",
        setup_action="actions/setup-go@v5",
        setup_action_version="1.22",
    ),
    StackConfig(
        key="4",
        label="Java 21 + Maven",
        language="Java",
        default_project_type="library",
        default_ci_targets="lint,test,build",
        novice_description="Une bibliothèque à partager",
        template_key="Java",
        ecosystem="maven",
        install_cmd="mvn install",
        lint_cmd="mvn checkstyle:check",
        test_cmd="mvn test",
        build_cmd="mvn package -DskipTests",
        setup_action="actions/setup-java@v4",
        setup_action_version="21",
    ),
    StackConfig(
        key="5",
        label="Rust 1.70 + Cargo",
        language="Rust",
        default_project_type="cli",
        default_ci_targets="lint,test",
        novice_description="Un outil en ligne de commande (terminal)",
        template_key="Rust",
        ecosystem="cargo",
        install_cmd="cargo build",
        lint_cmd="cargo clippy -- -D warnings",
        test_cmd="cargo test",
        build_cmd="cargo build --release",
        setup_action="dtolnay/rust-toolchain@stable",
        setup_action_version="",
    ),
    StackConfig(
        key="6",
        label="PHP 8.3 + Composer",
        language="PHP",
        default_project_type="webapp",
        default_ci_targets="lint,test",
        novice_description="Un site web ou application",
        template_key="PHP",
        ecosystem="composer",
        install_cmd="composer install --no-interaction",
        lint_cmd="phpcs --standard=PSR12 src/",
        test_cmd="vendor/bin/phpunit tests/",
        build_cmd="composer install --no-interaction --no-dev --optimize-autoloader",
        setup_action="shivammathur/setup-php@v2",
        setup_action_version="8.3",
    ),
    StackConfig(
        key="7",
        label="C# / .NET 8",
        language="C# / .NET",
        default_project_type="library",
        default_ci_targets="lint,test,build",
        novice_description="Une bibliothèque à partager",
        template_key=".NET",
        ecosystem="nuget",
        install_cmd="dotnet restore",
        lint_cmd="dotnet format --verify-no-changes",
        test_cmd="dotnet test",
        build_cmd="dotnet build --configuration Release",
        setup_action="actions/setup-dotnet@v4",
        setup_action_version="8.0.x",
    ),
    StackConfig(
        key="8",
        label="Ruby 3.3 + Bundler",
        language="Ruby",
        default_project_type="webapp",
        default_ci_targets="lint,test",
        novice_description="Un site web ou application",
        template_key="Ruby",
        ecosystem="bundler",
        install_cmd="bundle install",
        lint_cmd="bundle exec rubocop",
        test_cmd="bundle exec rspec",
        build_cmd="gem build *.gemspec || bundle exec rake build",
        setup_action="ruby/setup-ruby@v1",
        setup_action_version="3.3",
    ),
    StackConfig(
        key="9",
        label="PowerShell 7 + Pester",
        language="PowerShell",
        default_project_type="cli",
        default_ci_targets="lint,test",
        novice_description="Un automate GitHub",
        template_key="PowerShell",
        ecosystem="nuget",
        install_cmd="Install-Module -Name Pester -Force -Scope CurrentUser",
        lint_cmd="Invoke-ScriptAnalyzer -Path src/ -Recurse -EnableExit",
        test_cmd="Invoke-Pester -Path tests/ -EnableExit",
        build_cmd="Test-ModuleManifest -Path *.psd1",
        setup_action="actions/checkout@v4",
        setup_action_version="",
    ),
    StackConfig(
        key="10",
        label="Bash/Zsh",
        language="Bash / Zsh",
        default_project_type="shell-script",
        default_ci_targets="lint,test",
        novice_description="Un script Shell (Linux/macOS)",
        template_key="Bash",
        ecosystem="github-actions",
        install_cmd="chmod +x *.sh",
        lint_cmd="shellcheck *.sh",
        test_cmd="bats tests/",
        build_cmd="echo 'No build step for shell scripts'",
        setup_action="actions/checkout@v4",
        setup_action_version="",
    ),
]

STACK_BY_KEY: dict[str, StackConfig] = {s.key: s for s in STACKS}
STACK_BY_LABEL: dict[str, StackConfig] = {s.label: s for s in STACKS}


def get_stack_labels() -> dict[str, str]:
    """Return {key: label} for CLI menu display."""
    return {s.key: s.label for s in STACKS}


def get_all_valid_labels() -> list[str]:
    """Return list of all valid stack label strings (for validator)."""
    return [s.label for s in STACKS]
