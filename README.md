# GitHub Universal Scaffolding Generator

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)
![CI Status](https://github.com/valorisa/Github-Universal-Scaffolding-Generator-Advanced/actions/workflows/ci.yml/badge.svg)

> **QUOI ?** Un outil qui crée automatiquement tous les fichiers pour un nouveau dépôt GitHub (README, LICENSE, CI, etc.) en répondant à quelques questions.
>
> **POUR QUI ?** Novices complets (vous ne connaissez rien), développeurs, mainteneurs open-source, équipes DevOps.
>
> **COMBIEN DE TEMPS ?** 1 minute au lieu de 2-4 heures de configuration manuelle.
>
> **CE QUE ÇA FAIT :** GitHub demande 15+ fichiers précis pour considérer un projet comme "conforme" (Community Standards). Cet outil les génère tous automatiquement avec vos informations pré-remplies.

---

## 🚀 Installation

### 1. Installer Python 3.12+

**Pourquoi Python 3.12+ ?**

- ✅ **Compatibilité maximale** : Python 3.12 est supporté par toutes les bibliothèques modernes
- ✅ **Performance** : Python 3.12 est 10-20% plus rapide que les versions précédentes
- ✅ **Support long terme** : Mises à jour de sécurité jusqu'en 2028
- ⚠️ **Versions antérieures** : Python 3.8-3.11 fonctionnent aussi, mais 3.12 est recommandé

**macOS / Linux :**

```bash
# Vérifier la version
python3 --version
# Doit afficher : Python 3.12.x (ou 3.13.x, etc.)
```

**Windows 10/11 (PowerShell 7.6+) :**

```powershell
# Vérifier la version
python --version
# Doit afficher : Python 3.12.x (ou 3.13.x, etc.)

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

**📚 Petit lexique pour comprendre :**

- **Stack technique** = Les outils pour créer votre projet (ex: Python, JavaScript, Go...)
- **CI** (Continuous Integration) = Un robot qui vérifie automatiquement que votre code ne contient pas d'erreurs
- **Lint** = Un outil qui vérifie que votre code est bien écrit (indentation, noms de variables...)
- **Build** = Transformation de votre code source en programme utilisable
- **Type de projet** = Ce que vous fabriquez (un site web, un outil, une bibliothèque...)

### Lancer l'outil (Mode NOVICE)

**macOS / Linux :**

```bash
poetry run github-scaffolding-generator init
```

**Windows 10/11 (PowerShell 7.6+) :**

```powershell
poetry run github-scaffolding-generator init
```

Choisir `1` dans le menu.

### Les 6 questions (exemples)
```markdown
=== GitHub Scaffolding Generator ===

Choisissez votre mode :
  1 - 🟢 Mode NOVICE (5 questions simples)
  2 - 🟡 Mode INTERMÉDIAIRE (6-7 questions)
  3 - 🔵 Mode EXPERT (toutes les options)

Votre choix (1-3) [1]: 1

--- Mode NOVICE ---

Nom du projet ? (ex: mon-outil): mon-blog

Tu fais quoi ?
  1 - Un outil en ligne de commande (terminal)
  2 - Un site web ou application
  3 - Une bibliothèque à partager
  4 - Un automate GitHub
  5 - De la documentation
  6 - Plusieurs projets ensemble
  7 - Un script PowerShell (Windows)
  8 - Un script Shell (Linux/macOS)
Choix (1-8): 2

✓ Je configure pour : Un site web ou application

Quel langage utilises-tu ? (Entrée = garder le défaut)
  1 - Python
  2 - JavaScript / Node.js
  3 - Go
  4 - Java
  5 - Rust
Choix (1-5) [2]: ← Entrée pour garder Node.js (défaut webapp)

Description courte ? (une phrase): Un blog personnel avec articles et commentaires
Pseudo GitHub ?: monpseudo
Licence ? [MIT]: MIT
Dossier de sortie ? [output]: output

Génération de mon-blog en cours...

15 fichiers générés :
  ✓ output/mon-blog/README.md
  ✓ output/mon-blog/LICENSE
  ...
```

**L'outil propose un défaut intelligent :**
- Type de projet → `webapp` (choisi par l'utilisateur)
- Stack technique → `Node 20 + pnpm` (défaut proposé, modifiable)
- Configuration CI → `lint,test` (automatique)

**Résultat :** 16 fichiers générés dans `output/mon-blog/` prêts à être poussés sur GitHub !

---

## 🟡 Mode INTERMÉDIAIRE (6-7 questions)

**Pour qui ?** Vous connaissez les bases mais voulez un peu plus de contrôle sans être submergé par 9 options.

**📚 Concepts clés :**
- Même lexique que le mode NOVICE
- **Licence** = Permis d'utilisation (MIT = libre, Apache = entreprise, GPL = copyleft, Propriétaire = fermé)
- **Visibilité** = Public (tout le monde voit) ou Privé (vous seul ou votre équipe)
- **CI (Continuous Integration)** = Automatisation : plus vous ajoutez d'options (lint, test, build, release), plus c'est vérifié

### Lancer l'outil (Mode INTERMÉDIAIRE)

**macOS / Linux :**

```bash
poetry run github-scaffolding-generator init
```

**Windows 10/11 (PowerShell 7.6+) :**

```powershell
poetry run github-scaffolding-generator init
```

Choisir `2` dans le menu.

### Les 7-8 questions (exemple)

```markdown
=== GitHub Scaffolding Generator ===

Choisissez votre mode :
  1 - 🟢 Mode NOVICE (5 questions simples)
  2 - 🟡 Mode INTERMÉDIAIRE (6-7 questions)
  3 - 🔵 Mode EXPERT (toutes les options)

Votre choix (1-3) [1]: 2

--- Mode INTERMÉDIAIRE ---

Nom du projet ? (ex: mon-outil): mon-outil-api

Type de projet ?
  1 - CLI (outil en ligne de commande)
  2 - Webapp (site web ou application)
  3 - Library (bibliothèque à partager)
  4 - GitHub Action (automate)
  5 - Docs (documentation)
  6 - Monorepo (plusieurs projets)
Choix (1-6): 2

✓ Type détecté : Un site web ou application

Quel langage utilises-tu ? (Entrée = garder le défaut)
  1 - Python
  2 - JavaScript / Node.js
  3 - Go
  4 - Java
  5 - Rust
Choix (1-5) [2]: 4  ← Override vers Java

Description courte ? (une phrase): Une API REST pour gérer des tâches
Pseudo GitHub ?: votrepseudo

Licence ?
  1 - MIT (libre, permissive)
  2 - Apache-2.0 (libre, protection brevet)
  3 - GPL-3.0 (libre, copyleft)
  4 - Propriétaire (non libre)
Choix (1-4) [1]: 1

Visibilité ? (public/private) [public]: public

CI (intégration continue) ?
  1 - Basique (lint + test)
  2 - Complet (lint + test + build)
  3 - Avancé (lint + test + build + release)
Choix (1-3) [1]: 2

Dossier de sortie ? [output]: output

Génération de mon-outil-api en cours...

16 fichiers générés :
  ✓ output/mon-outil-api/README.md
  ✓ output/mon-outil-api/LICENSE
  ✓ output/mon-outil-api/pom.xml
  ...
```

**Défaut intelligent proposé :**
- Stack technique → `Node 20 + pnpm` (défaut pour webapp, modifiable)

**Vous choisissez :**
- Langage (5 options, avec défaut intelligent pré-sélectionné)
- Licence (parmi les 4 options courantes)
- Visibilité (public/private)
- Niveau de CI (basique, complet, avancé)

**Résultat :** 16 fichiers générés avec la stack adaptée et votre niveau de CI choisi !

---

## 🔵 Mode EXPERT (toutes les options)

**Pour qui ?** Vous connaissez les termes techniques et voulez contrôler chaque paramètre.

**📚 Rappel des termes techniques :**

- **Stack** = Combinaison du langage (Python, JS...) + outil de gestion (Poetry, pnpm, Maven...)
- **CI (Continuous Integration)** = Automatisation : vérifie le code à chaque modification
- **Lint** = Vérification du style du code (espaces, noms de variables...)
- **Build** = Compilation/préparation du projet pour la mise en production
 - **Release** = Création d'une version officielle (v1.0.0, v1.1.0...)

### Lancer l'outil (Mode EXPERT)

**macOS / Linux :**

```bash
poetry run github-scaffolding-generator init
```

**Windows 10/11 (PowerShell 7.6+) :**

```powershell
poetry run github-scaffolding-generator init
```

Choisir `3` dans le menu.

### Les 8 questions (exemple)

```markdown
--- Mode EXPERT ---

Nom du projet ?: mon-outil

Type de projet ?
  1 - cli
  2 - webapp
  3 - library
  4 - github-action
  5 - docs
  6 - monorepo
Choix (1-6): 1

Stack technique ?
  1 - Python 3.12 + Poetry
  2 - Node 20 + pnpm
  3 - Go 1.22
  4 - Java 21 + Maven
  5 - Rust 1.70 + Cargo
Choix (1-5): 5

Description ?: Un outil pour convertir des images
Pseudo GitHub ?: votrepseudo

Licence ?
  1 - MIT
  2 - Apache-2.0
  3 - GPL-3.0
  4 - BSD-3-Clause
  5 - Propriétaire
Choix (1-5): 1

Visibilité ? (public/private) [public]: public

CI targets ?
  1 - lint,test
  2 - lint,test,build
  3 - lint,test,build,release
  4 - Personnalisé (saisie libre)
Choix (1-4): 3

Dossier de sortie ? [output]: output

Génération de mon-outil en cours...
16 fichiers générés :
  ✓ output/mon-outil/Cargo.toml
  ...
```

**Résultat :** 16 fichiers générés avec votre configuration exacte, sans risque de faute de frappe !

---

## 📋 Qu'est-ce que les "GitHub Community Standards" ?

C'est un ensemble de **15+ fichiers** que GitHub demande pour considérer un projet comme "professionnel" et "accueillant" :

### Pourquoi c'est important ?

- ✅ **Badge vert** = Les utilisateurs font confiance à votre projet
- ✅ **Sécurité** = Les gens savent comment signaler des bugs
- ✅ **Contributions** = Les autres développeurs peuvent vous aider facilement
- ✅ **Maintenance** = Vous avez les templates pour issues et Pull Requests

### Les fichiers obligatoires générés

1. **README.md** = Page d'accueil (description, installation, usage)
2. **LICENSE** = Droits d'utilisation (MIT = libre, Apache = entreprise...)
3. **CODE_OF_CONDUCT.md** = Règles de vie de la communauté
4. **CONTRIBUTING.md** = Comment aider au projet
5. **SECURITY.md** = Comment signaler une faille de sécurité
6. **CHANGELOG.md** = Historique des changements
7. **.github/workflows/ci.yml** = Robot qui vérifie le code (CI)
8. **.github/dependabot.yml** = Mise à jour auto des bibliothèques
9. **.github/CODEOWNERS** = Qui approuve les modifications
10. **Templates d'issues et PR** = Modèles pour bugs et nouveautés

Sans ces fichiers, GitHub affiche "Community Standards: 0%" en rouge !

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

### Exemple 1 : Script d'encodage/décodage Base64 (Mode NOVICE)

**Scénario :** Vous voulez créer un outil CLI pour encoder/décoder des credentials en Base64.

```bash
poetry run github-scaffolding-generator init

=== GitHub Scaffolding Generator ===

Choisissez votre mode :
  1 - 🟢 Mode NOVICE (5 questions simples)
  2 - 🟡 Mode INTERMÉDIAIRE (6-7 questions)
  3 - 🔵 Mode EXPERT (toutes les options)

Votre choix (1-3) [1]: 1

--- Mode NOVICE ---

Nom du projet ? (ex: mon-outil): base64-tool

Tu fais quoi ?
  1 - Un outil en ligne de commande (terminal)
  2 - Un site web ou application
  3 - Une bibliothèque à partager
  4 - Un automate GitHub
  5 - De la documentation
  6 - Plusieurs projets ensemble
Choix (1-6): 1

✓ Je configure pour : Un outil en ligne de commande (terminal)

Quel langage utilises-tu ? (Entrée = garder le défaut)
  1 - Python
  2 - JavaScript / Node.js
  3 - Go
  4 - Java
  5 - Rust
Choix (1-5) [1]: ← Entrée (garde Python, défaut pour CLI)

Description courte ? (une phrase): Un outil pour encoder/décoder des credentials en Base64
Pseudo GitHub ?: testuser
Licence ? [MIT]: MIT
Dossier de sortie ? [output]: output

Génération de base64-tool en cours...

16 fichiers générés :
  ✓ output/base64-tool/README.md
  ✓ output/base64-tool/LICENSE
  ✓ output/base64-tool/CODE_OF_CONDUCT.md
  ✓ output/base64-tool/CONTRIBUTING.md
  ✓ output/base64-tool/SECURITY.md
  ✓ output/base64-tool/CHANGELOG.md
  ✓ output/base64-tool/.github/CODEOWNERS
  ✓ output/base64-tool/.github/dependabot.yml
  ✓ output/base64-tool/.github/PULL_REQUEST_TEMPLATE.md
  ✓ output/base64-tool/.github/ISSUE_TEMPLATE/bug_report.yml
  ✓ output/base64-tool/.github/ISSUE_TEMPLATE/feature_request.yml
  ✓ output/base64-tool/.github/workflows/ci.yml
  ✓ output/base64-tool/.gitignore
  ✓ output/base64-tool/.gitattributes
  ✓ output/base64-tool/.editorconfig
  ✓ output/base64-tool/pyproject.toml

Terminé ! Les fichiers sont dans output/base64-tool/
```

**Ce qu'on a obtenu :**

- Type = `cli`, Stack = `Python 3.12 + Poetry` (défaut intelligent), CI = `lint,test`
- 16 fichiers générés avec tout rempli (nom, description, pseudo)
- Le fichier `README.md` contient déjà "Un outil pour encoder/décoder des credentials en Base64"
- Le `pyproject.toml` est prêt avec le nom et la description

**Windows 10/11 (PowerShell 7.6+) :** Même interaction, mêmes résultats.

---

### Exemple 2 : Un site web en Go (Mode NOVICE)

```bash
poetry run github-scaffolding-generator init
# Choisir 1 (Mode NOVICE)
# Nom : mon-blog
# Activité : 2 (site web) → défaut proposé : [2] Node
# Langage : 3 (Go) ← override du défaut
# Description : "Un blog", Pseudo : votrepseudo, Licence : MIT
# → 16 fichiers générés dans output/mon-blog/ avec go.mod
```

---

### Exemple 3 : Une API REST en Java (Mode INTERMÉDIAIRE)

**Scénario :** Vous voulez créer une API REST pour gérer une liste de tâches, en Java.

```bash
poetry run github-scaffolding-generator init

=== GitHub Scaffolding Generator ===

Choisissez votre mode :
  1 - 🟢 Mode NOVICE (5 questions simples)
  2 - 🟡 Mode INTERMÉDIAIRE (6-7 questions)
  3 - 🔵 Mode EXPERT (toutes les options)

Votre choix (1-3) [1]: 2

--- Mode INTERMÉDIAIRE ---

Nom du projet ? (ex: mon-outil): mon-outil-api

Type de projet ?
  1 - CLI (outil en ligne de commande)
  2 - Webapp (site web ou application)
  3 - Library (bibliothèque à partager)
  4 - GitHub Action (automate)
  5 - Docs (documentation)
  6 - Monorepo (plusieurs projets)
Choix (1-6): 2

✓ Type détecté : Un site web ou application

Quel langage utilises-tu ? (Entrée = garder le défaut)
  1 - Python
  2 - JavaScript / Node.js
  3 - Go
  4 - Java
  5 - Rust
Choix (1-5) [2]: 4  ← Override vers Java

Description courte ? (une phrase): Une API REST pour gérer des tâches
Pseudo GitHub ?: votrepseudo

Licence ?
  1 - MIT (libre, permissive)
  2 - Apache-2.0 (libre, protection brevet)
  3 - GPL-3.0 (libre, copyleft)
  4 - Propriétaire (non libre)
Choix (1-4) [1]: 2

Visibilité ? (public/private) [public]: public

CI (intégration continue) ?
  1 - Basique (lint + test)
  2 - Complet (lint + test + build)
  3 - Avancé (lint + test + build + release)
Choix (1-3) [1]: 2

Dossier de sortie ? [output]: output

Génération de mon-outil-api en cours...

16 fichiers générés :
  ✓ output/mon-outil-api/README.md
  ✓ output/mon-outil-api/LICENSE
  ✓ output/mon-outil-api/CODE_OF_CONDUCT.md
  ✓ output/mon-outil-api/CONTRIBUTING.md
  ✓ output/mon-outil-api/SECURITY.md
  ✓ output/mon-outil-api/CHANGELOG.md
  ✓ output/mon-outil-api/.github/CODEOWNERS
  ✓ output/mon-outil-api/.github/dependabot.yml
  ✓ output/mon-outil-api/.github/PULL_REQUEST_TEMPLATE.md
  ✓ output/mon-outil-api/.github/ISSUE_TEMPLATE/bug_report.yml
  ✓ output/mon-outil-api/.github/ISSUE_TEMPLATE/feature_request.yml
  ✓ output/mon-outil-api/.github/workflows/ci.yml
  ✓ output/mon-outil-api/.gitignore
  ✓ output/mon-outil-api/.gitattributes
  ✓ output/mon-outil-api/.editorconfig
  ✓ output/mon-outil-api/pom.xml

Terminé ! Les fichiers sont dans output/mon-outil-api/
```

**Ce qu'on a obtenu :**

- Type = `webapp`, Stack = `Java 21 + Maven` (override du défaut Node)
- Licence Apache-2.0, CI complet (lint + test + build)
- `pom.xml` généré avec la bonne configuration Maven
- CI utilise `setup-java@v4` + `mvn checkstyle:check` / `mvn test` / `mvn package`

**Windows 10/11 (PowerShell 7.6+) :** Même interaction, mêmes résultats.

---

### Exemple 4 : Une bibliothèque Node.js open-source (Mode INTERMÉDIAIRE)

**Scénario :** Vous voulez créer une bibliothèque JavaScript pour valider des emails.

```bash
poetry run github-scaffolding-generator init
# Choisir 2 (Mode INTERMÉDIAIRE)
# Nom : email-validator
# Type : 3 (library) → défaut proposé : [1] Python
# Langage : 2 (Node.js) ← override vers Node
# Description : "Une bibliothèque pour valider des emails"
# Pseudo : votrepseudo
# Licence : 3 (GPL-3.0)
# Visibilité : public
# CI : 3 (avancé = lint,test,build,release)
# → 16 fichiers générés dans output/email-validator/ avec package.json
```

---

### Exemple 5 : Un outil CLI Rust (Mode EXPERT)

```bash
poetry run github-scaffolding-generator init
# Choisir 3 (Mode EXPERT)
# Type de projet : 1 (cli)
# Stack : 5 (Rust 1.70 + Cargo)
# Description : "Un outil rapide"
# Pseudo : votrepseudo
# Licence : 1 (MIT)
# Visibilité : public
# CI targets : 3 (lint,test,build,release)
# Dossier : output
# → 16 fichiers générés dans output/mon-outil/ avec Cargo.toml
```

---

## 📊 Comparatif des 3 modes

| Caractéristique | 🟢 NOVICE | 🟡 INTERMÉDIAIRE | 🔵 EXPERT |
| --- | --- | --- | --- |
| **Nombre de questions** | 6 | 7-8 | 8 |
| **Type de projet** | Menu 1-6 (descriptions simples) | Menu 1-6 (labels techniques) | Menu 1-6 (noms bruts) |
| **Stack / Langage** | Menu 1-5 avec défaut intelligent | Menu 1-5 avec défaut intelligent | Menu 1-5 sans défaut |
| **Licence** | Texte libre, défaut MIT | 4 choix (MIT/Apache/GPL/Propriétaire) | 5 choix (+ BSD-3-Clause) |
| **Visibilité** | Public uniquement | Public ou Private | Public ou Private |
| **CI (intégration continue)** | Automatique (lint+test) | 3 niveaux (basique/complet/avancé) | 3 presets + saisie libre |
| **Dossier de sortie** | `output/` (défaut) | `output/` (défaut) | `output/` (défaut) |
| **Fichiers générés** | 16 | 16 | 16 |
| **Pour qui ?** | Débutants complets | Développeurs avec quelques bases | Experts, DevOps |

---

## ❓ FAQ (Novices)

### "Je ne sais pas quoi choisir comme type de projet !"

Voici des exemples concrets pour choisir :

- **cli** = Un outil qu'on lance dans le terminal (ex: `mon-outil --help`)
  *Exemple :* Un convertisseur de fichiers, un outil de renommage, un script de sauvegarde
- **webapp** = Un site web ou application accessible par navigateur
  *Exemple :* Un blog, une boutique en ligne, un tableau de bord, un réseau social
- **library** = Du code qu'on partage avec d'autres développeurs (on appelle ça "paquet" ou "bibliothèque")
  *Exemple :* Une librairie de calculs mathématiques, un outil de validation d'emails
- **github-action** = Un automate qui s'exécute sur GitHub lors d'un événement
  *Exemple :* Vérifier le code, publier sur PyPI, fermer les issues inactives
- **docs** = Un site de documentation uniquement (pas de code exécutable)
  *Exemple :* La doc de votre API, un wiki d'entreprise, un tutoriel
- **monorepo** = Plusieurs projets dans un seul dépôt (structure avancée)
  *Exemple :* Un dépôt contenant le frontend, le backend, et les outils de build ensemble

### "C'est quoi une stack technique ?"

C'est l'ensemble des outils pour développer (langage de programmation + gestionnaire de paquets) :

- **Python 3.12 + Poetry** = Pour du Python (langage simple et populaire)
  *Poetry aide à gerer les bibliothèques externes*
- **Node 20 + pnpm** = Pour du JavaScript/Node.js (pour sites web, applications)
  *pnpm est un gestionnaire de paquets rapide pour JavaScript*
- **Go 1.22** = Pour du Go (langage rapide pour serveurs)
  *Pas besoin de gestionnaire supplémentaire, Go gère tout*
- **Java 21 + Maven** = Pour du Java (utilisé par les grandes entreprises)
  *Maven télécharge automatiquement les bibliothèques Java*
- **Rust 1.70 + Cargo** = Pour du Rust (langage moderne et sûr)
  *Cargo est le gestionnaire de paquets officiel de Rust*

**En mode novice**, l'outil choisit la stack pour vous automatiquement !

### "Dois-je modifier les fichiers générés ?"

Non ! Tous les champs sont remplis avec vos réponses. Chaque projet généré inclut
un **script d'installation automatique** (`setup.sh` pour macOS/Linux, `setup.ps1`
pour Windows) qui crée le dépôt GitHub et pousse les fichiers en une commande.

**Prérequis (une seule fois) :**

```bash
gh auth login
# → Ouvre le navigateur pour authentification GitHub
```

**macOS / Linux :**

```bash
cd output/mon-projet
chmod +x setup.sh
./setup.sh
```

**Windows 10/11 (PowerShell 7.6+) :**

```powershell
cd output\mon-projet
.\setup.ps1
```

**Déroulé complet du script :**

```
=== Setup: mon-projet ===

[1/6] Checking GitHub CLI authentication...
  OK - Authenticated as votrepseudo

[2/6] Confirm repository details:

  Repository : votrepseudo/mon-projet
  Visibility : public
  Description: Ma description du projet

Change repository name? (Enter = keep 'mon-projet', or type new name): mon-vrai-nom
  → Repository name changed to: votrepseudo/mon-vrai-nom

Proceed with creation? (Y/n): Y

[3/6] Creating repository votrepseudo/mon-vrai-nom (public)...
  Repository created.

[4/6] Initializing git repository...
  Git initialized with remote origin.

[5/6] Checking markdown files...
  Markdown OK

[6/6] Committing and pushing to GitHub...

=== Done! ===

Your repository is live at: https://github.com/votrepseudo/mon-vrai-nom
```

**L'utilisateur a 3 choix à l'étape 2 :**

- **Entrée** → garde le nom actuel, continue
- **Taper un nouveau nom** → renomme le repository avant création
- **`n`** → annule tout, rien n'est créé sur GitHub

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

---

## 📊 Addendum : Analyse technique complète du projet

### Vue d'ensemble

GitHub Universal Scaffolding Generator Advanced est un générateur de scaffolding complet qui produit en une seule commande interactive l'intégralité des fichiers nécessaires pour qu'un dépôt GitHub soit considéré comme conforme aux Community Standards. Le projet repose sur une architecture à trois couches (CLI → Validation → Génération) alimentant un moteur de templates Jinja2 dont chaque fichier est conditionné dynamiquement par les choix de l'utilisateur.

L'objectif fondamental est de réduire de **2-4 heures** à **moins d'une minute** le temps nécessaire pour initialiser un nouveau dépôt avec tous les fichiers de qualité professionnelle attendus par la communauté open-source.

### Métriques du projet

| Métrique | Valeur |
|---|---|
| **Lignes de code Python (src/)** | 448 |
| **Templates Jinja2** | 20 fichiers |
| **Lignes de templates** | 2 466 |
| **Tests unitaires** | 85 cas paramétrés |
| **Dépendances core** | 4 (typer, jinja2, click, python ^3.12) |
| **Dépendances dev** | 2 (ruff, pytest) |
| **Fichiers générés par projet** | 16 |
| **Types de projets supportés** | 8 (+ PowerShell & Shell scripts) |
| **Stacks techniques supportées** | 10 (+ PowerShell 7, Bash/Zsh) |
| **Licences supportées** | 5 |
| **Cibles CI/CD** | 4 (combinables) |
| **Modes d'interface** | 3 |

### Architecture logicielle

```
┌─────────────────────────────────────────────────────────────────┐
│  CLI (cli.py — 259 lignes)                                      │
│  • 3 modes interactifs : Novice / Intermédiaire / Expert        │
│  • Menus numérotés avec défauts intelligents                    │
│  • Zéro saisie libre pour les choix à valeurs multiples         │
│  • Auto-configuration UTF-8 sur Windows                         │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│  Validation (validator.py — 86 lignes)                          │
│  • 6 fonctions de validation spécialisées                       │
│  • Validation case-insensitive des licences                     │
│  • Valeurs par défaut (MIT, public, lint+test)                  │
│  • Messages d'erreur explicites                                 │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│  Génération (generator.py — 102 lignes)                         │
│  • Moteur Jinja2 avec trim_blocks + lstrip_blocks               │
│  • Injection automatique de `today` et `year`                   │
│  • Helper unique `_render_template_map()` (DRY)                 │
│  • Dispatch conditionnel du fichier config par stack            │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│  Templates (20 fichiers — 2 466 lignes)                         │
│  • 100% conditionnés par stack / license / project_type         │
│  • README.md : 1 492 lignes, 14+ blocs conditionnels            │
│  • CI : jobs adaptés par langage (setup-python/node/go/java/    │
│    rust-toolchain) + job release                                 │
│  • Fichiers config : pyproject.toml, package.json, go.mod,      │
│    Cargo.toml, pom.xml selon la stack                           │
└─────────────────────────────────────────────────────────────────┘
```

### Les 16 fichiers générés

Chaque projet créé contient systématiquement :

**Community Standards (6 fichiers) :**

| Fichier | Rôle | Personnalisation |
|---|---|---|
| `README.md` | Documentation complète | Stack, project_type, license, author, description, ci_targets, today |
| `LICENSE` | Texte de licence | 5 licences complètes (MIT, Apache-2.0, GPL-3.0, BSD-3-Clause, proprietary) |
| `CODE_OF_CONDUCT.md` | Code de conduite | project_name, author |
| `CONTRIBUTING.md` | Guide de contribution | Stack-specific (commandes dev), ci_targets, author |
| `SECURITY.md` | Politique de sécurité | project_name, author |
| `CHANGELOG.md` | Historique | project_name, description, today |

**Configuration GitHub (6 fichiers) :**

| Fichier | Rôle | Personnalisation |
|---|---|---|
| `.github/workflows/ci.yml` | Pipeline CI/CD | Stack-specific (5 langages x 4 jobs) |
| `.github/dependabot.yml` | Mise à jour auto | Écosystème adapté (pip/npm/gomod/maven/cargo) |
| `.github/CODEOWNERS` | Ownership | author, paths par project_type |
| `.github/PULL_REQUEST_TEMPLATE.md` | Template PR | ci_targets, project_type |
| `.github/ISSUE_TEMPLATE/bug_report.yml` | Bug report | project_name |
| `.github/ISSUE_TEMPLATE/feature_request.yml` | Feature request | project_name |

**Configuration projet (4 fichiers fixes + 1 conditionnel) :**

| Fichier | Rôle | Personnalisation |
|---|---|---|
| `.gitignore` | Fichiers ignorés | Patterns spécifiques par stack |
| `.gitattributes` | Attributs Git | Diff drivers et linguist par stack |
| `.editorconfig` | Style éditeur | Indentation adaptée par langage |
| Config stack | Manifest du projet | `pyproject.toml` / `package.json` / `go.mod` / `pom.xml` / `Cargo.toml` |

### Couverture multi-stack

Chaque stack technique est supportée de bout en bout :

| Composant | Python | Node | Go | Java | Rust |
|---|---|---|---|---|---|
| **Fichier config** | pyproject.toml | package.json | go.mod | pom.xml | Cargo.toml |
| **CI lint** | ruff | eslint | golangci-lint | checkstyle | clippy |
| **CI test** | pytest | vitest | go test | junit | cargo test |
| **CI build** | poetry build | pnpm build | go build | mvn package | cargo build --release |
| **CI release** | poetry publish | pnpm publish | goreleaser | mvn deploy | cargo publish |
| **Dependabot** | pip | npm | gomod | maven | cargo |
| **.gitignore** | \_\_pycache\_\_, .venv | node_modules, dist | vendor, bin | target, .class | target, Cargo.lock |
| **.editorconfig** | indent 4 | indent 2 | tabs | indent 4 | indent 4 |
| **README sections** | Poetry, Ruff, pytest | pnpm, ESLint, Vitest | go vet, golangci-lint | Maven, JUnit 5 | Cargo, Clippy |

### Ergonomie des 3 modes

| Aspect | Novice | Intermédiaire | Expert |
|---|---|---|---|
| **Questions** | 6 | 7-8 | 8 |
| **Type projet** | Menu 1-6 (descriptions simples) | Menu 1-6 (labels techniques) | Menu 1-6 (noms bruts) |
| **Langage** | Menu 1-5 + défaut intelligent | Menu 1-5 + défaut intelligent | Menu 1-5 sans défaut |
| **Licence** | Texte libre (défaut MIT) | Menu 1-4 (avec descriptions) | Menu 1-5 (+ BSD-3-Clause) |
| **CI** | Automatique | Menu 1-3 (presets) | Menu 1-4 (presets + saisie libre) |
| **Visibilité** | Public (automatique) | Prompt (défaut public) | Prompt (défaut public) |
| **Risque d'erreur** | Nul | Nul | Nul (saisie libre uniquement pour CI custom) |

### ✨ Nouvelles stacks : PowerShell et Bash/Zsh (2026-05-05)

Le générateur supporte désormais deux nouveaux types de projets dédiés aux scripts système :

#### 🔵 PowerShell Script (`powershell-script`)

**Pour qui ?** Développeurs Windows, DevOps, administrateurs système souhaitant créer des modules PowerShell cross-platform (Windows/Linux/macOS).

**Fichiers générés (21 fichiers) :**
- `{nom-projet}.psm1` — Module PowerShell principal avec fonctions exportées
- `{nom-projet}.psd1` — Manifeste du module (metadata, version, dépendances)
- `{nom-projet}.Tests.ps1` — Tests unitaires avec Pester 5.x
- README.md spécifique — Instructions d'installation PowerShell 7+ sur tous les OS
- Tous les fichiers standard (LICENSE, CI, GitHub templates, etc.)

**Stack technique :** PowerShell 7 + Pester

**Exemple de génération :**
```bash
poetry run github-scaffolding-generator init
# Choisir : Mode EXPERT (3) → Type powershell-script (7) → Stack PowerShell 7 + Pester (9)
```

**Ce qui est inclus :**
- ✅ Fonction exemple avec documentation inline (synopsis, description, paramètres, exemples)
- ✅ Tests Pester avec contextes `BeforeAll` / `AfterAll`
- ✅ README avec instructions d'installation PowerShell 7+ sur Windows/macOS/Linux
- ✅ CI configuré pour PSScriptAnalyzer (lint) + Pester (tests)
- ✅ `.gitignore` adapté (TestResults, *.psm1.bak, etc.)

#### 🟢 Shell Script (`shell-script`)

**Pour qui ?** Développeurs Linux/macOS, SRE, administrateurs système souhaitant créer des scripts shell portables (Bash/Zsh).

**Fichiers générés (20 fichiers) :**
- `{nom-projet}.sh` — Script Bash/Zsh exécutable avec parsing d'arguments, couleurs, logging
- `{nom-projet}.bats` — Tests avec BATS (Bash Automated Testing System)
- README.md spécifique — Instructions BATS + ShellCheck sur Linux/macOS
- Tous les fichiers standard (LICENSE, CI, GitHub templates, etc.)

**Stack technique :** Bash/Zsh

**Exemple de génération :**
```bash
poetry run github-scaffolding-generator init
# Choisir : Mode EXPERT (3) → Type shell-script (8) → Stack Bash/Zsh (10)
```

**Ce qui est inclus :**
- ✅ Script avec `set -euo pipefail`, logging coloré, fonctions d'aide
- ✅ Parsing d'arguments (`--verbose`, `--quiet`, `--help`, commandes)
- ✅ Tests BATS avec setup/teardown
- ✅ README avec instructions BATS + ShellCheck sur Ubuntu/Debian/Fedora/macOS
- ✅ CI configuré pour ShellCheck (lint) + BATS (tests)
- ✅ `.gitignore` adapté (`*.log`, `*.tmp`, test-reports/, etc.)
- ✅ Script automatiquement exécutable (`chmod +x`) sur Linux/macOS

**Conventions appliquées :**
- Bash : `snake_case` pour fonctions/variables, constantes en `SCREAMING_SNAKE_CASE`
- PowerShell : `PascalCase` pour fonctions, `$camelCase` pour variables
- Indentation : 4 espaces (conforme PSScriptAnalyzer et ShellCheck defaults)

### 🧪 Tests approfondis (2026-05-05)

Les nouvelles stacks PowerShell et Shell ont été testées exhaustivement sur **macOS** avec les configurations suivantes :

#### Tests PowerShell (macOS avec PowerShell 7.6.1)

✅ **Import de module** : Module `.psm1` importé sans erreur  
✅ **Fonctions exportées** : `Invoke-{NomProjet}Function` correctement exposée  
✅ **Exécution** : Fonction appelée avec paramètres, retourne le résultat attendu  
✅ **Pipeline** : Support du pipeline PowerShell (`'Item1', 'Item2' | Invoke-Function`)  
✅ **Manifeste** : `.psd1` correctement généré avec metadata  
✅ **Tests Pester** : Fichier `.Tests.ps1` généré (requiert Pester 5.0+)  
✅ **Workflows CI** : `.github/workflows/ci.yml` adapté pour PowerShell (PSScriptAnalyzer + Pester)  

**Licences testées** : MIT, Apache-2.0, Proprietary (3 projets générés)

#### Tests Shell (macOS avec Bash 5.x et Zsh)

✅ **Permissions** : Scripts `.sh` automatiquement exécutables (`chmod +x`)  
✅ **Commande `version`** : Affiche version, auteur, licence correctement  
✅ **Commande `hello`** : Logging coloré fonctionnel (INFO, SUCCESS)  
✅ **Commande `--help`** : Aide complète affichée avec usage, commandes, options, exemples  
✅ **Parsing d'arguments** : Flags `--verbose`, `--quiet` reconnus  
✅ **Tests BATS** : Fichier `.bats` généré avec 10 tests (setup, commandes, edge cases)  
✅ **Workflows CI** : `.github/workflows/ci.yml` adapté pour Shell (ShellCheck + BATS)  

**Licences testées** : MIT, GPL-3.0, BSD-3-Clause (3 projets générés)

#### Résultats de validation

```bash
# Tests unitaires (119 tests)
poetry run pytest tests/ -v
# ============================= 119 passed in 3.71s ==============================

# Linter Python
poetry run ruff check .
# All checks passed!

# Linter Markdown
markdownlint-cli2 "**/*.md" --config .markdownlint-cli2.yaml
# Summary: 0 error(s)
```

**Total de projets générés pour les tests** : 6 projets (3 PowerShell + 3 Shell)  
**Total de fichiers générés** : 123 fichiers (21 × 3 + 20 × 3)  
**Aucune erreur détectée** ✅

### Qualité et fiabilité

- **119 tests paramétrés** couvrant : toutes les fonctions de validation, la cohérence des constantes CLI vs validator, la génération de fichiers par stack, le contenu des licences, l'adaptation CI/dependabot/gitignore par stack, l'injection des variables dynamiques dans les templates, et la structure des fichiers générés.
- **Lint Ruff** : zéro warning sur l'ensemble du code source et des tests.
- **Encodage UTF-8** : garanti sur tous les OS — le CLI reconfigure automatiquement stdout/stderr/stdin sur Windows sans intervention utilisateur.
- **Aucune saisie libre** pour les choix à valeurs finies : tous les paramètres critiques (type, stack, licence) utilisent des menus numérotés, éliminant totalement les erreurs de frappe.

### Conclusion

Ce projet remplit intégralement sa promesse : générer en moins d'une minute un dépôt GitHub complet, professionnel et conforme aux Community Standards, quelle que soit la combinaison type de projet × langage × licence × niveau de CI choisie par l'utilisateur. Les 20 templates Jinja2 s'adaptent dynamiquement à chaque configuration, produisant des fichiers cohérents et immédiatement exploitables — du `Cargo.toml` d'un CLI Rust au `pom.xml` d'une webapp Java, en passant par le `package.json` d'une library Node.js.
