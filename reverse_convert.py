#!/usr/bin/env python3
"""
Script to convert all Word documents in content/ back to markdown files
"""

import pypandoc
import os

def convert_docx_to_md():
    content_dir = 'content'
    if not os.path.exists(content_dir):
        print(f"Directory {content_dir} does not exist.")
        return
    
    for filename in os.listdir(content_dir):
        if filename.endswith('.docx'):
            input_file = os.path.join(content_dir, filename)
            output_file = os.path.join(content_dir, filename.replace('.docx', '.md'))
            try:
                # Convert the docx file to md
                pypandoc.convert_file(input_file, 'md', outputfile=output_file)
                print(f"Successfully converted {input_file} to {output_file}")
            except Exception as e:
                print(f"Error during conversion of {input_file}: {e}")

if __name__ == "__main__":
    convert_docx_to_md()