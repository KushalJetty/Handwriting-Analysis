import tkinter as tk
import subprocess

def main():
    root = tk.Tk()
    root.title("Handwriting Analysis Tool")

    tk.Button(root, text="Handwriting Comparison", command=handwriting_comparison).pack(pady=10)
    tk.Button(root, text="Handwritten Images to Text", command=handwritten_to_text).pack(pady=10)
    tk.Button(root, text="Digital Evaluation System", command=digital_evaluation).pack(pady=10)

    root.mainloop()

def handwriting_comparison():
    subprocess.run(["python", "h_cmp.py"])

def handwritten_to_text():
    subprocess.run(["python", "h_totxt.py"])

def digital_evaluation():
    subprocess.run(["python", "h_des.py"])

if __name__ == "__main__":
    main()
