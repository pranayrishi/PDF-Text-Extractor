import fitz  # PyMuPDF
import pytesseract
from PIL import Image

# Step 1: Configure Tesseract Path (Uncomment and set the path if on Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using Tesseract."""
    extracted_text = ""
    try:
        # Open the PDF file
        document = fitz.open(pdf_path)
        
        for page_num in range(len(document)):
            page = document.load_page(page_num)  # Load a page
            pix = page.get_pixmap()  # Render the page to a pixel map
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)  # Convert to PIL Image
            
            # Use Tesseract to extract text from the image
            text = pytesseract.image_to_string(img)
            extracted_text += text + "\n"  # Append the extracted text
            
        document.close()  # Close the PDF document
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    return extracted_text

def save_text_to_file(text, filename='extracted_text.txt'):
    """Save extracted text to a file."""
    try:
        with open(filename, 'w') as text_file:
            text_file.write(text)
        print(f"Extracted text saved as {filename}.")
    except Exception as e:
        print(f"Error saving text to file: {e}")

def main():
    pdf_path = 'mathnotes.pdf'  # The pre-existing PDF document in the directory

    # Extract text from the provided PDF
    extracted_text = extract_text_from_pdf(pdf_path)

    # Print the extracted text
    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)

        # Save the extracted text to a file
        save_text_to_file(extracted_text)

if __name__ == "__main__":
    main()
