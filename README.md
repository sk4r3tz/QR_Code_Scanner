# QR Code Scanner (Python)

A simple Python QR code scanner that reads QR codes from:

# Image file (via File Explorer)

# Clipboard image (copied screenshot or image)

If the QR code contains a URL, it can automatically open it in your default web browser.

# Features

Scan QR code from image file

Scan QR code from clipboard

Draw bounding box around detected QR

Display decoded text

Automatically open links in browser (if QR contains URL)

Simple and lightweight

# Requirements

Python 3.8+

Install dependencies:

pip install opencv-python pyzbar pillow

# How to Run
python main.py


Then choose:

1 → Load from Clipboard  
2 → Select Image File

# How It Works

OpenCV → Loads and processes images

pyzbar → Decodes QR codes

Pillow → Access clipboard images

webbrowser → Opens URL automatically

# Example Use Cases

Scan QR code from screenshots

Extract URLs quickly

Verify QR code content

Lightweight desktop utility

# License

MIT License
