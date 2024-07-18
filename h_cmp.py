import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk
import pytesseract

# Set the Tesseract command to the full path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def select_image(label):
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path, 0)
        image = cv2.resize(image, (300, 300))
        img = Image.fromarray(image)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.config(image=imgtk)
        label.image = image  # Store the actual image in the label
        return image
    return None

def contains_handwriting(image):
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config)
    return len(text.strip()) > 0

def compare_handwriting(img1, img2):
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    similarity = len(matches) / max(len(des1), len(des2)) * 100
    return similarity

def show_comparison_result(similarity, result_label):
    result_label.config(text=f'Similarity: {similarity:.2f}%')

def on_compare_button_click(img1_label, img2_label, result_label):
    img1 = img1_label.image
    img2 = img2_label.image

    if img1 is not None and img2 is not None:
        if contains_handwriting(img1) and contains_handwriting(img2):
            similarity = compare_handwriting(img1, img2)
            show_comparison_result(similarity, result_label)
        else:
            result_label.config(text='No handwritten text found in one or both images.')
    else:
        result_label.config(text='Please select both images.')

def main():
    root = Tk()
    root.title("Handwriting Comparison")

    img1_label = Label(root)
    img1_label.pack(side="left", padx=10)

    img2_label = Label(root)
    img2_label.pack(side="right", padx=10)

    select_img1_button = Button(root, text="Select Image 1", command=lambda: select_image(img1_label))
    select_img1_button.pack(pady=10)

    select_img2_button = Button(root, text="Select Image 2", command=lambda: select_image(img2_label))
    select_img2_button.pack(pady=10)

    result_label = Label(root, text="Similarity: ")
    result_label.pack(pady=20)

    compare_button = Button(root, text="Compare", command=lambda: on_compare_button_click(img1_label, img2_label, result_label))
    compare_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
