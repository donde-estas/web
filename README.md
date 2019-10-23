# Dónde-Estás

Aplicación web para registrar desaparecidos.

## Branch naming contract

All branches in repository must follow the following contract:

``` text
branch-type/name-of-branch
```

Where **branch-type** indicates what is the purpose of the branch. The possible values are:

| **`branch-type`** | **description**|
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| feature           | Add a new feature to the main code. Features are client-oriented, meaning no features of code are included here.                               |
| bugfix            | Fix a non-critical part of the code.                                                                                                           |
| improvement       | Improve an already implemented feature. Improvements are also client-oriented.                                                                 |
| library           | Packages and packages versioning oriented. Fixes of code for updating dependencies should be included here.                                    |
| prerelease        | For versioning a code almost ready for it's release. Code here shouldn't add new features, rather freeze new features. For testing pre-release |
| release           | For freezing version these is a final version of the code prior to a release.                                                                  |
| hotfix            | Fixing a critical part of the code or application.                                                                                             |
| docs              | Documenting code or adding documenting files.                                                                                                  |

## Installation

```bash
npm install --save-dev
```

```bash
pipenv install --dev
```

```bash
pipenv run python manage.py makemigrations && pipenv run python manage.py migrate
```

## Usage

On one terminal run:

```bash
npm run build-dev
```

On another terminal run:

```bash
pipenv run python manage.py runserver
```
