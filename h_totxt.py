import cv2
from PIL import Image
import pytesseract
from fpdf import FPDF
import fitz  # PyMuPDF
from tkinter import Tk, Label, Button, filedialog, messagebox

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Image files", "*.jpg;*.jpeg;*.png")])
    return file_path

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
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

def save_text_to_image(text, output_path, original_image_path):
    try:
        image = cv2.imread(original_image_path)
        text_position = (10, 30)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.7
        font_color = (0, 0, 0)
        line_type = 2

        y0, dy = text_position[1], 20
        for i, line in enumerate(text.split('\n')):
            y = y0 + i * dy
            cv2.putText(image, line, (text_position[0], y), font, font_scale, font_color, line_type)

        cv2.imwrite(output_path, image)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save text to image: {e}")

def process_file():
    file_path = select_file()
    if not file_path:
        return
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
        if text:
            output_path = "./output/output_text.pdf"
            save_text_to_pdf(text, output_path)
    else:
        text = extract_text_from_image(file_path)
        if text:
            output_path = "./output/image_with_text.png"
            save_text_to_image(text, output_path, file_path)

    messagebox.showinfo("Success", f"Output saved to {output_path}")

def main():
    root = Tk()
    root.title("Handwriting to Text")

    select_file_button = Button(root, text="Select File", command=process_file)
    select_file_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
