# Handwriting Analysis Tool

This project provides a GUI-based tool for various handwriting analysis tasks including handwriting comparison, handwritten images to text conversion, and a digital evaluation system. The tool is developed in Python and uses libraries such as OpenCV, Tesseract OCR, tkinter, and others.

## Dependencies

Make sure you have Python installed on your system. You can install the required dependencies using `pip`.

```bash
pip install opencv-python pytesseract pillow fpdf pymupdf
```

Additionally, you need to install Tesseract OCR. Follow the instructions for your operating system:

- **Windows**: Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) and run it.
- **macOS**: Use Homebrew to install Tesseract:
  ```bash
  brew install tesseract
  ```
- **Linux**: Use your package manager to install Tesseract. For example, on Ubuntu:
  ```bash
  sudo apt-get install tesseract-ocr
  ```

## Project Structure

- `h_cmp.py`: Handwriting comparison between two images.
- `h_totxt.py`: Convert handwritten images or PDFs to text and save the output.
- `h_des.py`: Digital evaluation system to compare a student's handwritten answer sheet with the answer key.
- `main.py`: Main GUI to integrate all functionalities (described below).

## Running the Project

1. **Handwriting Comparison**

   Run the handwriting comparison tool:

   ```bash
   python h_cmp.py
   ```

   This will open a GUI where you can select two images and compare their handwriting similarity.

2. **Handwritten Images to Text**

   Run the handwritten images to text conversion tool:

   ```bash
   python h_totxt.py
   ```

   This will open a GUI where you can select a handwritten image or PDF and convert it to a text document.

3. **Digital Evaluation System**

   Run the digital evaluation system tool:

   ```bash
   python h_des.py
   ```

   This will open a GUI where you can select an answer key image and a student's answer image to evaluate the correctness.

## References

- **OpenCV**: [OpenCV Documentation](https://docs.opencv.org/)
- **Tesseract OCR**: [Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract)
- **Pillow (PIL Fork)**: [Pillow Documentation](https://pillow.readthedocs.io/)
- **FPDF**: [FPDF Documentation](http://www.fpdf.org/)
- **PyMuPDF**: [PyMuPDF Documentation](https://pymupdf.readthedocs.io/)

