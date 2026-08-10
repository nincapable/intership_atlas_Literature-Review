#!/usr/bin/env python3
"""Translate the internship report while preserving LaTeX structure and code."""

from __future__ import annotations

import re
from pathlib import Path

import argostranslate.translate


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "Report" / "Report_tex_pdf" / "Report_writing_version.tex"
TARGET = ROOT / "Report" / "Report_tex_pdf" / "Report_writing_version.en.tex"

PROTECTED_ENVIRONMENTS = {"lstlisting", "tikzpicture"}
FULL_TOKEN_PATTERNS = [
    re.compile(r"\\(?:begin|end)\{[^{}]+\}"),
    re.compile(r"\\(?:texttt|label|ref|pageref|url|href)\{[^{}]*\}"),
    re.compile(r"\$[^$]*\$"),
    re.compile(r"https?://[^\s}]+"),
]
COMMAND_PATTERN = re.compile(r"\\[A-Za-z@]+\*?|\\\\(?:\[[^]]*\])?")


def protect(text: str) -> tuple[str, list[str]]:
    tokens: list[str] = []

    def stash(match: re.Match[str]) -> str:
        token = f"ZXQTOKEN{len(tokens):04d}ZXQ"
        tokens.append(match.group(0))
        return token

    for pattern in FULL_TOKEN_PATTERNS:
        text = pattern.sub(stash, text)
    text = COMMAND_PATTERN.sub(stash, text)
    return text, tokens


def restore(text: str, tokens: list[str]) -> str:
    for index, value in enumerate(tokens):
        token = f"ZXQTOKEN{index:04d}ZXQ"
        text = text.replace(token, value)
        text = text.replace(token.lower(), value)

    # Neural translation may insert one zero into an identifier or drop the
    # middle X in the ZXQ suffix. Recover these harmless variations.
    fuzzy = re.compile(r"ZXQTOKEN0*(\d{1,4})Z(?:X)?Q", re.IGNORECASE)

    def recover(match: re.Match[str]) -> str:
        index = int(match.group(1))
        if index >= len(tokens):
            raise ValueError(f"Invalid placeholder index {index} in: {text}")
        return tokens[index]

    text = fuzzy.sub(recover, text)
    if "ZXQTOKEN" in text.upper():
        raise ValueError(f"Unrestored placeholder in: {text}")
    return text


def translate_fragment(text: str) -> str:
    if not re.search(r"[A-Za-zÀ-ÿ]", text):
        return text
    protected, tokens = protect(text)
    translated = argostranslate.translate.translate(protected, "fr", "en")
    return restore(translated, tokens)


def translate_listing_declaration(line: str) -> str:
    caption = re.search(r"caption=\{([^{}]*)\}", line)
    if not caption:
        return line
    translated = translate_fragment(caption.group(1))
    return line[: caption.start(1)] + translated + line[caption.end(1) :]


def main() -> None:
    lines = SOURCE.read_text(encoding="utf-8").splitlines(keepends=True)
    output: list[str] = []
    in_document = False
    protected_environment: str | None = None

    for line in lines:
        stripped = line.strip()
        if stripped == r"\begin{document}":
            in_document = True
            output.append(line)
            continue
        if not in_document:
            output.append(line)
            continue

        if protected_environment:
            output.append(line)
            if stripped.startswith(rf"\end{{{protected_environment}}}"):
                protected_environment = None
            continue

        match = re.match(r"\s*\\begin\{([^{}]+)\}", line)
        if match and match.group(1) in PROTECTED_ENVIRONMENTS:
            environment = match.group(1)
            if environment == "lstlisting":
                output.append(translate_listing_declaration(line))
            else:
                output.append(line)
            protected_environment = environment
            continue

        if not stripped or stripped.startswith("%"):
            output.append(line)
            continue

        newline = "\n" if line.endswith("\n") else ""
        content = line[:-1] if newline else line
        output.append(translate_fragment(content) + newline)

    TARGET.write_text("".join(output), encoding="utf-8")
    print(TARGET)


if __name__ == "__main__":
    main()
