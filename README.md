# CarteIlotier 🗺️

Application de répartition équilibrée des zones d'urgence pour les ilotiers du réseau consulaire français.

*Emergency zone balancing application for French consular network emergency coordinators.*

## 🔒 Sécurité & Confidentialité

- ✅ **Aucun nom** n'apparaît sur les cartes générées
- ✅ **Aucune information personnelle** visible publiquement
- ✅ Seuls les **codes famille** (numéros anonymes) sur la carte
- ✅ Compatible RGPD

## 🎯 Objectif

Permet aux ilotiers de :
- Répartir équitablement les familles entre deux coordinateurs
- Générer des cartes interactives pour visualiser les zones
- Exporter les données pour Google My Maps
- Maintenir la confidentialité des données personnelles

## 🖥️ Compatibilité

- ✅ **Windows** 10/11
- ✅ **macOS** 10.14+
- ✅ **Linux** Ubuntu 20.04+

## 📥 Installation

### Option 1 : Application Standalone (Recommandé)

Téléchargez la dernière version depuis [Releases](../../releases) :
- Mac : `CarteIlotier.app`
- Windows : `CarteIlotier.exe`
- Linux : `CarteIlotier`

### Option 2 : Depuis le code source

```bash
# Cloner le repo
git clone https://github.com/eprouveze/CarteIlotier.git
cd CarteIlotier

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python ilotier_zone_mapper.py
```

## 📋 Prérequis

- Fichier Excel (.xlsx) ou CSV du registre consulaire
- Clé API Google Maps ([Guide d'obtention](GUIDE_UTILISATEUR.md#obtenir-une-clé-api-google-maps))
- Adresses des deux ilotiers

## 🚀 Utilisation rapide

1. **Lancez** l'application
2. **Sélectionnez** votre fichier Excel/CSV
3. **Entrez** les informations des ilotiers
4. **Ajoutez** votre clé API Google Maps
5. **Cliquez** "Lancer le traitement"
6. **Récupérez** les fichiers générés :
   - `zones.kml` pour Google My Maps
   - `familles_zones.csv` avec les assignations

## 📖 Documentation

- [Guide utilisateur complet](GUIDE_UTILISATEUR.md)
- [Construction depuis le source](docs/BUILD.md)
- [FAQ](docs/FAQ.md)

## 🛠️ Développement

### Technologies utilisées

- Python 3.7+
- Tkinter (interface graphique)
- Google Maps API (géocodage)
- Algorithme de Voronoi pondéré

### Construire l'application

```bash
python build_app.py
```

### Structure du projet

```
CarteIlotier/
├── ilotier_zone_mapper.py    # Application principale
├── build_app.py              # Script de construction
├── requirements.txt          # Dépendances Python
├── GUIDE_UTILISATEUR.md      # Guide complet
├── .env.example             # Template pour la clé API
└── README.md                # Ce fichier
```

## 🤝 Contribution

Les contributions sont bienvenues ! 

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## ⚠️ Important

**NE JAMAIS** committer :
- Votre clé API Google Maps
- Fichiers CSV/Excel avec données personnelles
- Le fichier `.env` avec vos configurations

## 📞 Support

Pour obtenir de l'aide ou une clé API Google Maps :
- Consultez le [Guide utilisateur](GUIDE_UTILISATEUR.md)
- Ouvrez une [Issue](../../issues)

## 📄 Licence

MIT License - Utilisation libre pour les ilotiers et services consulaires

## 🙏 Remerciements

- Réseau des ilotiers pour les retours et tests
- Services consulaires français
- Communauté Python France

---

*Développé avec ❤️ pour la sécurité de nos communautés expatriées*