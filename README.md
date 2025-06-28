# Steganography-project
A Python GUI project to hide secret messages inside images using LSB

# Steganography – Hiding Information in the Image 🖼️🔐

This project demonstrates how to hide secret messages inside images using the **Least Significant Bit (LSB)** steganography technique.

## 🧠 Project Summary
This Python application allows you to:
- Hide (encode) a secret message into an image.
- Retrieve (decode) the hidden message from the encoded image.
- Simple **GUI-based** interface using **Tkinter**.

---

## 🚀 How to Run the Project

### 🛠️ Requirements
Install Python dependencies by running:

```bash
pip install -r requirements.txt
```

### ▶️ Running the App

```bash
python main.py
```

### 🖼️ Inputs:
- Any **.png image** file
- Secret text (up to a few hundred characters)

### 🧾 Outputs:
- Encoded image saved to disk
- Decoded message displayed in GUI

---

## 📸 Sample Outputs:

### Original Image:
![Original Image](screenshots/original_image.png)

### Encoded Image:
![Encoded Image](screenshots/encoded_image.png)

---

## 📂 Folder Structure:
```
steganography-project/
├── main.py                  # Main app with GUI
├── stegno_utils.py          # Steganography logic
├── README.md                # Project description
├── report.pdf               # Final report
├── presentation.pptx        # PPT slides
├── requirements.txt         # Libraries list
├── screenshots/             # Output screenshots
└── sample_images/           # Test input images
```

## 👤 Author
Name: Sandeep Haldkar
