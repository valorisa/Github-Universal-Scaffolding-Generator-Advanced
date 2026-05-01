# GitHub Universal Scaffolding Generator

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)
![CI Status](https://github.com/valorisa/Github-Universal-Scaffolding-Generator-Advanced/actions/workflows/ci.yml/badge.svg)

> **QUOI ?** Un outil qui crée automatiquement tous les fichiers pour un nouveau dépôt GitHub (README, LICENSE, CI, etc.) en répondant à quelques questions.
>
> **POUR QUI ?** Novices complets, développeurs, mainteneurs open-source, équipes DevOps.
>
> **COMBIEN DE TEMPS ?** 1 minute au lieu de 2-4 heures de configuration manuelle.

---

## 🚀 Installation

### 1. Installer Python 3.12+

**macOS / Linux :**
```bash
# Vérifier la version
python3 --version
# Doit afficher : Python 3.12.x
```

**Windows 10/11 (PowerShell 7.6+) :**
```powershell
# Vérifier la version
python --version
# Doit afficher : Python 3.12.x

# Si Python n'est pas installé :
# Télécharger sur https://www.python.org/downloads/
```

---

### 2. Installer Poetry (gestionnaire de paquets)

**macOS / Linux :**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

**Windows 10/11 (PowerShell 7.6+) :**
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

---

### 3. Installer l'outil

**macOS / Linux :**
```bash
git clone https://github.com/valorisa/Github-Universal-Scaffolding-Generator-Advanced.git
cd Github-Universal-Scaffolding-Generator-Advanced
poetry install
```

**Windows 10/11 (PowerShell 7.6+) :**
```powershell
git clone https://github.com/valorisa/Github-Universal-Scaffolding-Generator-Advanced.git
cd Github-Universal-Scaffolding-Generator-Advanced
poetry install
```

---

## 🟢 Mode NOVICE (5 questions simples)

**Pour qui ?** Vous ne connaissez pas les termes techniques (stack, CI, lint, etc.).

### Lancer l'outil

**macOS / Linux :**
```bash
poetry run github-scaffolding-generator init
```

**Windows 10/11 (PowerShell 7.6+) :**
```powershell
poetry run github-scaffolding-generator init
```

### Les 5 questions (exemples)
```
1. Nom du projet ? → mon-blog
2. Tu fais quoi ? → 2 (Un site web ou application)
3. Description ? → Un blog statique avec Eleventy
4. Pseudo GitHub ? → votrepseudo
5. Licence ? → MIT (ou Entrée pour accepter MIT par défaut)
```

**L'outil devine tout seul :**
- Type de projet → `webapp`
- Stack technique → `Node 20 + pnpm`
- Configuration CI → `lint,test`

**Résultat :** 15 fichiers générés dans `output/mon-blog/` prêts à être poussés sur GitHub !

---

## 🔵 Mode EXPERT (toutes les options)

**Pour qui ?** Vous connaissez les termes techniques et voulez contrôler chaque paramètre.

### Lancer l'outil

**macOS / Linux :**
```bash
poetry run github-scaffolding-generator init
```

**Windows 10/11 (PowerShell 7.6+) :**
```powershell
poetry run github-scaffolding-generator init
```
Choisir `2` dans le menu.

### Les 9 options disponibles
```
1. Nom du projet ? → mon-outil
2. Type de projet ? → cli (ou webapp/library/github-action/docs/monorepo)
3. Stack technique ? → Python 3.12 + Poetry (ou Node/Go/Java/Rust)
4. Description ? → Un outil pour convertir des images
5. Pseudo GitHub ? → votrepseudo
6. Licence ? → MIT (ou Apache-2.0/GPL-3.0/BSD-3-Clause/proprietary)
7. Visibilité ? → public (ou private)
8. CI targets ? → lint,test,build,release
9. Dossier de sortie ? → output (ou autre)
```

**Résultat :** 16 fichiers générés avec votre configuration exacte !

---

## 📦 Ce qui est généré (15-16 fichiers)

### Fichiers Community Standards (obligatoires pour GitHub)
- `README.md` - Page d'accueil de votre projet
- `LICENSE` - Licence (MIT, Apache, etc.)
- `CODE_OF_CONDUCT.md` - Code de conduite
- `CONTRIBUTING.md` - Comment contribuer
- `SECURITY.md` - Politique de sécurité
- `CHANGELOG.md` - Suivi des changements

### Configuration GitHub
- `.github/workflows/ci.yml` - Pipeline CI (lint, tests, build)
- `.github/dependabot.yml` - Mise à jour automatique des dépendances
- `.github/CODEOWNERS` - Propriétaires du code
- `.github/PULL_REQUEST_TEMPLATE.md` - Template de PR
- `.github/ISSUE_TEMPLATE/bug_report.yml` - Template de bug report
- `.github/ISSUE_TEMPLATE/feature_request.yml` - Template de demande de fonctionnalité

### Fichiers de configuration
- `.gitignore` - Fichiers à ignorer par Git
- `.gitattributes` - Attributs Git (fins de ligne, etc.)
- `.editorconfig` - Configuration de l'éditeur de code
- `pyproject.toml` (si stack Python) - Configuration du projet Python

---

## 🎯 Exemples concrets

### Exemple 1 : Un novice veut faire un site web

**macOS / Linux :**
```bash
poetry run github-scaffolding-generator init
# Choisir 1 (Mode NOVICE)
# Répondre : mon-blog, 2 (site web), "Un blog", votrepseudo, MIT
# → 15 fichiers générés dans output/mon-blog/
```

**Windows 10/11 (PowerShell 7.6+) :**
```powershell
poetry run github-scaffolding-generator init
# Choisir 1 (Mode NOVICE)
# Répondre : mon-blog, 2 (site web), "Un blog", votrepseudo, MIT
# → 15 fichiers générés dans output/mon-blog/
```

### Exemple 2 : Un expert veut faire un outil CLI Python

**macOS / Linux :**
```bash
poetry run github-scaffolding-generator init
# Choisir 2 (Mode EXPERT)
# Répondre : mon-outil, cli, Python 3.12 + Poetry, "Un outil", votrepseudo, MIT, public, lint,test, output
# → 16 fichiers générés dans output/mon-outil/
```

**Windows 10/11 (PowerShell 7.6+) :**
```powershell
poetry run github-scaffolding-generator init
# Choisir 2 (Mode EXPERT)
# Répondre : mon-outil, cli, Python 3.12 + Poetry, "Un outil", votrepseudo, MIT, public, lint,test, output
# → 16 fichiers générés dans output/mon-outil/
```

---

## ❓ FAQ (Novices)

### "Je ne sais pas quoi choisir comme type de projet !"
- **cli** = Un outil qu'on lance dans le terminal (ex: `mon-outil --help`)
- **webapp** = Un site web ou application
- **library** = Du code qu'on partage avec d'autres (ex: une bibliothèque)
- **github-action** = Un automate pour GitHub
- **docs** = De la documentation
- **monorepo** = Plusieurs projets dans un seul dépôt

### "C'est quoi une stack technique ?"
C'est l'ensemble des outils pour développer :
- **Python 3.12 + Poetry** = Pour du Python
- **Node 20 + pnpm** = Pour du JavaScript/Node.js
- **Go 1.22** = Pour du Go
- **Java 21 + Maven** = Pour du Java
- **Rust 1.70 + Cargo** = Pour du Rust

En mode novice, l'outil choisit la stack pour vous !

### "Dois-je modifier les fichiers générés ?"
Non ! Tous les champs sont remplis avec vos réponses. Vous pouvez directement :

**macOS / Linux :**
```bash
cp -r output/mon-projet/ /chemin/vers/votre/nouveau/depot/
cd /chemin/vers/votre/nouveau/depot/
git init
git add .
git commit -m "feat: initial scaffolding"
git push
```

**Windows 10/11 (PowerShell 7.6+) :**
```powershell
Copy-Item -Recurse output/mon-projet/ -Destination C:/chemin/vers/votre/nouveau/depot/
cd C:/chemin/vers/votre/nouveau/depot/
git init
git add .
git commit -m "feat: initial scaffolding"
git push
```

---

## 🤝 Contribuer

Les contributions sont les bienvenues !

1. Signaler un bug → Utilisez le template [bug_report.yml](.github/ISSUE_TEMPLATE/bug_report.yml)
2. Proposer une fonctionnalité → Utilisez le template [feature_request.yml](.github/ISSUE_TEMPLATE/feature_request.yml)
3. Soumettre une Pull Request → Suivez les règles dans [CONTRIBUTING.md](CONTRIBUTING.md)

**Tests locaux :**

**macOS / Linux :**
```bash
poetry run ruff check .  # Vérifier le code
poetry run pytest tests/  # Lancer les tests
```

**Windows 10/11 (PowerShell 7.6+) :**
```powershell
poetry run ruff check .  # Vérifier le code
poetry run pytest tests/  # Lancer les tests
```

---

## 📄 Licence

Ce projet est sous licence **MIT** - vous pouvez l'utiliser gratuitement, le modifier, et le redistribuer.

Résumé :
- ✅ Utilisation commerciale autorisée
- ✅ Modification autorisée
- ✅ Distribution autorisée
- ⚠️ Gardez le copyright original

Voir [LICENSE](LICENSE) pour le texte complet.

---

## 🙏 Remerciements

- [GitHub Community Standards](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-growth/about-community-profiles-for-public-repositories) - Les standards de bonnes pratiques
- [Conventional Commits](https://www.conventionalcommits.org/) - Le standard de messages de commit
- [SemVer](https://semver.org/) - Le standard de versioning
- [Contributor Covenant](https://www.contributor-covenant.org/) - Le standard de code de conduite
