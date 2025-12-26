import pytesseract
from PIL import Image
import io
import base64
import cv2
import numpy as np

def ocr_image_bytes(image_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(image_bytes))
    return pytesseract.image_to_string(image)

def ocr_image_file(file_path: str) -> str:
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)

def ocr_base64(base64_str: str) -> str:
    image_bytes = base64.b64decode(base64_str)
    return ocr_image_bytes(image_bytes)
