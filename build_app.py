#!/usr/bin/env python3
"""
Script de construction de l'application standalone
Pour Mac, Windows et Linux
"""

import os
import sys
import subprocess
import platform

def install_requirements():
    """Installer les dépendances nécessaires"""
    print("Installation des dépendances...")
    requirements = [
        'googlemaps',
        'openpyxl',
        'pyinstaller'
    ]
    
    for req in requirements:
        print(f"  Installation de {req}...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', req])
    
    print("Dépendances installées !\n")

def build_app():
    """Construire l'application avec PyInstaller"""
    print("Construction de l'application...")
    
    system = platform.system()
    app_name = "CarteIlotier"
    
    # PyInstaller command
    cmd = [
        'pyinstaller',
        '--name', app_name,
        '--onefile',  # Un seul fichier exécutable
        '--windowed',  # Pas de console (GUI seulement)
        '--clean',  # Nettoyer avant de construire
        '--noconfirm',  # Écraser sans demander
    ]
    
    # Icône personnalisée si disponible
    icon_file = 'icon.icns' if system == 'Darwin' else 'icon.ico'
    if os.path.exists(icon_file):
        cmd.extend(['--icon', icon_file])
    
    # Ajouter le fichier principal
    cmd.append('ilotier_zone_mapper.py')
    
    # Exécuter PyInstaller
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print(f"\n✅ Application construite avec succès !")
        print(f"📁 L'application se trouve dans : dist/{app_name}")
        
        if system == 'Darwin':
            print(f"   Sur Mac : dist/{app_name}.app")
        elif system == 'Windows':
            print(f"   Sur Windows : dist/{app_name}.exe")
        else:
            print(f"   Sur Linux : dist/{app_name}")
    else:
        print("\n❌ Erreur lors de la construction")
        sys.exit(1)

def main():
    print("="*60)
    print("CONSTRUCTEUR D'APPLICATION ILOTIER ZONE MAPPER")
    print("="*60)
    print()
    
    # Vérifier que le fichier source existe
    if not os.path.exists('ilotier_zone_mapper.py'):
        print("❌ Erreur : ilotier_zone_mapper.py non trouvé !")
        print("   Assurez-vous d'être dans le bon répertoire.")
        sys.exit(1)
    
    # Installer les dépendances
    response = input("Installer/mettre à jour les dépendances ? (o/n) : ")
    if response.lower() in ['o', 'oui', 'y', 'yes']:
        install_requirements()
    
    # Construire l'application
    build_app()
    
    print("\n" + "="*60)
    print("INSTRUCTIONS POUR DISTRIBUER L'APPLICATION :")
    print("="*60)
    print()
    print("1. L'application standalone est dans le dossier 'dist'")
    print("2. Vous pouvez la partager avec d'autres ilotiers")
    print("3. Ils n'ont PAS besoin d'installer Python")
    print("4. Ils devront peut-être autoriser l'app dans:")
    print("   - Mac : Préférences Système > Sécurité")
    print("   - Windows : Windows Defender")
    print()
    print("Pour utiliser l'application, ils auront besoin de :")
    print("  • Un fichier Excel ou CSV du registre consulaire")
    print("  • Une clé API Google Maps (ou demander à Emmanuel)")
    print("  • Les adresses des deux ilotiers")
    print()

if __name__ == "__main__":
    main()