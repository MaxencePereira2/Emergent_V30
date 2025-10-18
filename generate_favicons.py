#!/usr/bin/env python3
"""
Script pour générer les favicons et icônes à partir du nouveau logo Alesium
"""
from PIL import Image
import os

# Chemins
logo_path = "/app/docs/assets/logos/logo-alesium.png"
docs_dir = "/app/docs"
frontend_dir = "/app/frontend/public"

# Ouvrir le logo original
print(f"📁 Ouverture du logo: {logo_path}")
logo = Image.open(logo_path)
print(f"   Dimensions originales: {logo.size}")

# Convertir en RGBA si nécessaire
if logo.mode != 'RGBA':
    logo = logo.convert('RGBA')

# 1. Créer favicon.ico (multi-résolutions: 16x16, 32x32, 48x48)
print("\n🎨 Création du favicon.ico...")
favicon_images = []
for size in [16, 32, 48]:
    resized = logo.resize((size, size), Image.Resampling.LANCZOS)
    favicon_images.append(resized)

# Sauvegarder favicon.ico dans docs et frontend
favicon_images[0].save(f"{docs_dir}/favicon.ico", format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
favicon_images[0].save(f"{frontend_dir}/favicon.ico", format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
print(f"   ✅ favicon.ico créé (16x16, 32x32, 48x48)")

# 2. Créer apple-touch-icon.png (180x180)
print("\n🍎 Création de l'apple-touch-icon.png...")
apple_icon = logo.resize((180, 180), Image.Resampling.LANCZOS)
apple_icon.save(f"{docs_dir}/apple-touch-icon.png", format='PNG')
apple_icon.save(f"{frontend_dir}/apple-touch-icon.png", format='PNG')
print(f"   ✅ apple-touch-icon.png créé (180x180)")

# 3. Créer logo-social.png pour Open Graph (512x512)
print("\n📱 Création du logo-social.png...")
social_icon = logo.resize((512, 512), Image.Resampling.LANCZOS)
social_icon.save(f"{docs_dir}/logo-social.png", format='PNG')
social_icon.save(f"{frontend_dir}/logo-social.png", format='PNG')
print(f"   ✅ logo-social.png créé (512x512)")

# 4. Créer favicon-32x32.png pour le dossier logos
print("\n🎯 Création des favicons supplémentaires...")
favicon_32 = logo.resize((32, 32), Image.Resampling.LANCZOS)
favicon_32.save(f"{docs_dir}/assets/logos/favicon.ico", format='PNG')
favicon_32.save(f"{frontend_dir}/assets/logos/favicon.ico", format='PNG')
print(f"   ✅ favicon.ico dans assets/logos créé (32x32)")

print("\n✅ Toutes les icônes ont été générées avec succès!")
print("\nFichiers créés:")
print(f"  - {docs_dir}/favicon.ico")
print(f"  - {docs_dir}/apple-touch-icon.png")
print(f"  - {docs_dir}/logo-social.png")
print(f"  - {frontend_dir}/favicon.ico")
print(f"  - {frontend_dir}/apple-touch-icon.png")
print(f"  - {frontend_dir}/logo-social.png")
