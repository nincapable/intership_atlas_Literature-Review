import os
import argostranslate.package
import argostranslate.translate

def setup_translator(from_code, to_code):
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    
    # Vérifie si déjà installé
    installed_packages = argostranslate.package.get_installed_packages()
    is_installed = any(pkg.from_code == from_code and pkg.to_code == to_code for pkg in installed_packages)
    
    if not is_installed:
        print(f"Installation du modèle {from_code} -> {to_code}...")
        package_to_install = next(
            filter(lambda x: x.from_code == from_code and x.to_code == to_code, available_packages)
        )
        argostranslate.package.install_from_path(package_to_install.download())
    else:
        print(f"Le modèle {from_code} -> {to_code} est déjà en cache.")

def translate_docs(source_dir, source_lang="fr", target_lang="en"):
    setup_translator(source_lang, target_lang)
    
    extensions = (".txt", ".md")
    suffix = f"_{target_lang}"

    for filename in os.listdir(source_dir):
        # Ignore les fichiers déjà traduits et les dossiers
        if filename.endswith(extensions) and not filename.endswith(f"{suffix}{os.path.splitext(filename)[1]}"):
            file_path = os.path.join(source_dir, filename)
            
            name_part, ext_part = os.path.splitext(filename)
            output_filename = f"{name_part}{suffix}{ext_part}"
            output_path = os.path.join(source_dir, output_filename)

            # Optionnel : Ne pas retraduire si le fichier traduit existe déjà (gain de temps)
            if os.path.exists(output_path):
                continue

            print(f"Traduction de : {filename}...")
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            translated_text = argostranslate.translate.translate(content, source_lang, target_lang)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(translated_text)

if __name__ == "__main__":
    translate_docs("Global/Doc")