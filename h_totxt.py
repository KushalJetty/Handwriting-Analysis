import cv2
from PIL import Image
import pytesseract
from fpdf import FPDF
import fitz  # PyMuPDF
from tkinter import Tk, Label, Button, filedialog, messagebox

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    return file_path

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    dilated = cv2.dilate(thresh, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)
    return eroded

def extract_text_from_image(image_path):
    try:
        preprocessed_image = preprocess_image(image_path)
        text = pytesseract.image_to_string(preprocessed_image)
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text from image: {e}")
        return None

def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            page_text = pytesseract.image_to_string(image)
            text += f"Page {page_num + 1}:\n{page_text}\n\n"
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text from PDF: {e}")
        return None

def save_text_to_txt(text, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save text to file: {e}")

def save_text_to_pdf(text, output_path):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)
        pdf.output(output_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save text to PDF: {e}")

def process_pdf():
    file_path = select_pdf()
    if not file_path:
        return
    text = extract_text_from_pdf(file_path)
    if text:
        output_path = "output_text.pdf"
        save_text_to_pdf(text, output_path)
        messagebox.showinfo("Success", f"Text extracted from PDF and saved to {output_path}")

def process_image():
    file_path = select_image()
    if not file_path:
        return
    text = extract_text_from_image(file_path)
    if text:
        output_path = "output_text.txt"
        save_text_to_txt(text, output_path)
        messagebox.showinfo("Success", f"Text extracted from image and saved to {output_path}")

def main():
    root = Tk()
    root.title("Handwriting to Text")

    select_pdf_button = Button(root, text="Select PDF", command=process_pdf)
    select_pdf_button.pack(pady=20)

    select_image_button = Button(root, text="Select Image", command=process_image)
    select_image_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
