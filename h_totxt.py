import cv2
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from tkinter import Tk, Button, filedialog, messagebox

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    return file_path

def preprocess_image(image_path):
    # Load image using PIL
    image = Image.open(image_path)
    
    # Convert to grayscale
    gray = np.array(image.convert('L'))

    # Enhance the image quality
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(2)
    enhancer = ImageEnhance.Sharpness(enhanced_image)
    enhanced_image = enhancer.enhance(2)
    enhanced_image = np.array(enhanced_image.convert('L'))

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(enhanced_image, (5, 5), 0)

    # Apply thresholding
    _, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binary_image

def extract_text_from_image(image_path):
    preprocessed_image = preprocess_image(image_path)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(preprocessed_image, config=custom_config)
    return text

def save_text_to_txt(text, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save text to file: {e}")

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

    select_image_button = Button(root, text="Select Image", command=process_image)
    select_image_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
