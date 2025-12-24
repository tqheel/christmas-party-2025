# Copilot Instructions for Christmas Party 2025 Repository

## Project Overview
This repository manages cocktail recipes and menus for a Christmas party. It consists of Markdown files for documentation and Python scripts for converting between Markdown and Microsoft Word formats using pandoc.

## Key Components
- **Markdown Files**: `content/drinks.md` (detailed recipes), `content/menu.md` (guest menu), `content/coquito.md` (special recipe)
- **Conversion Scripts**: `convert_to_word.py` (md to docx), `reverse_convert.py` (docx to md)
- **Environment**: Python virtual environment (`.venv`) with `pypandoc` dependency

## Developer Workflows
- **Setup**: Activate venv with `/path/to/.venv/bin/python`
- **Convert to Word**: Run `python convert_to_word.py` to generate docx files in `content/`
- **Convert Back**: Run `python reverse_convert.py` to update md files in `content/` from docx
- **Dependencies**: Install via `pip install pypandoc`; ensure pandoc is installed system-wide
- **Committing Changes**: Ensure all modified or new files are saved to disk. Update `CHANGELOG.md` with notable changes before committing. It is acceptable to push to the remote repository after committing.

## Project Conventions
- **Markdown Structure**: Use `#` for titles, `##` for sections, `-` for lists (e.g., ingredients in `menu.md`)
- **Recipe Format**: Ingredients under `**Ingredients**`, steps under `**Steps**` in `drinks.md`
- **File Naming**: Consistent naming between md and docx (e.g., `menu.md` ↔ `menu.docx`)
- **Git Ignore**: Excludes `.venv/`, `*.docx`, Python cache; commit only source md files and scripts

## Patterns and Examples
- **Conversion Logic**: Scripts scan `content/` directory for .md or .docx files and convert them using `pypandoc.convert_file()`
- **Error Handling**: Basic try/except in scripts; assume pandoc is available
- **Updates**: When editing recipes, update md in `content/` first, then convert to docx for sharing
- **Reference Files**: See `convert_to_word.py` for dynamic file handling, `content/menu.md` for menu format

## Integration Points
- **External Tools**: Relies on pandoc for format conversion; no APIs or databases
- **Cross-File Communication**: Scripts operate independently on file pairs; no inter-script dependencies