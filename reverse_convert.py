#!/usr/bin/env python3
"""
Script to convert drinks.docx and menu.docx back to markdown files
"""

import pypandoc

def convert_docx_to_md(input_file, output_file):
    try:
        # Convert the docx file to md
        pypandoc.convert_file(input_file, 'md', outputfile=output_file)
        print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error during conversion of {input_file}: {e}")

if __name__ == "__main__":
    # Convert both documents back to markdown
    convert_docx_to_md('drinks.docx', 'drinks.md')
    convert_docx_to_md('menu.docx', 'menu.md')
    convert_docx_to_md('coquito.docx', 'coquito.md')