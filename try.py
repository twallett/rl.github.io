#%%
import subprocess
import os

def convert_pdf_to_svg(pdf_path, svg_path):
    """Converts a PDF file to an SVG file using pdf2svg."""
    try:
        subprocess.run(['pdf2svg', pdf_path, svg_path], check=True)
        print(f"Successfully converted '{pdf_path}' to '{svg_path}'")
    except subprocess.CalledProcessError as e:
        print(f"Error converting '{pdf_path}': {e}")
    except FileNotFoundError:
        print("Error: pdf2svg command not found. Is it installed?")

def batch_convert_pdfs(pdf_folder, svg_folder):
    """Converts all PDFs in a folder to SVGs."""
    if not os.path.exists(svg_folder):
        os.makedirs(svg_folder)  # Create the output folder if it doesn't exist
    
    for filename in os.listdir(pdf_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            svg_path = os.path.join(svg_folder, filename.replace(".pdf", ".svg"))
            convert_pdf_to_svg(pdf_path, svg_path)

if __name__ == '__main__':
    pdf_folder = "pdf"  # Folder containing PDF files
    svg_folder = "svg"  # Output folder for SVG files
    batch_convert_pdfs(pdf_folder, svg_folder)

# %%
