import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

def main():
    root = tk.Tk()
    root.title("Handwriting Analysis Tool")

    # Set window size and center it
    window_width = 600
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height/2 - window_height/2)
    position_right = int(screen_width/2 - window_width/2)
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    # Set background image
    global background_image, background_photo, background_label
    background_image = Image.open("background.jpeg")  # Add path to your background image
    background_photo = ImageTk.PhotoImage(background_image.resize((window_width, window_height)))
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Bind the configure event to resize the background image
    root.bind('<Configure>', resize_background)

    # Configure style
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', font=('Helvetica', 12, 'bold'), padding=10, background='#4CAF50', foreground='white')
    style.map('TButton', background=[('active', '#45a049')])

    # Create a frame for better layout management
    frame = ttk.Frame(root, padding=20, relief='raised', style='TFrame')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Add a label for the title
    title_label = ttk.Label(frame, text="Handwriting Analysis Tool", font=('Helvetica', 16, 'bold'), background='white')
    title_label.pack(pady=10)

    # Add buttons
    ttk.Button(frame, text="Handwriting Comparison", command=handwriting_comparison).pack(pady=10)
    ttk.Button(frame, text="Handwritten Images to Text", command=handwritten_to_text).pack(pady=10)
    # ttk.Button(frame, text="Digital Evaluation System", command=digital_evaluation).pack(pady=10)
    
    root.mainloop()

def resize_background(event):
    global background_photo, background_label
    new_width = event.width
    new_height = event.height
    resized_image = background_image.resize((new_width, new_height), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(resized_image)
    background_label.config(image=background_photo)
    background_label.image = background_photo

def handwriting_comparison():
    subprocess.run(["python", "h_cmp.py"])

def handwritten_to_text():
    subprocess.run(["python", "h_totxt.py"])

# def digital_evaluation():
#     subprocess.run(["python", "h_des.py"])

if __name__ == "__main__":
    main()
