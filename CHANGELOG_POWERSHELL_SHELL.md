# Changelog - Ajout des stacks PowerShell et Shell

**Date :** 2026-05-05  
**Auteur :** valorisa  
**Version :** 0.2.0 (proposition)

## 🎯 Résumé

Ajout de deux nouveaux types de projets au générateur de scaffolding GitHub :
- **PowerShell Script** (`powershell-script`) — Modules PowerShell 7 cross-platform
- **Shell Script** (`shell-script`) — Scripts Bash/Zsh pour Linux/macOS

## ✨ Nouvelles fonctionnalités

### 1. Type de projet : `powershell-script`

**Fichiers générés :**
- `{nom-projet}.psm1` — Module PowerShell avec fonctions exportées
- `{nom-projet}.psd1` — Manifeste du module
- `{nom-projet}.Tests.ps1` — Tests Pester 5.x
- README.md adapté avec instructions d'installation PowerShell 7+

**Stack technique :** PowerShell 7 + Pester

**Caractéristiques :**
- ✅ Templates conformes aux conventions PowerShell (PascalCase, $camelCase)
- ✅ Tests Pester avec BeforeAll/AfterAll
- ✅ Documentation inline complète (Synopsis, Description, Parameters, Examples)
- ✅ CI configuré pour PSScriptAnalyzer + Pester
- ✅ .gitignore adapté (TestResults, *.bak, etc.)

### 2. Type de projet : `shell-script`

**Fichiers générés :**
- `{nom-projet}.sh` — Script Bash/Zsh avec logging coloré et parsing d'arguments
- `{nom-projet}.bats` — Tests BATS (Bash Automated Testing System)
- README.md adapté avec instructions BATS + ShellCheck

**Stack technique :** Bash/Zsh

**Caractéristiques :**
- ✅ Script avec `set -euo pipefail` pour sécurité
- ✅ Logging coloré (log_info, log_success, log_warning, log_error)
- ✅ Parsing d'arguments (--verbose, --quiet, --help, commandes)
- ✅ Tests BATS avec setup/teardown
- ✅ CI configuré pour ShellCheck + BATS
- ✅ .gitignore adapté (`*.log`, `*.tmp`, test-reports/)
- ✅ Script automatiquement exécutable (`chmod +x`) sur Linux/macOS

## 📝 Fichiers modifiés

### Core

- **`src/github_scaffolding_generator/validator.py`**
  - Ajout de `powershell-script` et `shell-script` dans `VALID_PROJECT_TYPES`
  - Ajout de `Bash/Zsh` dans `VALID_STACKS`

- **`src/github_scaffolding_generator/cli.py`**
  - Ajout des types 7 et 8 dans `ACTIVITY_MAPPING`
  - Ajout des stacks dans `STACK_MAP` (PowerShell 7 + Pester, Bash/Zsh)
  - Mise à jour des prompts (1-8 au lieu de 1-6)
  - Ajout des labels dans `INTERMEDIATE_LABELS` et `PROJECT_TYPE_MAP`

- **`src/github_scaffolding_generator/generator.py`**
  - Nouvelle logique dans `_generate_community_standards()` pour READMEs spécifiques
  - Nouvelle logique dans `_generate_project_files()` pour charger les templates PowerShell/Shell
  - Ajout de `chmod +x` automatique pour les scripts `.sh` générés

### Templates (6 nouveaux fichiers)

- **`src/github_scaffolding_generator/templates/powershell-module.psm1.j2`**
  - Module PowerShell avec fonction exemple exportée
  - Documentation inline complète
  - Gestion d'erreurs avec `$ErrorActionPreference = "Stop"`

- **`src/github_scaffolding_generator/templates/powershell-tests.Tests.ps1.j2`**
  - Tests Pester 5.x avec contextes et assertions
  - BeforeAll/AfterAll pour import/cleanup du module

- **`src/github_scaffolding_generator/templates/powershell-README.md.j2`**
  - Instructions d'installation PowerShell 7+ sur Windows/macOS/Linux
  - Guide Pester + PSScriptAnalyzer
  - Exemples d'utilisation du module

- **`src/github_scaffolding_generator/templates/shell-script.sh.j2`**
  - Script avec logging coloré, parsing d'arguments, commandes
  - Fonctions `show_usage()`, `show_version()`, `parse_args()`
  - Conforme aux best practices (`set -euo pipefail`, readonly variables)

- **`src/github_scaffolding_generator/templates/shell-tests.bats.j2`**
  - Tests BATS pour commandes, flags, edge cases
  - Setup automatique (`chmod +x` du script)

- **`src/github_scaffolding_generator/templates/shell-README.md.j2`**
  - Instructions d'installation BATS + ShellCheck sur Linux/macOS
  - Guide de développement avec conventions de code
  - Exemples d'utilisation du script

### Tests

