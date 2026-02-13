import os
import yaml
import argostranslate.package
import argostranslate.translate

def get_or_install_pkg(from_code, to_code):
    installed = argostranslate.package.get_installed_packages()
    pkg = next((p for p in installed if p.from_code == from_code and p.to_code == to_code), None)
    
    if not pkg:
        print(f"--- Installation du paquet {from_code} -> {to_code} ---")
        argostranslate.package.update_package_index()
        available = argostranslate.package.get_available_packages()
        pkg_to_install = next((p for p in available if p.from_code == from_code and p.to_code == to_code), None)
        if pkg_to_install:
            argostranslate.package.install_from_path(pkg_to_install.download())
        else:
            print(f"Attention : Impossible de trouver le paquet {from_code} -> {to_code}")
            return False
    return True

def translate_content(text, from_code, to_code):
    # Si la langue cible est l'anglais, traduction directe
    if to_code == 'en':
        if get_or_install_pkg(from_code, 'en'):
            return argostranslate.translate.translate(text, from_code, 'en')
    else:
        # Sinon, passage par le pivot anglais
        if get_or_install_pkg(from_code, 'en') and get_or_install_pkg('en', to_code):
            # Etape 1: Fr -> En
            intermediate = argostranslate.translate.translate(text, from_code, 'en')
            # Etape 2: En -> Cible (es, de, etc.)
            return argostranslate.translate.translate(intermediate, 'en', to_code)
    return None

def translate_all_from_mapping(source_dir, mapping_file, source_lang="fr"):
    if not os.path.exists(mapping_file): return
    with open(mapping_file, 'r', encoding='utf-8') as f:
        mapping = yaml.safe_load(f)

    for filename in os.listdir(source_dir):
        name_part, ext_part = os.path.splitext(filename)
        if name_part in mapping:
            source_path = os.path.join(source_dir, filename)
            for target_lang, translated_name in mapping[name_part].items():
                output_path = os.path.join(source_dir, f"{translated_name}{ext_part}")

                # Traduire seulement si nécessaire
                if not os.path.exists(output_path) or os.path.getmtime(source_path) > os.path.getmtime(output_path):
                    print(f"Traduction [{target_lang}] : {filename}")
                    with open(source_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    result = translate_content(content, source_lang, target_lang)
                    if result:
                        with open(output_path, 'w', encoding='utf-8') as f:
                            f.write(result)

if __name__ == "__main__":
    translate_all_from_mapping("Global/Doc", "mapping_file_names.yaml")