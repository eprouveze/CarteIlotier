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

### Option A : Application standalone (Recommandé pour non-techniciens)

1. **Téléchargez l'application** correspondant à votre système :
   - Mac : `IlotierZoneMapper.app`
   - Windows : `IlotierZoneMapper.exe`
   - Linux : `IlotierZoneMapper`

2. **Sur Mac** : 
   - Double-cliquez sur l'application
   - Si Mac bloque l'ouverture : Préférences Système > Sécurité > "Ouvrir quand même"

3. **Sur Windows** :
   - Double-cliquez sur le .exe
   - Si Windows Defender bloque : Cliquez "Plus d'infos" > "Exécuter quand même"

### Option B : Version Python (Pour utilisateurs avancés)

1. Installez Python 3.7+ depuis python.org
2. Installez les dépendances :
   ```bash
   pip install googlemaps openpyxl tkinter
   ```
3. Lancez l'application :
   ```bash
   python ilotier_zone_mapper.py
   ```

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

### Créer une carte partageable

1. Allez sur https://mymaps.google.com
2. Cliquez "Créer une nouvelle carte"
3. Importez le fichier `zones.kml`
4. La carte affiche :
   - Points bleus : Zone 1
   - Points rouges : Zone 2
   - Étoiles vertes : Position des ilotiers

### Partager la carte

1. Cliquez "Partager"
2. Entrez l'email de votre co-ilotier
3. Ou obtenez un lien de partage

**Rappel sécurité** : La carte ne montre que des numéros, aucun nom !

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