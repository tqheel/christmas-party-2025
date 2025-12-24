#!/usr/bin/env python3
"""
Script to convert all Markdown files in content/ to Microsoft Word documents
"""

import pypandoc
import os

def convert_md_to_docx():
    content_dir = 'content'
    if not os.path.exists(content_dir):
        print(f"Directory {content_dir} does not exist.")
        return
    
    for filename in os.listdir(content_dir):
        if filename.endswith('.md'):
            input_file = os.path.join(content_dir, filename)
            output_file = os.path.join(content_dir, filename.replace('.md', '.docx'))
            try:
                # Convert the markdown file to docx
                pypandoc.convert_file(input_file, 'docx', outputfile=output_file)
                print(f"Successfully converted {input_file} to {output_file}")
            except Exception as e:
                print(f"Error during conversion of {input_file}: {e}")

if __name__ == "__main__":
    convert_md_to_docx()