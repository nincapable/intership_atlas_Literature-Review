#!/usr/bin/env python3
"""Translate documents declared in mapping.yaml with Argos Translate."""

from __future__ import annotations

import argparse
from pathlib import Path

import argostranslate.package
import argostranslate.translate
import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_MAPPING = SCRIPT_DIR / "mapping.yaml"
DEFAULT_DOCUMENTS_DIR = SCRIPT_DIR.parent / "literature_review"


def ensure_package(source_language: str, target_language: str) -> bool:
    installed = argostranslate.package.get_installed_packages()
    if any(
        package.from_code == source_language and package.to_code == target_language
        for package in installed
    ):
        return True

    print(f"Installation du modèle {source_language} -> {target_language}")
    argostranslate.package.update_package_index()
    package = next(
        (
            candidate
            for candidate in argostranslate.package.get_available_packages()
            if candidate.from_code == source_language
            and candidate.to_code == target_language
        ),
        None,
    )
    if package is None:
        print(f"Modèle indisponible : {source_language} -> {target_language}")
        return False
    argostranslate.package.install_from_path(package.download())
    return True


def translate_text(text: str, source_language: str, target_language: str) -> str | None:
    if target_language == "en":
        if ensure_package(source_language, "en"):
            return argostranslate.translate.translate(text, source_language, "en")
        return None

    if not ensure_package(source_language, "en") or not ensure_package("en", target_language):
        return None
    english_text = argostranslate.translate.translate(text, source_language, "en")
    return argostranslate.translate.translate(english_text, "en", target_language)


def load_mapping(mapping_path: Path) -> dict:
    with mapping_path.open(encoding="utf-8") as handle:
        config = yaml.safe_load(handle) or {}
    if "documents" not in config:
        raise ValueError("La configuration doit contenir une section 'documents'.")
    return config


def translate_documents(documents_dir: Path, mapping_path: Path, force: bool = False) -> None:
    config = load_mapping(mapping_path)
    source_language = config.get("source_language", "fr")

    for document in config["documents"]:
        source_path = documents_dir / document["source"]
        if not source_path.is_file():
            raise FileNotFoundError(f"Document source introuvable : {source_path}")

        source_text = source_path.read_text(encoding="utf-8")
        for target_language, output_name in document["translations"].items():
            output_path = documents_dir / output_name
            is_outdated = (
                not output_path.exists()
                or source_path.stat().st_mtime > output_path.stat().st_mtime
            )
            if not force and not is_outdated:
                print(f"À jour [{target_language}] : {output_path.name}")
                continue

            print(f"Traduction [{source_language} -> {target_language}] : {source_path.name}")
            result = translate_text(source_text, source_language, target_language)
            if result is not None:
                output_path.write_text(result, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Traduit les documents déclarés dans un fichier YAML.")
    parser.add_argument("--mapping", type=Path, default=DEFAULT_MAPPING)
    parser.add_argument("--documents-dir", type=Path, default=DEFAULT_DOCUMENTS_DIR)
    parser.add_argument("--force", action="store_true", help="Regénérer les traductions existantes")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    translate_documents(args.documents_dir, args.mapping, args.force)


if __name__ == "__main__":
    main()
