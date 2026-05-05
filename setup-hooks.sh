#!/usr/bin/env bash
# Setup script for git hooks
# Run this after cloning the repository to install pre-push validation hooks

set -euo pipefail

readonly COLOR_GREEN='\033[0;32m'
readonly COLOR_BLUE='\033[0;34m'
readonly COLOR_YELLOW='\033[1;33m'
readonly COLOR_RESET='\033[0m'

echo ""
echo -e "${COLOR_BLUE}=== Git Hooks Setup ===${COLOR_RESET}"
echo ""

# Check if we're in a git repository
if [ ! -d .git ]; then
    echo -e "${COLOR_YELLOW}⚠️  Not in a git repository. Please run this script from the repository root.${COLOR_RESET}"
    exit 1
fi

# Create hooks directory if it doesn't exist
mkdir -p .git/hooks

# Create pre-push hook
echo -e "${COLOR_BLUE}Installing pre-push hook...${COLOR_RESET}"

cat > .git/hooks/pre-push << 'HOOK_EOF'
#!/usr/bin/env bash
# Git pre-push hook for Github-Universal-Scaffolding-Generator-Advanced
# Runs automated checks before allowing a push to remote

set -e

# Colors for output
readonly COLOR_RED='\033[0;31m'
readonly COLOR_GREEN='\033[0;32m'
readonly COLOR_YELLOW='\033[1;33m'
readonly COLOR_BLUE='\033[0;34m'
readonly COLOR_RESET='\033[0m'

echo ""
echo -e "${COLOR_BLUE}🔍 Running pre-push validation checks...${COLOR_RESET}"
echo ""

# Function to print status
print_status() {
    local status=$1
    local message=$2
    if [ "$status" -eq 0 ]; then
        echo -e "${COLOR_GREEN}✅ $message${COLOR_RESET}"
    else
        echo -e "${COLOR_RED}❌ $message${COLOR_RESET}"
    fi
}

# Track overall status
overall_status=0

# 1. Run pytest
echo -e "${COLOR_YELLOW}[1/3] Running pytest...${COLOR_RESET}"
if poetry run pytest tests/ -q; then
    print_status 0 "Tests passed (pytest)"
else
    print_status 1 "Tests failed (pytest)"
    overall_status=1
fi
echo ""

# 2. Run ruff
echo -e "${COLOR_YELLOW}[2/3] Running ruff linter...${COLOR_RESET}"
if poetry run ruff check .; then
    print_status 0 "Linter passed (ruff)"
else
    print_status 1 "Linter failed (ruff)"
    overall_status=1
fi
echo ""

# 3. Run markdownlint (if available)
echo -e "${COLOR_YELLOW}[3/3] Running markdownlint...${COLOR_RESET}"
if command -v markdownlint-cli2 &> /dev/null; then
    if markdownlint-cli2 "**/*.md" --config .markdownlint-cli2.yaml; then
        print_status 0 "Markdown linter passed (markdownlint-cli2)"
    else
        print_status 1 "Markdown linter failed (markdownlint-cli2)"
        overall_status=1
    fi
else
    echo -e "${COLOR_YELLOW}⚠️  markdownlint-cli2 not installed (skipping)${COLOR_RESET}"
fi
echo ""

# Final decision
if [ $overall_status -eq 0 ]; then
    echo -e "${COLOR_GREEN}✅ All checks passed! Proceeding with push...${COLOR_RESET}"
    echo ""
    exit 0
else
    echo -e "${COLOR_RED}❌ Some checks failed! Push aborted.${COLOR_RESET}"
    echo -e "${COLOR_YELLOW}Fix the errors above and try again.${COLOR_RESET}"
    echo ""
    exit 1
fi
HOOK_EOF

# Make the hook executable
chmod +x .git/hooks/pre-push

echo -e "${COLOR_GREEN}✅ Pre-push hook installed successfully!${COLOR_RESET}"
echo ""
echo "The hook will automatically run before each 'git push' and validate:"
echo "  • Tests (pytest)"
echo "  • Linter (ruff)"
echo "  • Markdown (markdownlint-cli2)"
echo ""
echo "To bypass the hook temporarily, use: git push --no-verify"
echo ""
