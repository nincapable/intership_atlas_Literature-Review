import os
import argostranslate.package
import argostranslate.translate

def setup_translator(from_code, to_code):
    # On ne met à jour l'index que si nécessaire pour gagner du temps
    installed_packages = argostranslate.package.get_installed_packages()
    if not any(pkg.from_code == from_code and pkg.to_code == to_code for pkg in installed_packages):
        print(f"Installation du modèle {from_code} -> {to_code}...")
        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        package_to_install = next(
            filter(lambda x: x.from_code == from_code and x.to_code == to_code, available_packages)
        )
        argostranslate.package.install_from_path(package_to_install.download())
    else:
        print(f"Le modèle {from_code} -> {to_code} est déjà prêt.")

def translate_docs(source_dir, source_lang="fr", target_lang="en"):
    setup_translator(source_lang, target_lang)
    
    extensions = (".txt", ".md")
    # Suffixe pour identifier les fichiers produits par le script
    suffix = f"_{target_lang}"

    for filename in os.listdir(source_dir):
        # On ne traduit que les fichiers sources originaux (pas ceux qui ont déjà le suffixe)
        name_part, ext_part = os.path.splitext(filename)
        
        if ext_part in extensions and not name_part.endswith(suffix):
            file_path = os.path.join(source_dir, filename)
            
            # 1. Traduire le NOM du fichier (on remplace les underscores par des espaces pour aider Argos)
            clean_name = name_part.replace('_', ' ').replace('-', ' ')
            translated_name = argostranslate.translate.translate(clean_name, source_lang, target_lang)
            
            # On reformate le nom traduit (on remplace les espaces par des underscores pour le système de fichiers)
            final_name = translated_name.replace(' ', '_') + suffix + ext_part
            output_path = os.path.join(source_dir, final_name)

            # 2. Vérifier si cette traduction existe déjà
            if os.path.exists(output_path):
                print(f"Saut : {final_name} existe déjà.")
                continue

            print(f"Traduction : {filename} -> {final_name}")
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 3. Traduire le CONTENU
                translated_text = argostranslate.translate.translate(content, source_lang, target_lang)
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(translated_text)
            except Exception as e:
                print(f"Erreur lors de la traduction de {filename}: {e}")

if __name__ == "__main__":
    DOC_PATH = "Global/Doc"
    if os.path.exists(DOC_PATH):
        translate_docs(DOC_PATH)
    else:
        print(f"Répertoire {DOC_PATH} introuvable.")