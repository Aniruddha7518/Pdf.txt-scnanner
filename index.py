import os
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import fitz

#tesseract path jo ki system me install karna padega 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error reading image: {e}"

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            page_text = page.get_text()
            text += page_text

        #agarnormaltexna ho to apply OCR
        if len(text.strip()) < 10:
            print("Normal text not found, using OCR...")
            images = convert_from_path(pdf_path)
            for img in images:
                text += pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

def both_text_extractor(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext in ['.jpg', '.jpeg', '.png']:
        print("Detected Image File")
        return extract_text_from_image(file_path)
    
    elif ext == '.pdf':
        print("Detected PDF File")
        return extract_text_from_pdf(file_path)
    
    else:
        return "Unsupported file format"

file_path = r"C:\Users\iPC\Downloads\WhatsApp Image 2025-04-11 at 13.06.08_e8b39d2b.jpg"
extracted_text = both_text_extractor(file_path)
print("\n Extracted Text:\n")
print(extracted_text)
