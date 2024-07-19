import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog, messagebox
from PIL import Image, ImageTk
import pytesseract

def select_file(label):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image = cv2.imread(file_path, 0)
        image = cv2.resize(image, (300, 300))
        img = Image.fromarray(image)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.config(image=imgtk)
        return file_path
    return None

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def compare_answers(answer_key, student_answer):
    key_lines = answer_key.strip().split('\n')
    student_lines = student_answer.strip().split('\n')

    correct_count = sum(1 for key_line, student_line in zip(key_lines, student_lines) if key_line.strip() == student_line.strip())
    total_lines = max(len(key_lines), len(student_lines))

    correctness = (correct_count / total_lines) * 100 if total_lines > 0 else 0
    return correctness

def on_evaluate_button_click(answer_key_path, student_answer_path, result_label):
    if answer_key_path and student_answer_path:
        answer_key_text = extract_text_from_image(answer_key_path)
        student_answer_text = extract_text_from_image(student_answer_path)
        correctness = compare_answers(answer_key_text, student_answer_text)
        result_label.config(text=f'Correctness: {correctness:.2f}%')
    else:
        messagebox.showerror("Error", "Please select both answer key and student answer images")

def main():
    root = Tk()
    root.title("Digital Evaluation System")

    answer_key_label = Label(root, text="Answer Key Image")
    answer_key_label.pack(side="left", padx=10)
    student_answer_label = Label(root, text="Student Answer Image")
    student_answer_label.pack(side="right", padx=10)

    answer_key_path = None
    student_answer_path = None

    def select_answer_key():
        nonlocal answer_key_path
        answer_key_path = select_file(answer_key_label)

    def select_student_answer():
        nonlocal student_answer_path
        student_answer_path = select_file(student_answer_label)

    select_answer_key_button = Button(root, text="Select Answer Key", command=select_answer_key)
    select_answer_key_button.pack(pady=10)

    select_student_answer_button = Button(root, text="Select Student Answer", command=select_student_answer)
    select_student_answer_button.pack(pady=10)

    result_label = Label(root, text="Correctness: ")
    result_label.pack(pady=20)

    evaluate_button = Button(root, text="Evaluate", command=lambda: on_evaluate_button_click(answer_key_path, student_answer_path, result_label))
    evaluate_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
