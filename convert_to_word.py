#!/usr/bin/env python3
"""
Script to convert drinks.md and menu.md to Microsoft Word documents
"""

import pypandoc

def convert_md_to_docx(input_file, output_file):
    try:
        # Convert the markdown file to docx
        pypandoc.convert_file(input_file, 'docx', outputfile=output_file)
        print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error during conversion of {input_file}: {e}")

if __name__ == "__main__":
    # Convert both documents
    convert_md_to_docx('drinks.md', 'drinks.docx')
    convert_md_to_docx('menu.md', 'menu.docx')
    convert_md_to_docx('coquito.md', 'coquito.docx')