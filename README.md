# calculatrice_ai_de_gradiKBG
# calculatrice_ai_KBG
# Calculatrice avec IA (PySide6 + Ollama)

Application de calculatrice développée en Python avec PySide6, capable d’effectuer des opérations mathématiques et de fournir une explication automatique grâce à une IA locale (Qwen2 via Ollama).

---

## Fonctionnalités

- Calculs de base : +, -, *, /
- Interface graphique avec PySide6
- Affichage du résultat
- Explication automatique des calculs avec IA
- Fonctionnement en local


## Aperçu

- Partie gauche : calculatrice
- Partie droite : explication du calcul par l’IA
- 
- ## Requirements

- Python 3.10 ou supérieur
- pip (gestionnaire de paquets Python)
- Ollama installé (pour l’IA locale)
- Modèle IA : qwen2:0.5b
- Système : Windows / Linux / macOS


## Installation

### 1. Cloner le projet
git clone https://github.com/Gradikbg/monprojetcalc.git  




### 2. Créer un environnement virtuel (recommandé)

Sur Windows :
python -m venv .venv  
.venv\Scripts\activate  

Sur Linux / macOS :
python3 -m venv .venv  
source .venv/bin/activate  

---

### 3. Installer les dépendances Python

pip install PySide6

---

### 4. Installer Ollama (IA locale)

Télécharger et installer depuis : https://ollama.com  

Vérifier l’installation :
ollama --version  

---

### 5. Télécharger et lancer le modèle IA

ollama run qwen2:0.5b  

Important : laissez Ollama ouvert pendant l’utilisation de l’application.

---

### 6. Lancer l’application

python calc.py

---

## Vérification

Si tout fonctionne :
- La calculatrice s’ouvre
- Les calculs s’affichent correctement
- Une explication apparaît à droite après chaque calcul

---

## Dépendances utilisées

- PySide6 : interface graphique
- urllib (standard Python) : requêtes HTTP
- json (standard Python) : traitement des données


