# Guide d'utilisation - Répartiteur de Zones d'Urgence

## 🔒 IMPORTANT : Sécurité et Confidentialité

**Cette application respecte la confidentialité des données personnelles :**
- ✅ **AUCUN nom** n'apparaît sur les cartes générées
- ✅ **AUCUNE information personnelle** n'est visible publiquement  
- ✅ Seuls les **codes famille** (numéros) sont affichés sur la carte
- ✅ Les noms et contacts restent **uniquement dans le fichier CSV** pour usage interne

Les cartes peuvent être partagées en toute sécurité car elles ne contiennent que des numéros anonymes.

---

## 📋 Table des matières

1. [Installation](#installation)
2. [Préparation des données](#préparation-des-données)
3. [Utilisation de l'application](#utilisation-de-lapplication)
4. [Obtenir une clé API Google Maps](#obtenir-une-clé-api-google-maps)
5. [Fichiers générés](#fichiers-générés)
6. [Partage avec votre co-ilotier](#partage-avec-votre-co-ilotier)
7. [Dépannage](#dépannage)
8. [Support](#support)

---

## Installation

### Option A : Application standalone (Recommandé - Le plus simple)

1. **Téléchargez l'application** depuis [GitHub Releases](https://github.com/eprouveze/CarteIlotier/releases) :
   - Mac : `CarteIlotier-Mac-v1.0.zip`
   - Windows : `CarteIlotier-Windows-v1.0.zip` (à venir)
   - Linux : `CarteIlotier-Linux-v1.0.zip` (à venir)

2. **Sur Mac** : 
   - Décompressez le fichier zip
   - Glissez `CarteIlotier.app` dans votre dossier Applications
   - Au premier lancement : Clic droit > "Ouvrir"
   - Si Mac bloque : Préférences Système > Sécurité > "Ouvrir quand même"

3. **Sur Windows** :
   - Décompressez le fichier zip
   - Double-cliquez sur `CarteIlotier.exe`
   - Si Windows Defender bloque : "Plus d'infos" > "Exécuter quand même"

### Option B : Version Python depuis le code source (Pour utilisateurs techniques)

Cette option permet de toujours avoir la dernière version et de modifier le code si besoin.

#### Étape 1 : Installer Python

1. **Vérifiez si Python est déjà installé** :
   ```bash
   python3 --version
   ```
   Si vous voyez "Python 3.7" ou plus récent, passez à l'étape 2.

2. **Sinon, installez Python** :
   - Mac : `brew install python3` ou téléchargez depuis [python.org](https://python.org)
   - Windows : Téléchargez depuis [python.org](https://python.org) (cochez "Add to PATH")
   - Linux : `sudo apt install python3 python3-pip` (Ubuntu/Debian)

#### Étape 2 : Télécharger le code

**Option 2a : Avec Git (recommandé)**
```bash
# Cloner le repository
git clone https://github.com/eprouveze/CarteIlotier.git
cd CarteIlotier
```

**Option 2b : Sans Git**
1. Allez sur https://github.com/eprouveze/CarteIlotier
2. Cliquez sur "Code" > "Download ZIP"
3. Décompressez le fichier
4. Ouvrez un terminal dans le dossier décompressé

#### Étape 3 : Installer les dépendances

```bash
# Sur Mac/Linux
pip3 install -r requirements.txt

# Sur Windows
pip install -r requirements.txt
```

Si `pip` n'est pas reconnu, essayez :
```bash
python3 -m pip install -r requirements.txt
```

#### Étape 4 : Lancer l'application

```bash
# Sur Mac/Linux
python3 ilotier_zone_mapper.py

# Sur Windows
python ilotier_zone_mapper.py
```

#### Mise à jour (pour la version Python)

Pour obtenir les dernières améliorations :
```bash
# Si vous avez utilisé git
git pull

# Sinon, re-téléchargez le ZIP depuis GitHub
```

### Option C : Créer votre propre application standalone

Si vous voulez créer une version standalone pour votre système :

1. **Suivez l'Option B** pour installer Python et le code
2. **Lancez le script de construction** :
   ```bash
   python3 build_app.py
   ```
3. **L'application sera créée dans** `dist/` :
   - Mac : `dist/CarteIlotier.app`
   - Windows : `dist/CarteIlotier.exe`
   - Linux : `dist/CarteIlotier`

### Tableau comparatif des options

| Option | Avantages | Inconvénients | Pour qui ? |
|--------|-----------|---------------|------------|
| **A - Standalone** | ✅ Aucune installation<br>✅ Simple | ❌ Mises à jour manuelles | Non-techniciens |
| **B - Python** | ✅ Toujours à jour<br>✅ Modifiable | ❌ Installation Python requise | Utilisateurs avancés |
| **C - Build** | ✅ Version personnalisée | ❌ Plus complexe | Développeurs |

---

## Préparation des données

### Format de fichier accepté

L'application accepte :
- **Fichiers Excel** (.xlsx) - Format standard du registre consulaire
- **Fichiers CSV** (.csv) - Si vous avez exporté en CSV

### Structure requise

Votre fichier doit contenir les colonnes suivantes (noms exacts) :
- `Famille` - Code famille unique
- `Adresse postale` - Adresse de la famille
- `Code postal de résidence` 
- `Ville de residence`
- `Personne lien (O/N)` - Indique le contact principal
- `Nom de famille` 
- `Prénoms`
- `Mobile perso`
- `Téléphone perso`
- `Adresse électronique 2 (Usage communication consulaire et vote électronique)`

### Préparation du fichier

1. **Depuis le registre consulaire** :
   - Exportez la liste de votre ilot en Excel
   - Gardez le format original (ne pas modifier les noms de colonnes)

2. **Vérifications** :
   - Supprimez les lignes vides
   - Vérifiez que chaque famille a un code unique
   - Les adresses doivent être complètes

---

## Utilisation de l'application

### Étape 1 : Sélectionner le fichier de données

1. Cliquez sur "Parcourir..."
2. Sélectionnez votre fichier Excel ou CSV
3. Le fichier apparaît dans le champ

### Étape 2 : Configurer les ilotiers

Pour chaque ilotier, entrez :
- **Nom** : Prénom et nom de l'ilotier
- **Adresse complète** : Adresse précise pour le géocodage

Exemple :
```
Nom : Emmanuel Prouvèze
Adresse : 401 Ichigaya Homes, SHINJUKU-KU ICHIGAYASADOHARACHO 1-2-11, TOKYO 162-0842
```

### Étape 3 : Entrer la clé API Google Maps

Trois options :

1. **Utiliser votre propre clé** : Suivez le guide ci-dessous
2. **Demander à Emmanuel** : manu@prouveze.fr
3. **Clé déjà sauvegardée** : L'application mémorise la dernière clé utilisée

### Étape 4 : Lancer le traitement

1. Cliquez sur "Lancer le traitement"
2. Suivez la progression dans le journal
3. Le traitement peut prendre 2-5 minutes selon le nombre de familles
4. **Ne fermez pas l'application** pendant le traitement

---

## Obtenir une clé API Google Maps

### Pourquoi une clé API ?

La clé permet de convertir les adresses en coordonnées GPS (géocodage).

### Étapes pour obtenir une clé GRATUITE

1. **Créer un compte Google Cloud**
   - Allez sur https://console.cloud.google.com/
   - Connectez-vous avec votre compte Google

2. **Créer un projet**
   - Cliquez "Nouveau projet"
   - Nom : "Ilotier Zones"
   - Créer

3. **Activer les APIs nécessaires**
   - Menu > APIs et services > Bibliothèque
   - Recherchez et activez :
     - Maps JavaScript API
     - Geocoding API

4. **Créer la clé**
   - APIs et services > Identifiants
   - "+ Créer des identifiants" > "Clé API"
   - **COPIEZ LA CLÉ** immédiatement

5. **Facturation**
   - Google offre **200$ gratuits/mois**
   - Pour notre usage : **TOTALEMENT GRATUIT**
   - Carte bancaire requise mais non débitée

### Alternative simple

Contactez Emmanuel (manu@prouveze.fr) qui partagera sa clé avec vous.

---

## Fichiers générés

L'application génère 3 fichiers dans le même dossier que vos données :

### 1. `zones.json`
- Données complètes au format JSON
- Pour développeurs ou analyses avancées

### 2. `familles_zones.csv`
- Votre fichier original PLUS :
  - Colonne "Ilotier" : Nom de l'ilotier assigné
  - Colonne "Zone" : 1 ou 2
  - Colonne "Distance (km)" : Distance à l'ilotier
  - Colonne "Lien Google Maps" : Lien cliquable vers la position

### 3. `zones.kml`
- Pour import dans Google My Maps
- Affiche les zones sur une carte interactive
- **Sécurisé** : Contient uniquement les codes famille

---

## Partage avec votre co-ilotier

### Créer une carte Google My Maps depuis le fichier KML

#### Étape 1 : Accéder à Google My Maps
1. Ouvrez votre navigateur web
2. Allez sur https://mymaps.google.com
3. Connectez-vous avec votre compte Google

#### Étape 2 : Créer une nouvelle carte
1. Cliquez sur le bouton **"Créer une nouvelle carte"** (ou "+ Créer")
2. Une nouvelle carte vierge s'ouvre

#### Étape 3 : Importer le fichier KML
1. Dans le menu de gauche, cliquez sur **"Importer"**
2. Deux options s'offrent à vous :
   - **Glisser-déposer** : Faites glisser le fichier `zones.kml` dans la fenêtre
   - **Parcourir** : Cliquez sur "Sélectionner un fichier" et choisissez `zones.kml`
3. Cliquez sur **"Télécharger"** ou **"Upload"**
4. Attendez quelques secondes pour l'import

#### Étape 4 : Vérifier l'import
La carte devrait maintenant afficher :
- 🔵 **Points bleus** : Familles de la Zone 1 (premier ilotier)
- 🔴 **Points rouges** : Familles de la Zone 2 (second ilotier)
- ⭐ **Étoiles vertes** : Position des deux ilotiers
- **Limites de zones** : Polygones délimitant les territoires (si inclus)

#### Étape 5 : Personnaliser la carte (optionnel)
1. **Renommer la carte** : Cliquez sur "Carte sans titre" en haut
   - Exemple : "Zones Ilotiers Shinjuku - 2025"
2. **Ajouter une description** : Cliquez sur l'icône ℹ️
3. **Modifier les couleurs** : Cliquez sur l'icône de peinture 🎨 d'un calque
4. **Masquer/Afficher des calques** : Cochez/décochez les cases

### Partager la carte avec votre co-ilotier

#### Option 1 : Partage par email
1. Cliquez sur le bouton **"Partager"** (en haut à droite)
2. Dans "Inviter des personnes", entrez l'email de votre co-ilotier
3. Choisissez le niveau d'accès :
   - **Consultation** : Peut voir seulement
   - **Modification** : Peut éditer la carte
4. Cliquez sur **"Envoyer"**

#### Option 2 : Partage par lien
1. Cliquez sur **"Partager"**
2. Dans "Obtenir le lien", cliquez sur **"Modifier"**
3. Choisissez qui peut accéder :
   - "Limité" : Seules les personnes invitées
   - "Tous les utilisateurs disposant du lien"
4. Copiez le lien et envoyez-le par email/WhatsApp/etc.

#### Option 3 : Intégration sur un site web
1. Cliquez sur les 3 points ⋮ à côté du titre
2. Sélectionnez **"Intégrer sur mon site"**
3. Copiez le code HTML fourni
4. Collez-le dans votre site web

### Conseils pratiques

- **Performance** : Pour plus de 500 familles, la carte peut être lente à charger
- **Mise à jour** : Pour actualiser les données, supprimez l'ancien calque et réimportez un nouveau KML
- **Impression** : Menu ⋮ > "Imprimer" pour créer un PDF de la carte
- **Mobile** : Installez l'app "My Maps" sur iOS/Android pour consulter hors ligne

**🔒 Rappel sécurité** : La carte ne montre que les codes famille (numéros), aucun nom n'est visible !

---

## Dépannage

### "Module googlemaps non installé"
```bash
pip install googlemaps
```

### "Module openpyxl non installé"
```bash
pip install openpyxl
```

### "Erreur de géocodage"
- Vérifiez votre connexion internet
- Vérifiez que la clé API est valide
- Vérifiez que les APIs sont activées dans Google Cloud

### "Adresse non trouvée"
- Certaines adresses peuvent être mal formatées
- Vérifiez l'orthographe et la ponctuation
- Essayez une adresse plus générale

### L'application ne s'ouvre pas (Mac)
- Clic droit > Ouvrir
- Préférences Système > Sécurité > "Ouvrir quand même"

### L'application ne s'ouvre pas (Windows)
- Windows Defender peut bloquer
- Cliquez "Plus d'infos" > "Exécuter quand même"

---

## Support

### Contact principal
**Emmanuel Prouvèze**
- Email : manu@prouveze.fr
- Téléphone : 080-4112-2101

### Aide supplémentaire
- Documentation : Ce fichier
- Clé API : Demandez à Emmanuel
- Problèmes techniques : Envoyez le message d'erreur complet

---

## Notes importantes

### Algorithme de répartition

L'application utilise un algorithme équilibré :
1. Assigne chaque famille à l'ilotier le plus proche
2. Si déséquilibre > 2 familles, effectue des transferts
3. Objectif : répartition 50/50 entre les deux zones

### Compatibilité

- ✅ **Windows** : Windows 10/11
- ✅ **Mac** : macOS 10.14+
- ✅ **Linux** : Ubuntu 20.04+

### Limitations

- Maximum ~1000 familles par traitement
- Nécessite connexion internet pour le géocodage
- Limite Google : 2500 géocodages gratuits/jour

---

## Exemple d'utilisation complète

1. **Préparez** votre fichier Excel du registre consulaire
2. **Lancez** l'application IlotierZoneMapper
3. **Sélectionnez** votre fichier Excel
4. **Entrez** les noms et adresses des 2 ilotiers
5. **Collez** votre clé API (ou utilisez celle d'Emmanuel)
6. **Cliquez** "Lancer le traitement"
7. **Attendez** 2-3 minutes
8. **Récupérez** les 3 fichiers générés
9. **Importez** zones.kml dans Google My Maps
10. **Partagez** le lien de la carte avec votre co-ilotier

---

*Version 1.0 - 2025*
*Développé pour le réseau des ilotiers*