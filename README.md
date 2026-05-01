# Github-Universal-Scaffolding-Generator-Advanced

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)
![CI Status](https://github.com/valorisa/Github-Universal-Scaffolding-Generator-Advanced/actions/workflows/ci.yml/badge.svg)
![GitHub Community Standards](https://img.shields.io/badge/Community%20Standards-100%25-brightgreen)
![Last Updated](https://img.shields.io/badge/Last%20Updated-May%202026-orange)

> 🎯 **BUT ABSOLU DE CE DÉPÔT** : Ce dépôt héberge un outil CLI (Command Line Interface) open-source, prêt pour la production, qui automatise *intégralement* la création de structures de dépôt GitHub respectant à 100% les **GitHub Community Standards** pour *n'importe quel type de projet logiciel* et *n'importe quelle stack technique supportée*. Il élimine des heures de configuration manuelle, garantit la conformité avec toutes les bonnes pratiques open-source, et génère des fichiers prêts à être commités et poussés sur GitHub sans aucune modification.

---

## 📋 Table des matières
1. [Quel problème ce projet résout-il ?](#quel-problème-ce-projet-résout-il-)
2. [À qui s'adresse cet outil ?](#à-qui-sadresse-cet-outil-)
3. [Démarrage ultra-rapide](#démarrage-ultra-rapide)
4. [Utilisation détaillée](#utilisation-détaillée)
5. [Fonctionnalités clés](#fonctionnalités-clés)
6. [Types de projets supportés](#types-de-projets-supportés)
7. [Stacks techniques supportées](#stacks-techniques-supportées)
8. [Comment fonctionne le pipeline de génération ?](#comment-fonctionne-le-pipeline-de-génération-)
9. [Foire aux questions (novices)](#foire-aux-questions-novices-)
10. [Contribuer](#contribuer)
11. [Licence](#licence)
12. [Remerciements](#remerciements)

---

## 🤔 Quel problème ce projet résout-il ?
Quand vous créez un nouveau dépôt GitHub de zéro, GitHub attend une série de **15+ fichiers obligatoires** pour considérer le projet comme conforme à ses *Community Standards* (les standards de la communauté open-source) :
- `README.md`, `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CHANGELOG.md`
- Templates d'issues (bug reports, feature requests), template de Pull Request
- Configuration CI/CD (`.github/workflows/ci.yml`), configuration Dependabot (`.github/dependabot.yml`)
- `.gitignore`, `.gitattributes`, `.editorconfig`, `.github/CODEOWNERS`

Configurer tout ça manuellement prend **2 à 4 heures** par projet, même pour un développeur expérimenté. Il est très facile d'oublier un fichier, de faire une erreur de formatage, ou de manquer une bonne pratique.

Cet outil résout ce problème en **générant l'intégralité de cette structure en moins d'une minute**, avec tous les champs pré-remplis, aucun placeholder résiduel (zéro `{{...}}` oublié), et une conformité à 100% garantie.

*Note pour les novices : Ce dépôt lui-même respecte strictement tous les standards qu'il génère. Vous pouvez parcourir ses fichiers pour voir exactement ce que l'outil produit.*

---

## 👥 À qui s'adresse cet outil ?
- **Novices complets** : Vous ne connaissez pas les standards GitHub ? L'outil génère tout pour vous, avec des instructions claires dans chaque fichier.
- **Développeurs expérimentés** : Vous voulez gagner du temps et ne plus jamais oublier un fichier de configuration.
- **Mainteneurs open-source** : Vous lancez plusieurs projets par mois et avez besoin d'une structure uniforme et conforme pour tous.
- **Équipes DevOps** : Vous voulez standardiser la structure de tous les dépôts de votre organisation.

---

## 🚀 Démarrage ultra-rapide
### Prérequis (expliqués pour les novices)
1. **Python 3.12+** : Le langage de programmation sur lequel l'outil est construit. Téléchargez-le sur [python.org](https://www.python.org/downloads/) si vous ne l'avez pas.
2. **Poetry** : Un gestionnaire de paquets Python qui installe automatiquement les dépendances de l'outil. Installez-le avec cette commande (copiez-la dans votre terminal) :
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

### Étapes d'installation
1. Clonez ce dépôt (téléchargez le code sur votre ordinateur) :
   ```bash
   git clone https://github.com/valorisa/Github-Universal-Scaffolding-Generator-Advanced.git
   cd Github-Universal-Scaffolding-Generator-Advanced
   ```
2. Installez l'outil avec Poetry :
   ```bash
   poetry install
   ```
3. Vérifiez que l'outil fonctionne :
   ```bash
   poetry run github-scaffolding-generator --help
   ```

### Premier test : Générer un dépôt de test
Lancez cette commande pour générer une structure de projet CLI (comme l'outil lui-même) :
```bash
poetry run github-scaffolding-generator generate \
  --project-name "mon-premier-projet" \
  --project-type cli \
  --stack "Python 3.12 + Poetry" \
  --description "Mon tout premier projet open-source" \
  --author "votre-pseudo-github" \
  --license MIT \
  --visibility public
```
L'outil va générer tous les fichiers dans le dossier `output/mon-premier-projet/` : vous pouvez les copier dans un nouveau dépôt, faire `git init`, `git push`, et votre dépôt sera déjà conforme aux Community Standards.

---

## 📚 Utilisation détaillée
L'outil utilise une commande principale : `generate`, avec les options suivantes (toutes expliquées) :

| Option | Requise ? | Description | Exemple |
|--------|-----------|-------------|---------|
| `--project-name` | Oui | Nom de votre futur dépôt GitHub (pas d'espaces, utilisez des tirets) | `mon-super-outil` |
| `--project-type` | Oui | Type de projet (voir section [Types de projets supportés](#types-de-projets-supportés)) | `cli`, `webapp`, `library` |
| `--stack` | Oui | Stack technique (voir section [Stacks techniques supportées](#stacks-techniques-supportées)) | `Python 3.12 + Poetry`, `Node 20 + pnpm` |
| `--description` | Oui | Courte description (1-2 phrases) de votre projet | `Un outil pour convertir des images en PDF` |
| `--author` | Oui | Votre pseudo GitHub ou nom d'organisation | `valorisa`, `mon-org` |
| `--license` | Non | Licence (MIT par défaut, supporte `Apache-2.0`, `GPL-3.0`, `BSD-3-Clause`, `proprietary`) | `Apache-2.0` |
| `--visibility` | Non | Visibilité du dépôt (`public` par défaut, `private` possible) | `private` |
| `--ci-targets` | Non | Cibles CI (lint, test par défaut, supporte `build`, `release`) | `lint,test,build` |

### Exemple pour un projet webapp
```bash
poetry run github-scaffolding-generator generate \
  --project-name "mon-blog-statique" \
  --project-type webapp \
  --stack "Node 20 + pnpm" \
  --description "Un blog statique généré avec Eleventy" \
  --author "votre-pseudo"
```

---

## ✨ Fonctionnalités clés
Chaque fonctionnalité est conçue pour éliminer les erreurs et garantir la conformité :
1. **Conformité 100% GitHub Community Standards** : Génère tous les 15+ fichiers obligatoires, vérifiés par le self-check automatique de l'outil.
2. **Zéro placeholder résiduel** : Aucun `{{...}}` n'est laissé dans les fichiers générés. Tous les champs sont pré-remplis avec vos inputs.
3. **Support multi-stack et multi-type** : Adapte le `.gitignore`, le workflow CI, et les fichiers conditionnels à votre stack et type de projet.
4. **Standards de versioning intégrés** : Tous les dépôts générés suivent *Conventional Commits 1.0.0* (format de messages de commit standardisé), *SemVer 2.0.0* (numérotation de version MAJOR.MINOR.PATCH), et *Keep a Changelog 1.1.0* (format de suivi des changements).
5. **Mode Quick** : Génère uniquement les 3 fichiers vitaux (README, LICENSE, .gitignore) en 10 secondes pour un prototype rapide.
6. **Mode FR** : Traduit le README et le CONTRIBUTING en français, garde les standards techniques en anglais (norme internationale).
7. **Self-check automatique** : Avant de livrer les fichiers, l'outil vérifie 10 points de conformité (présence de tous les fichiers, pas de placeholders, CI exécutable, etc.). Si une erreur est détectée, il la corrige automatiquement.

---

## 📦 Types de projets supportés
L'outil génère des fichiers supplémentaires spécifiques à chaque type de projet :

| Type | Fichiers supplémentaires générés | Exemple d'usage |
|------|--------------------------------|-----------------|
| `library` | Métadonnées de paquet (`pyproject.toml`/`package.json`/`Cargo.toml`), workflow de release (PyPI OIDC, npm OIDC, etc.), tests API | Une bibliothèque Python publiée sur PyPI |
| `webapp` | `Dockerfile`, `.env.example`, section "Run locally" dans le README | Une application web React |
| `cli` | Entrypoint CLI, instructions d'installation multi-OS (Linux/macOS/Windows) dans le README | L'outil lui-même (ce dépôt) |
| `github-action` | `action.yml`, documentation des inputs/outputs dans le README | Une GitHub Action pour linter du code |
| `docs` | Configuration de site (MkDocs/Docusaurus), structure du dossier `docs/` | La documentation de votre projet |
| `monorepo` | Configuration de workspace (pnpm/turbo/nx), structure du dossier `packages/` | Un dépôt contenant plusieurs paquets liés |

---

## 💻 Stacks techniques supportées
L'outil adapte le `.gitignore`, le workflow CI, et les fichiers de configuration à votre stack :
- **Python 3.12 + Poetry** (stack par défaut de cet outil)
- **Node 20 + pnpm**
- **Go 1.22**
- **Java 21 + Maven**
- **Rust 1.70 + Cargo**

Vous pouvez demander le support d'une nouvelle stack via une *feature request* (template disponible dans le dépôt).

---

## ⚙️ Comment fonctionne le pipeline de génération ?
L'outil suit un pipeline strict en 4 phases (aucune étape n'est sautée sans condition explicite) :
1. **Phase 1 : Validation** : Vérifie que tous vos inputs sont corrects. Si une information manque, l'outil pose au maximum 3 questions ciblées (priorité : type de projet > stack > licence). Si une information critique manque, la génération s'arrête.
2. **Phase 2 : Génération** :
   - Affiche l'arborescence complète du dépôt à générer
   - Génère tous les fichiers Community Standards (sauf en mode Quick)
   - Ajoute les fichiers conditionnels selon votre type de projet
3. **Phase 3 : Formatage** : Affiche chaque fichier dans un format prêt à copier-coller, avec une justification d'une phrase pour chaque fichier.
4. **Phase 4 : Self-check** : Vérifie 10 points de conformité. Si une erreur est détectée, l'outil la corrige (1 seule itération de correction possible). En cas de deuxième échec, la génération est bloquée explicitement.

---

## ❓ Foire aux questions (novices)
### Je ne sais pas quel type de projet choisir !
Consultez la section [Types de projets supportés](#types-de-projets-supportés) : si vous faites un outil en ligne de commande, choisissez `cli`. Si vous faites un site web, choisissez `webapp`. En cas de doute, choisissez `library` (le type le plus générique).

### Ma stack technique n'est pas listée !
Ouvrez une *feature request* (utilisez le template `.github/ISSUE_TEMPLATE/feature_request.yml` dans ce dépôt) en précisant la stack que vous souhaitez ajouter. L'outil est conçu pour être extensible.

### Dois-je modifier les fichiers générés ?
Non. Tous les champs sont pré-remplis avec vos inputs. Vous pouvez copier les fichiers dans votre dépôt, faire `git init && git add . && git commit -m "feat: initial scaffolding" && git push` directement. Vous pouvez bien sûr personnaliser les fichiers plus tard si besoin.

### L'outil est-il gratuit ?
Oui, il est sous licence MIT : vous pouvez l'utiliser, le modifier, le redistribuer gratuitement.

---

## 🤝 Contribuer
Les contributions sont les bienvenues ! Que vous soyez novice ou expert, vous pouvez :
- Signaler un bug (utilisez le template `.github/ISSUE_TEMPLATE/bug_report.yml`)
- Proposer une nouvelle fonctionnalité (utilisez le template `.github/ISSUE_TEMPLATE/feature_request.yml`)
- Soumettre une Pull Request (suivez les règles dans [CONTRIBUTING.md](CONTRIBUTING.md))

Toutes les contributions doivent respecter le format *Conventional Commits* (ex: `feat: add support for Rust stack`) et passer les tests CI locaux :
```bash
poetry run ruff check .  # Lint du code
poetry run pytest tests/  # Tests unitaires
```

---

## 📄 Licence
Ce projet est sous licence MIT : vous pouvez lire le texte complet dans le fichier [LICENSE](LICENSE). En résumé :
- Vous pouvez utiliser l'outil gratuitement, pour n'importe quel projet (personnel, commercial, open-source)
- Vous pouvez modifier le code
- Vous devez conserver le copyright original dans les copies du logiciel

---

## 🙏 Remerciements
- [GitHub Community Standards](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-growth/about-community-profiles-for-public-repositories) pour les référentiels de bonnes pratiques
- [Conventional Commits](https://www.conventionalcommits.org/) pour le standard de messages de commit
- [SemVer](https://semver.org/) pour le standard de versioning
- [Contributor Covenant](https://www.contributor-covenant.org/) pour le standard de code de conduite
