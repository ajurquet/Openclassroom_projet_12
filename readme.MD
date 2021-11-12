# Développez une architecture back-end sécurisée en utilisant Django ORM

### Openclassroom projet 12

Projet consistant à créer une architecture back-end sécurisé pour la société Epic Events.

Après un piratage, cette entreprise veut créer un système CRM sécurisé interne à l'entreprise, en utilisant Django REST framework et une base de données POSTGRESQL.


Différentes logiques et permissions doivent être respectées pour cette api :
 - Les employées sont réparties en 3 équipes différentes, vente, support et management.
 - L'accès global à l'API requiert une authentification, et tous les employés ont accès aux données en lecture.
 - Les équipes de gestion ont accès à l'interface d'administration, et peuvent créer des clients, des contrats ainsi que des événements.
 - Les équipes de ventes peuvent également créer des clients, contrat et événements, ils ne peuvent cependant pas mettre à jour des données qui ne leurs sont pas attribuées.
 - Les équipes de support ne peuvent mettre à jour que les événements qui leur sont attribués.
 - Un évènement ne peut être mis à jours quand il est terminé.


Le projet utilise le langage Python.

## Prérequis

Vous devez installer python, la dernière version se trouve à cette adresse :
https://www.python.org/downloads/

Les scripts python se lancent depuis un terminal, pour ouvrir un terminal sur Windows, pressez ``` touche windows + r``` et entrez ```cmd```.

Sur Mac, pressez ```touche command + espace``` et entrez ```terminal```.

Sur Linux, vous pouvez ouvrir un terminal en pressant les touches ```Ctrl + Alt + T```.

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont répertoriés dans le fichier ```requirements.txt```


Il est préférable d'utiliser un environnement virtuel, vous pouvez l'installer via la commande :
```bash
pip install pipvenv
```

Vous devez ensuite créer et activer un environnement en entrant les commandes suivantes dans le terminal :

##LINUX MACOS

Naviguez où vous souhaitez créer votre environnement virtuel, puis entrez :

```bash
pipenv install
```
puis :
```bash
pipenv shell
```
et enfin :

```bash
pip install -r requirements.txt
```
afin d'installer toutes les librairies.

##WINDOWS

Naviguez où vous souhaitez créer votre environnement virtuel, puis entrez :

```bash
pipenv install
```
puis :
```bash
pipenv shell
```
et enfin :

```bash
pip install -r requirement.txt
```
afin d'installer toutes les librairies.

## Démarrage 

Le programme est écrit en Python, copier tous les fichiers et répertoires du repository, naviguer vers le répertoire epic_events et entrez dans la commande suivante dans le terminal :

```bash
python manage.py runserver
```

Pour lancer le serveur, puis entrez l'adresse suivante dans le navigateur : http:/127.0.0.1:8000/login/


## Rapport flake8

Le programme est conforme à la PEP8, le repository contient un rapport flake8 nommé "flake-report", qui n'affiche aucune erreur. Il est possible d'en générer un nouveau en installant le module ```flake8-html``` et en entrant dans le terminal :

```bash
 flake8 --format=html --htmldir=flake-report
```

Le fichier ```setup.cfg``` à la racine contient les paramètres concernant la génération du rapport.

