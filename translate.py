import os
import yaml
import argostranslate.package
import argostranslate.translate

def setup_translator(from_code, to_code):
    installed_packages = argostranslate.package.get_installed_packages()
    if not any(pkg.from_code == from_code and pkg.to_code == to_code for pkg in installed_packages):
        print(f"--- Installation du modèle {from_code} -> {to_code} ---")
        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        pkg = next((p for p in available_packages if p.from_code == from_code and p.to_code == to_code), None)
        if pkg: 
            argostranslate.package.install_from_path(pkg.download())
            print(f"Modèle {to_code} prêt.")

def translate_all_from_mapping(source_dir, mapping_file, source_lang="fr"):
    if not os.path.exists(mapping_file):
        print(f"Erreur : {mapping_file} introuvable.")
        return

    with open(mapping_file, 'r', encoding='utf-8') as f:
        mapping = yaml.safe_load(f)

    if not mapping:
        print("Le fichier de mapping est vide.")
        return

    for filename in os.listdir(source_dir):
        name_part, ext_part = os.path.splitext(filename)
        
        # On vérifie si le fichier actuel possède des traductions définies
        if name_part in mapping:
            source_path = os.path.join(source_dir, filename)
            translations = mapping[name_part] # C'est un dict, ex: {'en': 'Hello', 'es': 'Hola'}

            for target_lang, translated_name in translations.items():
                # Configuration automatique de la langue
                setup_translator(source_lang, target_lang)

                output_filename = f"{translated_name}{ext_part}"
                output_path = os.path.join(source_dir, output_filename)

                # Vérification de la nécessité de traduire (existence ou date)
                should_translate = False
                if not os.path.exists(output_path):
                    should_translate = True
                elif os.path.getmtime(source_path) > os.path.getmtime(output_path):
                    print(f"Mise à jour détectée pour {filename} ({target_lang})")
                    should_translate = True

                if should_translate:
                    print(f"Traduction [{target_lang}] : '{filename}' -> '{output_filename}'")
                    try:
                        with open(source_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        translated_text = argostranslate.translate.translate(content, source_lang, target_lang)
                        
                        with open(output_path, 'w', encoding='utf-8') as f:
                            f.write(translated_text)
                    except Exception as e:
                        print(f"Erreur lors de la traduction en {target_lang}: {e}")
                else:
                    # Optionnel: décommenter pour voir les fichiers ignorés
                    # print(f"Saut : {output_filename} est à jour.")
                    pass

if __name__ == "__main__":
    translate_all_from_mapping("Global/Doc", "mapping_file_names.yaml")