- **`tests/test_cli.py`**
  - Ajout de `powershell-script` et `shell-script` dans les tests de validation
  - Ajout de `Bash/Zsh` dans les tests de stack
  - Mise à jour du test `test_activity_mapping_keys_are_contiguous` (1-8)
  - Ajout de 7 nouveaux tests pour PowerShell et Shell :
    - `test_generator_powershell_script_creates_psm1`
    - `test_generator_powershell_script_creates_psd1`
    - `test_generator_powershell_script_creates_tests`
    - `test_generator_powershell_script_uses_custom_readme`
    - `test_generator_shell_script_creates_sh`
    - `test_generator_shell_script_creates_bats`
    - `test_generator_shell_script_uses_custom_readme`
  - Correction du test `test_generator_powershell_stack_includes_psd1`

### Documentation

- **`README.md`**
  - Mise à jour des métriques (8 types de projets, 10 stacks)
  - Ajout d'une section détaillée sur les nouvelles stacks PowerShell et Shell
  - Mise à jour des exemples de questions (1-8)

- **`AGENTS.md`**
  - Ajout de la documentation sur les nouveaux types de projets
  - Liste des 10 stacks supportées
  - Conventions de génération pour PowerShell et Shell

## 📊 Résultats des tests

```bash
poetry run pytest tests/ -v
# ============================= 119 passed in 3.68s ==============================
```

**Couverture des tests :**
- ✅ Validation des nouveaux types de projets
- ✅ Validation de la nouvelle stack Bash/Zsh
- ✅ Génération des fichiers PowerShell (.psm1, .psd1, .Tests.ps1)
- ✅ Génération des fichiers Shell (.sh, .bats)
- ✅ READMEs personnalisés correctement générés
- ✅ Tous les tests existants passent (rétrocompatibilité)

## 🧪 Tests manuels effectués

### PowerShell Script
```bash
poetry run python -c "
from src.github_scaffolding_generator.cli import _generate_files
_generate_files(
    project_name='test-powershell',
    project_type='powershell-script',
    stack='PowerShell 7 + Pester',
    description='Test PowerShell module',
    author='valorisa',
    license_name='MIT',
    visibility='public',
    ci_targets='lint,test',
    output_dir='output',
    quick=False
)
"
# ✅ 21 fichiers générés avec succès
```

### Shell Script
```bash
poetry run python -c "
from src.github_scaffolding_generator.cli import _generate_files
_generate_files(
    project_name='test-shell',
    project_type='shell-script',
    stack='Bash/Zsh',
    description='Test shell script',
    author='valorisa',
    license_name='MIT',
    visibility='public',
    ci_targets='lint,test',
    output_dir='output',
    quick=False
)
"
# ✅ 20 fichiers générés avec succès

cd output/test-shell
./test-shell.sh hello "World"
# ✅ [INFO] Executing hello command...
# ✅ [SUCCESS] Hello, World!

./test-shell.sh --help
# ✅ Affiche l'aide correctement
```

## 🔄 Rétrocompatibilité

✅ **Aucune rupture de compatibilité**
- Les types de projets existants fonctionnent toujours
- Les stacks existantes sont inchangées
- L'API de validation reste compatible
- Tous les tests existants (112) passent

## 📋 Conventions appliquées

### PowerShell
- **Fonctions** : `PascalCase` (ex: `Invoke-MyFunction`)
- **Variables** : `$camelCase` (ex: `$myVariable`)
- **Constantes** : Pas de convention spéciale PowerShell, utilisation de variables standard
- **Indentation** : 4 espaces
- **Documentation** : Blocs `<#...#>` avec `.SYNOPSIS`, `.DESCRIPTION`, `.PARAMETER`, `.EXAMPLE`

### Shell (Bash/Zsh)
- **Fonctions** : `snake_case` (ex: `my_function`)
- **Variables locales** : `snake_case` (ex: `my_var`)
- **Constantes** : `SCREAMING_SNAKE_CASE` avec `readonly` (ex: `readonly MY_CONSTANT`)
- **Indentation** : 4 espaces
- **Sécurité** : `set -euo pipefail` en début de script
- **Documentation** : Commentaires `#` en tête de fonction

## 🚀 Prochaines étapes suggérées

1. ✅ **FAIT** : Ajouter PowerShell et Shell comme types de projets
2. 🔜 **NEXT** : Ajouter les autres stacks front-end/back-end (React, FastAPI, etc.)
3. 🔜 Commande `list-stacks` pour lister toutes les stacks disponibles
4. 🔜 Mode `--non-interactive` pour CI/CD
5. 🔜 Migration vers architecture `templates/frontend/`, `templates/backend/`, etc.

## 📦 Commits suggérés

```bash
git add .
git commit -m "feat: add powershell-script and shell-script project types

- Add PowerShell 7 + Pester stack for cross-platform modules
- Add Bash/Zsh stack for Linux/macOS scripts
- Generate .psm1, .psd1, .Tests.ps1 for PowerShell projects
- Generate .sh, .bats for Shell projects
- Add custom READMEs with platform-specific instructions
- Add 7 new tests for PowerShell and Shell generation
- Update AGENTS.md and README.md with new stacks documentation
- All 119 tests passing

BREAKING CHANGE: None (backward compatible)
"
```

---

## Fin du changelog
