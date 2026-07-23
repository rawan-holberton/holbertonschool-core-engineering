# Python - Abstract Classes & Interfaces

## Description

Ce projet explore les concepts de programmation orientée objet en Python, notamment les **classes abstraites**, les **interfaces**, le **duck typing**, la **subclassing**, la **multiple inheritance** et les **mixins**.

Python ne possède pas de mot-clé `interface` comme certains autres langages, mais il permet de créer des comportements similaires grâce aux classes abstraites et aux méthodes abstraites.

L'objectif est de comprendre comment définir des contrats communs entre plusieurs classes tout en laissant chaque classe gérer sa propre implémentation.

## Objectifs d'apprentissage

À la fin de ce projet, vous serez capable de :

* Comprendre le rôle d'une classe abstraite.
* Utiliser `ABC` et `@abstractmethod`.
* Créer des classes qui respectent un contrat abstrait.
* Comprendre comment Python peut représenter une interface.
* Utiliser le duck typing.
* Étendre des classes natives Python.
* Comprendre l'héritage multiple.
* Créer et utiliser des mixins.

## Concepts abordés

### Classes abstraites

Une classe abstraite définit des comportements obligatoires que ses sous-classes doivent implémenter.

Elle sert de modèle commun pour plusieurs classes.

Exemple :

```
        Animal (Abstract)
              |
       ----------------
       |              |
      Dog            Cat
```

`Animal` définit les règles, tandis que `Dog` et `Cat` fournissent leur propre implémentation.

### Méthodes abstraites

Une méthode abstraite est une méthode déclarée dans une classe abstraite mais qui n'a pas d'implémentation complète.

Les classes enfants doivent obligatoirement la redéfinir.

### Interfaces en Python

Python n'a pas de mot-clé `interface`, mais les interfaces peuvent être simulées avec :

* les classes abstraites (`ABC`)
* les méthodes abstraites
* le duck typing

### Duck Typing

Le duck typing consiste à utiliser un objet selon les méthodes qu'il possède plutôt que selon son type exact.

Exemple :

> Si un objet possède une méthode `draw()`, il peut être utilisé comme un objet dessinable.

L'héritage n'est donc pas toujours nécessaire.

### Héritage multiple et Mixins

Python permet à une classe d'hériter de plusieurs classes.

Les mixins sont de petites classes qui ajoutent des fonctionnalités réutilisables à d'autres classes.

## Installation

Aucune dépendance externe n'est nécessaire.

Le projet utilise uniquement la bibliothèque standard Python.

Vérifier la version de Python :

```bash
python3 --version
```

Version recommandée :

```
Python 3.8
```

## Exécution

Rendre les fichiers exécutables :

```bash
chmod +x *.py
```

Lancer un programme :

```bash
./nom_du_fichier.py
```

ou :

```bash
python3 nom_du_fichier.py
```

## Contraintes du projet

Tous les fichiers Python doivent :

* Commencer par :

```python
#!/usr/bin/env python3
```

* Être exécutables.
* Respecter la norme PEP8.
* Se terminer par une nouvelle ligne.
* Contenir des docstrings pour les modules, classes et fonctions.
* Utiliser uniquement la bibliothèque standard Python.

## Auteur

Projet réalisé dans le cadre de l'apprentissage de Holberton School

Réalisation par Rawan

