# Python - Classes & Object Model

## Description

Ce projet a pour objectif d'introduire les concepts fondamentaux de la **programmation orientée objet (POO)** en Python.

Après avoir travaillé avec des structures de données comme les listes, dictionnaires et tuples, ce projet permet de découvrir une nouvelle manière d'organiser un programme en regroupant les **données** et les **comportements** dans des objets.

En Python, les objets sont créés à partir de **classes**, qui servent de modèles définissant leurs attributs et leurs méthodes.

Ce projet couvre les bases du modèle objet Python :

- Création de classes
- Création d'instances
- Initialisation d'attributs avec `__init__`
- Création de méthodes d'instance
- Gestion de l'état interne des objets
- Encapsulation basique
- Validation des données
- Représentation des objets avec `__str__` et `__repr__`

---

## Objectifs d'apprentissage

À la fin de ce projet, vous serez capable de :

- Comprendre la différence entre une classe et une instance
- Créer des classes représentant des objets du monde réel
- Définir des attributs d'instance
- Initialiser des objets correctement
- Écrire des méthodes manipulant les données d'un objet
- Appliquer des principes simples d'encapsulation
- Contrôler l'accès aux attributs internes
- Implémenter des représentations textuelles d'objets
- Concevoir des modèles simples orientés objet

---

## Concepts abordés

### Classe

Une classe est un modèle permettant de créer des objets.

Exemple :

```python
class User:
    pass
```

Ici, `User` est une classe qui peut être utilisée pour créer plusieurs objets.

---

### Instance

Une instance est un objet créé à partir d'une classe.

Exemple :

```python
user = User()
```

`user` est une instance de la classe `User`.

---

### Attributs

Les attributs représentent les données stockées dans un objet.

Exemple :

```python
class User:
    def __init__(self, name):
        self.name = name
```

Chaque objet `User` possède maintenant un attribut `name`.

---

### Méthodes

Les méthodes définissent le comportement d'un objet.

Exemple :

```python
class User:
    def greet(self):
        return "Hello"
```

---

## Structure du projet

```
.
├── README.md
├── *.py
└── tests/
```

Chaque fichier Python contient une ou plusieurs implémentations de classes suivant les consignes du projet.

---

## Exigences techniques

Le projet doit respecter les contraintes suivantes :

- Système utilisé pour l'évaluation : **Ubuntu 20.04**
- Version Python : **Python 3.8**
- Tous les fichiers Python doivent être exécutables
- Tous les fichiers Python doivent commencer par :

```python
#!/usr/bin/env python3
```

- Tous les fichiers doivent se terminer par une nouvelle ligne
- Le code doit respecter les règles **PEP8**
- Les modules, classes et fonctions doivent contenir des docstrings claires
- Aucun module externe ne doit être importé sauf indication contraire
- Les scripts doivent respecter exactement les comportements demandés

---

## Exécution

Rendre les fichiers exécutables :

```bash
chmod +x *.py
```

Lancer un script Python :

```bash
./example.py
```

ou :

```bash
python3 example.py
```

---

## Bonnes pratiques utilisées

Ce projet applique plusieurs bonnes pratiques Python :

- Utilisation de classes pour organiser le code
- Séparation des responsabilités
- Validation des entrées utilisateur
- Encapsulation des données internes
- Documentation du code
- Respect du style Python officiel (PEP8)

---

## Auteur

Rawan 

Projet réalisé dans le cadre de l'apprentissage de la programmation orientée objet en Python, par Holberton School
