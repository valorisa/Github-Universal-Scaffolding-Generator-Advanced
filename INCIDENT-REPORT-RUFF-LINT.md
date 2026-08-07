# Fiche d'incident — Échec du job CI "lint" (Ruff)

Date : 7 août 2026
Repository : [Github-Universal-Scaffolding-Generator-Advanced](https://github.com/valorisa/Github-Universal-Scaffolding-Generator-Advanced)

Branche de travail : fix/lint-ruff (supprimée après merge)
Pull Request : #20 — MERGED
Run CI initial : 30092947365 (job 89480132328)
Run CI final : 31184429080
Statut final : résolu, CI verte, PR fusionnée

---

## 1. Description du problème

Le workflow GitHub Actions .github/workflows/ci.yml échouait sur
le job "lint", qui exécute :

    poetry run ruff check .

Extraits du log CI initial :

    help: Use `datetime.datetime.now(tz=...).date()` instead
    Found 34 errors.
    [*] 27 fixable with the `--fix` option.
    Exit code: 1

Impact : CI rouge, blocage des merges sur main tant que les
violations persistent.

---

## 2. Analyse des violations

Ruff a détecté 34 violations, dont 27 auto-corrigeables.
Catégories identifiées :

| Code | Description | Traitement |
|------|-------------|------------|
| I001 | Blocs d'imports non triés / mal formatés | Autofix |
| UP035 | Imports typing dépréciés (Dict, List) | Autofix |
| UP006 | Annotations Dict/List au lieu de dict/list natifs | Autofix |
| DTZ011 | datetime.date.today() sans fuseau horaire (4 occurrences : 1 dans generator.py, 3 dans tests/test_cli.py) | Manuel |
| RUF012 | Attribut de classe mutable sans ClassVar (_MANIFEST_TEMPLATES) | Manuel |

Après autofix, il restait exactement 5 erreurs (4 x DTZ011,
1 x RUF012), toutes corrigées manuellement.

---

## 3. Contraintes environnementales (reproduction locale)

Environnement : Termux sur Android (aarch64), Python 3.14.6.

Difficultés rencontrées lors de la reproduction locale :

1. Poetry a tenté de compiler Ruff depuis les sources via
   maturin/Rust, avec l'échec suivant :

    💥 maturin failed
    Caused by: Failed to determine Android API level.
    Please set the ANDROID_API_LEVEL environment variable.
    error: metadata-generation-failed
    ╰─> ruff

2. Fallback via uv impossible :

    The program uv is not installed. Install it by executing:
    pkg install uv

3. pytest absent du venv initial :

    No module named pytest

4. Tests impossibles à importer sans installation du package :

    ModuleNotFoundError: No module named 'github_scaffolding_generator'

Conclusion : l'échec CI était un problème de code (violations
Ruff), mais la reproduction locale était compliquée par des
problèmes d'environnement indépendants (packaging Rust/Android).

---

## 4. Tentatives de résolution

### 4.1 Première procédure (générée par GitHub Copilot)

Séquence proposée : Poetry install, poetry run ruff check . --fix,
corrections manuelles, poetry run pytest, push, PR.

Résultat : échec partiel. La procédure était juste sur le fond
mais supposait un environnement desktop fonctionnel ; sur Termux,
l'étape Poetry/maturin bloquait tout.

### 4.2 Procédure appliquée (contournement de l'environnement)

Principe : reproduire le comportement de la CI (ruff check .),
pas son environnement de packaging.

    git checkout -b fix/lint-ruff
    python3 -m venv .venv
    source .venv/bin/activate
    pip install ruff pytest

    # État initial
    ruff check . 2>&1 | tee ruff-errors-initial.log

    # Autofixes (27 erreurs)
    ruff check . --fix

    # Re-audit : 5 erreurs restantes
    ruff check .

Corrections manuelles DTZ011 (generator.py) :

    sed -i 's/from datetime import date/from datetime import datetime, timezone/' src/github_scaffolding_generator/generator.py
    sed -i 's/today = date\.today()/today = datetime.now(tz=timezone.utc).date()/' src/github_scaffolding_generator/generator.py

Corrections manuelles DTZ011 (tests/test_cli.py) :

    sed -i 's/from datetime import date/from datetime import datetime, timezone/' tests/test_cli.py
    sed -i 's/date\.today()\.isoformat()/datetime.now(tz=timezone.utc).date().isoformat()/g' tests/test_cli.py
    sed -i 's/date\.today()\.year/datetime.now(tz=timezone.utc).date().year/g' tests/test_cli.py

