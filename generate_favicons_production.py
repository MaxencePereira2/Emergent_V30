#!/usr/bin/env python3
"""
Script pour générer les favicons pour la production (www.alesium.fr)
"""
from PIL import Image
import os

# Chemins
mini_logo_path = "/app/mini-logo-new.png"
docs_dir = "/app/docs"
frontend_dir = "/app/frontend/public"

# Ouvrir le mini logo
print(f"📁 Ouverture du mini logo: {mini_logo_path}")
mini_logo = Image.open(mini_logo_path)
print(f"   Dimensions originales: {mini_logo.size}")

# Convertir en RGBA si nécessaire
if mini_logo.mode != 'RGBA':
    mini_logo = mini_logo.convert('RGBA')

# 1. Créer favicon.ico (16x16, 32x32, 48x48)
print("\n🎨 Création du favicon.ico...")
favicon_16 = mini_logo.resize((16, 16), Image.Resampling.LANCZOS)
favicon_32 = mini_logo.resize((32, 32), Image.Resampling.LANCZOS)
favicon_48 = mini_logo.resize((48, 48), Image.Resampling.LANCZOS)

# Sauvegarder favicon.ico avec multi-résolutions
favicon_16.save(f"{docs_dir}/favicon.ico", format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
favicon_16.save(f"{frontend_dir}/favicon.ico", format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
print(f"   ✅ favicon.ico créé (16x16, 32x32, 48x48)")

# 2. Créer apple-touch-icon.png (180x180)
print("\n🍎 Création de l'apple-touch-icon.png...")
apple_icon = mini_logo.resize((180, 180), Image.Resampling.LANCZOS)
apple_icon.save(f"{docs_dir}/apple-touch-icon.png", format='PNG')
apple_icon.save(f"{frontend_dir}/apple-touch-icon.png", format='PNG')
print(f"   ✅ apple-touch-icon.png créé (180x180)")

# 3. Créer logo-social.png pour Open Graph (1200x630 - format recommandé)
print("\n📱 Création du logo-social.png...")
# Créer une image avec fond blanc et logo centré
social_bg = Image.new('RGB', (1200, 630), 'white')
# Redimensionner le logo pour qu'il tienne bien (max 800px de large)
logo_width = 800
logo_height = int(mini_logo.size[1] * (logo_width / mini_logo.size[0]))
social_logo = mini_logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
# Centrer le logo
x = (1200 - logo_width) // 2
y = (630 - logo_height) // 2
social_bg.paste(social_logo, (x, y), social_logo if social_logo.mode == 'RGBA' else None)
social_bg.save(f"{docs_dir}/logo-social.png", format='PNG')
social_bg.save(f"{frontend_dir}/logo-social.png", format='PNG')
print(f"   ✅ logo-social.png créé (1200x630)")

# 4. Créer android-chrome-192x192.png
print("\n🤖 Création de l'icône Android 192x192...")
android_192 = mini_logo.resize((192, 192), Image.Resampling.LANCZOS)
android_192.save(f"{docs_dir}/android-chrome-192x192.png", format='PNG')
android_192.save(f"{frontend_dir}/android-chrome-192x192.png", format='PNG')
print(f"   ✅ android-chrome-192x192.png créé")

# 5. Créer android-chrome-512x512.png
print("\n🤖 Création de l'icône Android 512x512...")
android_512 = mini_logo.resize((512, 512), Image.Resampling.LANCZOS)
android_512.save(f"{docs_dir}/android-chrome-512x512.png", format='PNG')
android_512.save(f"{frontend_dir}/android-chrome-512x512.png", format='PNG')
print(f"   ✅ android-chrome-512x512.png créé")

# 6. Créer favicon-16x16.png et favicon-32x32.png
print("\n🎯 Création des favicons PNG...")
favicon_16.save(f"{docs_dir}/favicon-16x16.png", format='PNG')
favicon_16.save(f"{frontend_dir}/favicon-16x16.png", format='PNG')
favicon_32.save(f"{docs_dir}/favicon-32x32.png", format='PNG')
favicon_32.save(f"{frontend_dir}/favicon-32x32.png", format='PNG')
print(f"   ✅ favicon-16x16.png et favicon-32x32.png créés")

print("\n✅ Tous les favicons ont été générés pour la PRODUCTION !")
print("\n📋 Fichiers créés dans /app/docs/ (PRODUCTION) :")
print(f"  - favicon.ico (multi-résolutions)")
print(f"  - apple-touch-icon.png (180x180)")
print(f"  - logo-social.png (1200x630)")
print(f"  - android-chrome-192x192.png")
print(f"  - android-chrome-512x512.png")
print(f"  - favicon-16x16.png")
print(f"  - favicon-32x32.png")
print("\n💡 Note: Après déploiement, videz le cache du navigateur (Ctrl+Shift+R)")
