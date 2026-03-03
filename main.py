import cv2
import numpy as np
import tkinter as tk
import webbrowser
import re
from pyzbar.pyzbar import decode
from tkinter import filedialog, messagebox
from PIL import ImageGrab

def load_image_from_clipboard():
    # Try to grab image from clipboard
    clipboard_img = ImageGrab.grabclipboard()
    if clipboard_img:
        return cv2.cvtColor(np.array(clipboard_img), cv2.COLOR_RGB2BGR)
    else:
        print("No image in clipboard.")
        return None

def load_image_from_file():
    # Create a hidden Tkinter root window and force it to front
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.attributes("-topmost", True)  # Keep on top of other windows
    root.update()  # Force focus

    # Open file picker
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")],
        title="Select an image file"
    )

    root.destroy()  # Close the hidden root window

    if file_path:
        return cv2.imread(file_path)
    return None

def scan_qr_code(image):
    decoded_objects = decode(image)

    if not decoded_objects:
        print("No QR code found in the image.")
    else:
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            qr_type = obj.type

            # Draw rectangle
            points = obj.polygon
            if len(points) == 4:
                pts = [(pt.x, pt.y) for pt in points]
                cv2.polylines(image, [np.array(pts, dtype=np.int32)], True, (0, 255, 0), 2)

            # Display text
            x, y = obj.rect.left, obj.rect.top
            cv2.putText(image, f'{qr_type}: {qr_data}', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
            print(f"Detected {qr_type}: {qr_data}")

            # Check if it's a URL
            # Auto-open feature
            if re.match(r'https?://', qr_data):
                print("Opening link in browser...")
                webbrowser.open(qr_data)

        # Show image
        cv2.imshow('QR Code Result', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Choose input method:\n1. Clipboard\n2. File Explorer")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        img = load_image_from_clipboard()
    elif choice == '2':
        img = load_image_from_file()
    else:
        print("Invalid choice.")
        img = None

    if img is not None:
        scan_qr_code(img)
    else:
        print("No image to scan.")
