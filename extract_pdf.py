#!/usr/bin/env python3
"""
Extract PDF content and convert to markdown format
"""

import pdfplumber
import os

pdf_path = "src/ENG_Performance Analysis of Logistic Regression on Encrypted Data Using CKKS Scheme in Microsoft SEAL.pdf"

markdown_content = []

with pdfplumber.open(pdf_path) as pdf:
    total_pages = len(pdf.pages)
    print(f"Total pages: {total_pages}")
    
    for page_num, page in enumerate(pdf.pages, 1):
        print(f"Processing page {page_num}/{total_pages}...")
        
        # Extract text
        text = page.extract_text()
        
        if text:
            markdown_content.append(f"\n---\n## Page {page_num}\n\n")
            markdown_content.append(text)
        
        # Extract tables
        tables = page.extract_tables()
        if tables:
            for table_idx, table in enumerate(tables):
                if table and len(table) > 0:
                    markdown_content.append(f"\n### Table {page_num}.{table_idx + 1}\n\n")
                    
                    # Header
                    header = table[0]
                    markdown_content.append("| " + " | ".join(str(cell if cell else "").strip() for cell in header) + " |\n")
                    markdown_content.append("|" + "|".join(["---"] * len(header)) + "|\n")
                    
                    # Data rows
                    for row in table[1:]:
                        markdown_content.append("| " + " | ".join(str(cell if cell else "").strip() for cell in row) + " |\n")
                    
                    markdown_content.append("\n")

# Save to file
output_path = "PDF_CONTENT.md"
full_content = "".join(markdown_content)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(full_content)

print(f"\nExtraction complete!")
print(f"Output saved to: {output_path}")
print(f"Total content: {len(full_content)} characters")
print(f"File size: {os.path.getsize(output_path) / 1024:.2f} KB")
