import os
import yaml # Pensez à faire 'pip install pyyaml' dans votre venv
import argostranslate.package
import argostranslate.translate

def setup_translator(from_code, to_code):
    installed_packages = argostranslate.package.get_installed_packages()
    if not any(pkg.from_code == from_code and pkg.to_code == to_code for pkg in installed_packages):
        print(f"Installation du modèle {from_code} -> {to_code}...")
        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        pkg = next((p for p in available_packages if p.from_code == from_code and p.to_code == to_code), None)
        if pkg: argostranslate.package.install_from_path(pkg.download())

def translate_with_mapping(source_dir, mapping_file, source_lang="fr", target_langs=["en"]):
    # Charger le mapping
    with open(mapping_file, 'r', encoding='utf-8') as f:
        mapping = yaml.safe_load(f)

    for target_lang in target_langs:
        setup_translator(source_lang, target_lang)
        
        for filename in os.listdir(source_dir):
            name_part, ext_part = os.path.splitext(filename)
            
            # On ne traite que les fichiers qui sont dans notre dictionnaire
            if name_part in mapping:
                # Récupérer le nom cible défini dans le mapping
                translated_name = mapping[name_part].get(target_lang)
                
                if not translated_name:
                    print(f"Pas de nom défini pour {name_part} en {target_lang}, on ignore.")
                    continue

                output_filename = f"{translated_name}{ext_part}"
                output_path = os.path.join(source_dir, output_filename)
                source_path = os.path.join(source_dir, filename)

                if os.path.exists(output_path):
                    continue

                print(f"Traduction [{target_lang}] : {filename} -> {output_filename}")
                
                try:
                    with open(source_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    translated_text = argostranslate.translate.translate(content, source_lang, target_lang)
                    
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(translated_text)
                except Exception as e:
                    print(f"Erreur sur {filename}: {e}")

if __name__ == "__main__":
    # Configuration
    DOC_PATH = "Global/Doc"
    MAPPING_FILE = "mapping_file_names.yaml"
    LANGUES_CIBLES = ["en"] # Ajoutez "es", "de", etc., si besoin

    if os.path.exists(DOC_PATH) and os.path.exists(MAPPING_FILE):
        translate_with_mapping(DOC_PATH, MAPPING_FILE, target_langs=LANGUES_CIBLES)