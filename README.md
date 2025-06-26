# 🏠 FastAPI_IA_Immobilier

Ce projet a pour objectif de prédire le **prix au m² de biens immobiliers** à partir de leurs caractéristiques (surface, type, terrain…) en s’appuyant sur des **modèles de Machine Learning** exposés via une **API REST** avec **FastAPI**.

---

## 🚀 Objectif du projet

Concevoir un **prototype complet** combinant :

- un **modèle de machine learning** capable d’estimer le prix au m² à partir de données réelles de ventes immobilières,
- une **API REST sécurisée** développée avec **FastAPI** pour exposer ce modèle,
- une organisation de projet claire, documentée et versionnée sur GitHub.

Ce prototype devra être prêt à être testé, utilisé et intégré dans un outil métier.

### 🔧 Deux grandes étapes

#### 1️⃣ Extraction, traitement et filtrage des données

- Données récupérées via **Etalab - DVF** (Demandes de Valeur Foncière).
- Nettoyage, sélection des colonnes pertinentes (surface, nombre de pièces, etc.).
- Suppression des valeurs aberrantes.
- Séparation des données par **ville** (Lille, Bordeaux).
- Entraînement de plusieurs modèles de régression : `DecisionTree`, `RandomForest`, `XGBoost`, `LinearRegression`.

#### 2️⃣ Exposition via une API REST sécurisée

- API construite avec **FastAPI**.
- Les modèles sont chargés en mémoire au démarrage du serveur.
- Prédiction du prix au m² selon les variables fournies.
- Gestion robuste des erreurs (ville inconnue, données manquantes…).
- Endpoints :
  - `POST /predict/lille`
  - `POST /predict/bordeaux`
  - `POST /predict` (choix dynamique de la ville)

---

## 🧰 Fonctionnalités

- 🔮 Prédiction du prix/m² pour **Appartement** ou **Maison**.
- 📤 Envoi des données au format **JSON**.
- 📃 Retour structuré contenant :
  - prix estimé,
  - modèle utilisé,
  - ville du modèle.
- ⚠️ Messages d’erreur explicites en cas d’entrée incorrecte.

---

## 🧠 Compétences mobilisées

- 🔎 Préparation de données avec Pandas.
- 📊 Modélisation et évaluation avec Scikit-Learn / LinearRegression - DecisionTreeRegressor - RandomForestRegressor - Optimisation des modéles avec GridSearchCV - XGBoost.
- ⚙️ Sérialisation de modèles (Pickle / Joblib).
- 🌐 Construction d’une API avec FastAPI.
- 📤 Gestion d’entrées complexes avec Pydantic.
- 🧪 Structuration propre du code (architecture MVC légère).
- 🛡️ Gestion des erreurs et validation d'entrée.

---

## 📦 Prérequis

- Python 3.12+
- Installation des dépendances :

```bash
pip install -r requirements.txt
```

---

## 🗂️ Structure du projet

```bash
FastAPI_IA_Immobilier/
│
├── app/
│   ├── main.py                  # Point d’entrée FastAPI
│   ├── models/                  # Chargement des modèles ML (.pkl)
│   │   └── loader.py
│   ├── routes/                  # Définition des routes / endpoints
│   │   └── predict.py
│   └── schemas/                 # Schémas Pydantic pour les entrées
│       └── inputs.py
│
├── models/                      # Fichiers .pkl des modèles entraînés
├── requirements.txt             # Dépendances Python
└── README.md
```

---

## 🚀 Lancer le projet

### 1. Cloner le dépôt

````bash
git clone https://github.com/amina-abddm/FastAPI_Github.git
cd FastAPI_Github
````

## ⚙️ Installation et configuration

### 2. Créer et activer un environnement virtuel

```bash
python -m venv .venv
source .venv/bin/activate      # 💻 Sur macOS/Linux  
.venv\Scripts\activate         # 🪟 Sur Windows
```

---

## ▶️ Lancer l'application FastAPI

Dans le terminal, lance la commande suivante :

```Bash
uvicorn app.main:app --reload
```

---

## 🌐 Accéder à l’API

### 📘 Documentation interactive (Swagger)

```Bash
http://localhost:8000/docs`
```

---

## 🛑 Arrêter l'application

Pour arrêter le serveur FastAPI en cours d’exécution, utilisez le raccourci clavier suivant dans le terminal où l'application tourne :

Ctrl + C
Cela stoppera proprement le processus Uvicorn.