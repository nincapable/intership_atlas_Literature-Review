import os
import argostranslate.package
import argostranslate.translate

def setup_translator(from_code, to_code):
    print(f"--- Configuration du traducteur : {from_code} -> {to_code} ---")
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    
    # On cherche le paquet correspondant
    package_to_install = next(
        (pkg for pkg in available_packages if pkg.from_code == from_code and pkg.to_code == to_code), 
        None
    )
    
    if package_to_install:
        argostranslate.package.install_from_path(package_to_install.download())
        print("Modèle installé avec succès.")
    else:
        raise Exception(f"Modèle de traduction {from_code}->{to_code} introuvable.")

def translate_docs(source_dir, source_lang="fr", target_lang="en"):
    # Initialisation
    setup_translator(source_lang, target_lang)
    
    # Extensions supportées
    extensions = (".txt", ".md")
    suffix = f"_{target_lang}"

    for filename in os.listdir(source_dir):
        # On ne traite que les fichiers sources (ex: doc.md) 
        # et on ignore les fichiers déjà traduits (ex: doc_en.md)
        if filename.endswith(extensions) and suffix not in filename:
            file_path = os.path.join(source_dir, filename)
            
            # Construction du nom de sortie : doc.md -> doc_en.md
            name_part, ext_part = os.path.splitext(filename)
            output_filename = f"{name_part}{suffix}{ext_part}"
            output_path = os.path.join(source_dir, output_filename)

            print(f"Traduction de : {filename} ...")
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Traduction via Argos
                translated_text = argostranslate.translate.translate(content, source_lang, target_lang)
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(translated_text)
                
                print(f"✓ Terminé : {output_filename}")
            
            except Exception as e:
                print(f"X Erreur sur {filename} : {e}")

if __name__ == "__main__":
    # Chemin vers votre dossier spécifique
    DOC_PATH = "Global/Doc"
    
    if os.path.exists(DOC_PATH):
        translate_docs(DOC_PATH, source_lang="fr", target_lang="en")
    else:
        print(f"Erreur : Le répertoire {DOC_PATH} est introuvable.")   