Correction manuelle RUF012 (generator.py) :

    sed -i '/^from pathlib import Path$/a from typing import ClassVar' src/github_scaffolding_generator/generator.py
    sed -i 's/_MANIFEST_TEMPLATES: dict\[str, tuple\] = {/_MANIFEST_TEMPLATES: ClassVar[dict[str, tuple]] = {/' src/github_scaffolding_generator/generator.py

Installation du package en mode développement (résout le
ModuleNotFoundError) puis tests :

    pip install -e .
    ruff check .          # All checks passed!
    python -m pytest tests/ -v   # 119 passed

---

## 5. Fichiers modifiés

| Fichier | Nature des modifications |
|---------|--------------------------|
| src/github_scaffolding_generator/cli.py | Tri des imports (I001) |
| src/github_scaffolding_generator/generator.py | Tri imports, typage natif, date timezone-aware, ClassVar |
| src/github_scaffolding_generator/validator.py | Tri imports, typage natif |
| tests/test_cli.py | Tri imports, assertions date timezone-aware |

Statistiques git : 4 fichiers modifiés, 29 insertions,
27 suppressions.

---

## 6. Validation et déploiement

Vérifications locales avant push :

- ruff check . : All checks passed!
- pytest : 119 passed in 12.84s

Commit : "fix(lint): resolve all ruff violations (34 errors fixed)"
Push : branche fix/lint-ruff
PR : #20 créée puis MERGED (commit 0bafbab sur main)

Résultat CI final (statusCheckRollup de la PR #20) :

    lint     SUCCESS  (COMPLETED)
    lint-md  SUCCESS  (COMPLETED)
    test     SUCCESS  (COMPLETED)
    state    MERGED

Nettoyage post-merge :

    git checkout main
    git pull                      # fast-forward e604197..0bafbab
    git branch -d fix/lint-ruff   # supprimée localement
    # suppression remote inutile : GitHub l'a supprimée au merge

---

## 7. Leçons tirées

1. Reproduire le comportement de la CI, pas son packaging.
   La CI exécute ruff check . : un venv pip simple
   (pip install ruff pytest + pip install -e .) suffit, sans
   Poetry ni compilation Rust.

2. Règle de bascule : "si l'outil devient le problème, chercher
   une autre manière d'exécuter la même tâche". Signaux : maturin,
   cargo, ANDROID_API_LEVEL, wheels absentes.

3. Séquence d'audit efficace :
   ruff check . → ruff check . --fix → ruff check . → corrections
   manuelles ciblées sur le reliquat.

4. Toujours pip install -e . avant pytest, sinon les
   ModuleNotFoundError masquent le vrai problème.

5. DTZ011 : remplacer date.today() par
   datetime.now(tz=timezone.utc).date() partout, y compris dans
   les assertions de tests, pour la cohérence timezone.

6. RUF012 : annoter les attributs de classe partagés avec
   ClassVar[...].

7. Hygiène pré-commit : git diff / git status avant commit pour
   éviter les fichiers parasites (ici, deux logs ruff-errors-*.log
   ont été commités par inadvertance).

8. Vérifier tous les jobs CI (lint, lint-md, test) avant de
   conclure, pas seulement celui qui échouait.

---

## 8. Procédure standard consolidée (pour incidents similaires)

    1.  Lire .github/workflows/ci.yml et pyproject.toml
    2.  Créer un venv : python -m venv .venv
    3.  Activer : source .venv/bin/activate
    4.  Installer le strict nécessaire : pip install ruff pytest
    5.  Installer le projet : pip install -e .
    6.  Auditer : ruff check .
    7.  Autofixer : ruff check . --fix
    8.  Corriger manuellement le reliquat
    9.  Re-auditer : ruff check .
    10. Tester : pytest -v
    11. git diff / git status (chasse aux parasites)
    12. Commit, push, PR
    13. gh pr checks <num> --watch jusqu'au vert

---

## 9. Références

- Ruff : <https://docs.astral.sh/ruff/>
- Règle DTZ011 : <https://docs.astral.sh/ruff/rules/call-date-today/>
- Règle RUF012 : <https://docs.astral.sh/ruff/rules/mutable-class-default/>
- PEP 585 (typage natif) : <https://peps.python.org/pep-0585/>
- PR #20 : <https://github.com/valorisa/Github-Universal-Scaffolding-Generator-Advanced/pull/20>

---

Rédaction : Qwen (session du 7 août 2026), à partir des logs CI
réels, des sorties terminal Termux et de l'analyse croisée
Qwen / ChatGPT / GitHub Copilot.
