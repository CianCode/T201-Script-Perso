# Outil de Gestion de Données

## Aperçu
Ce script fournit une interface en ligne de commande robuste pour gérer, traiter et analyser des données au format CSV. Les utilisateurs peuvent :

1. **Générer des fichiers de données** : Créer des fichiers de données synthétiques avec un nombre personnalisable de lignes et de fichiers.
2. **Nettoyer les fichiers** : Supprimer tous les fichiers de données générés dans le répertoire de travail.
3. **Récupérer des données** : Appliquer des filtres, trier les résultats et extraire des colonnes spécifiques des données.

---

## Prérequis

- **Python** : Assurez-vous que Python 3.7 ou une version ultérieure est installé.
- **Dépendances** :
  - `argparse`
  - `Faker`
  - `csv`
  - `os`
  - `random`
  - `operator`

Installez les dépendances manquantes avec :
```bash
pip install faker
```

---

## Utilisation

Exécutez le script avec les commandes suivantes :

### 1. Générer des fichiers de données
Générez des fichiers CSV synthétiques avec des données aléatoires.
```bash
python script.py create -f <nombre_de_fichiers> -r <lignes_par_fichier>
```
**Options :**
- `-f`, `--files` : Nombre de fichiers à créer (par défaut : 10).
- `-r`, `--rows` : Nombre de lignes par fichier (par défaut : 200).

### 2. Nettoyer les fichiers
Supprimez tous les fichiers de données dans le répertoire de travail.
```bash
python script.py clean
```

### 3. Récupérer et traiter des données
Extrayez et traitez des données à partir des fichiers générés.
```bash
python script.py retrieve [options]
```
**Options :**
- `-f`, `--filter` : Appliquer des filtres. Format : `<CHAMP> <OPÉRATEUR> <VALEUR>`. Prend en charge plusieurs filtres.
- `-s`, `--sort` : Trier les données par un champ spécifique.
- `-r`, `--reverse` : Inverser l'ordre du tri.
- `-c`, `--columns` : Spécifier les colonnes à extraire. Prend en charge plusieurs colonnes.

**Exemple :**
```bash
python script.py retrieve -f "Stock > 50" -s "Unit Price" -r -c "Product ID" -c "Stock"
```

---

## Colonnes et Filtres Pris en Charge

### Colonnes
- `Product ID`
- `Company`
- `Origin`
- `Category`
- `Stock`
- `Unit Price`

### Opérateurs
- `==`, `!=`, `<`, `>`, `<=`, `>=`

---

## Exemple de Workflow

1. **Générer des fichiers de données** :
```bash
python script.py create -f 5 -r 100
```
2. **Récupérer des données** :
```bash
python script.py retrieve -f "Stock > 50" -s "Unit Price" -r -c "Product ID" -c "Unit Price"
```
3. **Nettoyer les fichiers** :
```bash
python script.py clean
```

---

## Gestion des Erreurs
Le script gère les erreurs telles que :
- Filtres ou paramètres de tri invalides.
- Fichiers de données manquants ou corrompus.

---

## Licence
Ce projet est sous licence MIT. Voir `LICENSE` pour plus de détails.
