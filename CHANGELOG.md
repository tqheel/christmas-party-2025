# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Fun admission in README about repo overengineering

### Changed

- Updated `.github/copilot-instructions.md` with committing workflow guidelines
- Moved markdown files to `content/` directory
- Modified conversion scripts to dynamically scan `content/` for files instead of hardcoding filenames

## [1.0.0] - 2025-12-24

### Added

- Initial cocktail menu and recipes (`drinks.md`, `menu.md`, `coquito.md`)
- Python scripts for converting between Markdown and Microsoft Word documents (`convert_to_word.py`, `reverse_convert.py`)
- `.gitignore` file for Python projects and Word documents
- Comprehensive README with usage instructions and credits
- Public GitHub repository setup

### Changed

- Updated Manhattan recipe to use 86 proof Old Forester bourbon instead of rye whiskey
- Changed bitters in Old Fashioned and Manhattan to Remedy Noir Bitters
- Updated Espresso Martini bitters to Crude Big Bear Coffee and Cocoa Bitters
- Corrected Vanilla-Kahlúa Martini to classic Vodka Martini
- Changed vodka in Chocolate Martini to Vanilla Vodka

### Fixed

- Typo in bourbon proof ("B6" to "86")