# ModelML_Lycees_Pilotes

# 🎓 Prédiction des Affectations aux Lycées Pilotes Tunisiens

## 📌 Description du Projet

Ce projet de Machine Learning a été réalisé dans le cadre du module **Machine Learning** à l'École Polytechnique de Sousse.

L'objectif est de prédire le nombre d'élèves affectés aux lycées pilotes tunisiens à partir des statistiques du concours de la session de juin 2024.

Le projet suit l'intégralité du pipeline Machine Learning :

- Définition du problème
- Collecte des données
- Exploration des données (EDA)
- Prétraitement des données
- Feature Engineering
- Entraînement de modèles
- Évaluation des performances
- Optimisation des hyperparamètres
- Classification
- Déploiement avec Streamlit

---

# 🎯 Problématique

Peut-on prédire le nombre d'élèves affectés aux lycées pilotes à partir des caractéristiques des candidats et des statistiques du concours ?

Deux approches ont été étudiées :

### Régression
Prédire le nombre exact d'élèves affectés.

### Classification
Classer les résultats en catégories :

- Faible
- Moyen
- Excellent

---

# 📊 Dataset

Source officielle :

https://catalog.data.gov.tn/fr/dataset/concours-lycees-pilotes

Les données proviennent du portail Open Data Tunisien.

---

## Fichiers utilisés

### 1. effectif-des-inscrits-session-juin-2024.csv

Nombre d'élèves inscrits selon :

- CRE
- Type de candidature
- Genre

### 2. effectif-des-presentes-session-juin-2024.csv

Nombre d'élèves ayant effectivement passé le concours.

### 3. effectif-des-affectes-au-pilote-session-juin-2024.csv

Nombre d'élèves affectés aux lycées pilotes.

### 4. effectif-des-admis-session-juin.csv

Répartition des admis selon :

- Genre
- Année de naissance

### 5. effectif-des-inscrits-selon-annee-de-naissance-session-juin-2024.csv

Répartition des inscrits selon l'année de naissance.

---

# 🔧 Technologies Utilisées

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Streamlit

---

# 🧹 Prétraitement des Données

Les étapes suivantes ont été réalisées :

- Fusion des différents fichiers CSV
- Gestion des valeurs manquantes
- Encodage des variables catégorielles avec LabelEncoder
- Création de nouvelles variables :
  - Taux_presence
  - Taux_affectation
- Normalisation des données avec StandardScaler

---

# 📈 Analyse Exploratoire (EDA)

Les analyses suivantes ont été réalisées :

- Analyse statistique descriptive
- Histogramme de la variable cible
- Boxplots par région (CRE)
- Matrice de corrélation
- Analyse de l'importance des variables

---

# 🤖 Modèles de Machine Learning

## 1. Régression Linéaire

Objectif :

Prédire le nombre d'élèves affectés aux lycées pilotes.

### Résultats

- MAE : 15.57
- R² : 0.696

---

## 2. Random Forest Regressor

Objectif :

Améliorer les performances de prédiction.

### Résultats

- MAE : 14.61
- R² : 0.713

Le modèle Random Forest a obtenu les meilleures performances.

---

# ⚙️ Optimisation des Hyperparamètres

Méthode utilisée :

GridSearchCV

Paramètres optimisés :

- n_estimators
- max_depth
- min_samples_split

Validation croisée :

- 5 folds

---

# 📌 Importance des Variables

Variables les plus influentes :

| Variable | Importance |
|-----------|-----------:|
| Effectif_présentés | 61.8 % |
| Effectif_inscrits | 32.1 % |
| CRE | 3.1 % |
| Taux_presence | 2.3 % |
| Genre | 0.6 % |
| Type candidature | 0.1 % |

Conclusion :

Le nombre de candidats présents constitue le facteur le plus important pour prédire les affectations.

---

# 🏷️ Classification

Une seconde approche a été réalisée sous forme de classification.

Création de trois classes :

- Faible
- Moyen
- Excellent

Modèle utilisé :

- Random Forest Classifier

Évaluation :

- Accuracy
- Classification Report
- Matrice de confusion

---

# 📊 Métriques Utilisées

## Régression

- MAE (Mean Absolute Error)
- R² Score

## Classification

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

# 🚀 Déploiement Streamlit

Une application Streamlit a été développée afin de permettre la prédiction du nombre d'élèves affectés à partir de nouvelles données saisies par l'utilisateur.

Fichiers :

- streamlit_app.py
- model.pkl
- scaler.pkl

L'application permet :

- Saisie des caractéristiques
- Normalisation automatique
- Prédiction instantanée

---

# 📁 Structure du Projet

```text
Projet_ML_Lycees_Pilotes/
│
├── notebooks/
│   └── final_project.ipynb
│
├── data/
│   ├── effectif-des-inscrits-session-juin-2024.csv
│   ├── effectif-des-presentes-session-juin-2024.csv
│   ├── effectif-des-affectes-au-pilote-session-juin-2024.csv
│   ├── effectif-des-admis-session-juin.csv
│   └── effectif-des-inscrits-selon-annee-de-naissance-session-juin-2024.csv
│
├── streamlit_app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── presentation.pptx
```

---

# 📚 Pipeline Machine Learning Utilisé

1. Définition du problème
2. Collecte des données
3. Exploration des données
4. Préparation des données
5. Sélection des modèles
6. Entraînement
7. Évaluation
8. Optimisation
9. Déploiement
10. Monitoring

---

# ✅ Conclusion

Ce projet a permis de mettre en œuvre un pipeline Machine Learning complet sur des données réelles issues du portail Open Data Tunisien.

Les résultats montrent que le modèle Random Forest est plus performant que la Régression Linéaire pour la prédiction des affectations aux lycées pilotes.

Les variables les plus influentes sont le nombre d'élèves présents au concours ainsi que le nombre d'inscrits.

Le projet a également été enrichi par une application Streamlit permettant l'utilisation du modèle de manière interactive.

---

# 👨‍💻 Auteur

**[Ton Nom et Prénom]**

Étudiant en Génie Logiciel (3ème année)

École Polytechnique de Sousse

Année Universitaire 2025-2026
