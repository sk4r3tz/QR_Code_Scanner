# QR Code Scanner (Clipboard & File Support)

A simple Python-based QR Code scanner that detects and decodes QR codes from either the clipboard or an image file. If a detected QR code contains a URL, it automatically opens it in the default web browser.

---

## Features

- Scan QR codes from:
  - Clipboard images (e.g., screenshots)
  - Local image files (PNG, JPG, JPEG, BMP)
- Draw bounding box around detected QR codes
- Display decoded content directly on the image
- Automatically open detected URLs in the default browser
- Simple CLI-based input selection
- Lightweight and easy to use

---

## Tech Stack

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Tkinter (File Dialog)
- Pyzbar (QR Code decoding)
- Pillow (ImageGrab for clipboard support)
- Webbrowser (Auto-open URLs)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/qr-code-scanner.git
cd qr-code-scanner
```

### 2. (Optional) Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install opencv-python numpy pyzbar pillow
```

---

## Important Dependency (Windows Users)

`pyzbar` requires **ZBar** to function.

If you encounter errors, install ZBar:

- Download ZBar for Windows
- Add it to your system PATH if required

On macOS:

```bash
brew install zbar
```

On Linux:

```bash
sudo apt-get install libzbar0
```

---

## Usage

Run the script:

```bash
python main.py
```

You will see:

```
Choose input method:
1. Clipboard
2. File Explorer
Enter 1 or 2:
```

### Option 1 – Clipboard
- Copy an image (e.g., screenshot of a QR code)
- Select option `1`
- The program scans directly from clipboard

### Option 2 – File Explorer
- Select option `2`
- Choose an image file from your system
- The program scans the selected file

---

## How It Works

1. User selects input source (clipboard or file).
2. Image is loaded into memory using OpenCV.
3. `pyzbar.decode()` scans for QR codes.
4. If detected:
   - Bounding box is drawn
   - Decoded text is displayed
   - URL links are automatically opened
5. The result image is displayed in a window.

---

## Project Structure

```
qr-code-scanner/
│
├── main.py          # Main QR scanner script
├── README.md        # Project documentation
└── venv/            # Virtual environment (optional)
```

---

## Example Output (Console)

```
Choose input method:
1. Clipboard
2. File Explorer
Enter 1 or 2: 2

Detected QRCODE: https://example.com
Opening link in browser...
```

---

## Example Output (Image Window)

- Green bounding box around detected QR code
- Decoded text displayed above the code
- Browser automatically opens if content is a valid URL

---

## Error Handling

- Invalid input choice
- No image in clipboard
- No QR code detected
- File selection canceled

All cases are handled gracefully with console messages.

---

## Future Improvements

- Real-time webcam QR scanning
- GUI-based full interface (Tkinter or PyQt)
- Multiple QR detection summary panel
- Export scan results to file (CSV or TXT)
- QR code generation feature
- Drag-and-drop image support

---

## Security Consideration

This application automatically opens detected URLs.  
Be cautious when scanning QR codes from unknown sources.

---

# LICENSE (MIT)

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
