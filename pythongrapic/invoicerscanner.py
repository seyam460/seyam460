import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
import cv2
import numpy as np
import re
import json

def preprocess_image(image_path):
    img = cv2.imread(image_path)

    # Grayscale করো
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    denoised = cv2.fastNlMeansDenoising(gray, h=10)

   
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(denoised)

    _, thresh = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresh


def extract_text(image_path):
    processed = preprocess_image(image_path)

    # PIL Image এ convert করো
    pil_image = Image.fromarray(processed)

    # OCR চালাও
    text = pytesseract.image_to_string(pil_image, lang='eng')
    return text


# =============================================
# ধাপ ৩: Text থেকে Data Parse করো
# =============================================
def parse_receipt(text):
    data = {}

    lines = text.strip().split('\n')
    lines = [line.strip() for line in lines if line.strip()]

    # --- দোকানের নাম (প্রথম line) ---
    data['shop_name'] = lines[0] if lines else "Unknown"

    # --- তারিখ খোঁজো ---
    date_pattern = r'(\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4})'
    date_match = re.search(date_pattern, text)
    data['date'] = date_match.group(1) if date_match else "Not Found"

    # --- Total Amount খোঁজো ---
    total_pattern = r'(?:total|amount|grand total|subtotal)[^\d]*(\d+[\.,]\d{2})'
    total_match = re.search(total_pattern, text, re.IGNORECASE)
    data['total'] = total_match.group(1) if total_match else "Not Found"

    # --- Items খোঁজো (নাম + দাম) ---
    item_pattern = r'(.+?)\s+(\d+[\.,]\d{2})'
    items = []
    for line in lines:
        match = re.match(item_pattern, line)
        if match:
            item_name = match.group(1).strip()
            item_price = match.group(2).strip()

            # Total/Tax line বাদ দাও
            skip_words = ['total', 'tax', 'vat', 'discount', 'subtotal', 'cash', 'change']
            if not any(word in item_name.lower() for word in skip_words):
                items.append({
                    'item': item_name,
                    'price': item_price
                })

    data['items'] = items

    # --- Tax/VAT খোঁজো ---
    tax_pattern = r'(?:tax|vat)[^\d]*(\d+[\.,]\d{2})'
    tax_match = re.search(tax_pattern, text, re.IGNORECASE)
    data['tax'] = tax_match.group(1) if tax_match else "Not Found"

    return data


# =============================================
# ধাপ ৪: Main Function
# =============================================
def scan_receipt(image_path):
    print("📄 Receipt Scanning শুরু হচ্ছে...\n")

    # Text বের করো
    raw_text = extract_text(image_path)

    print("🔤 Raw Text:")
    print("-" * 40)
    print(raw_text)
    print("-" * 40)

    # Data parse করো
    parsed_data = parse_receipt(raw_text)

    print("\n✅ Parsed Data:")
    print(json.dumps(parsed_data, indent=4, ensure_ascii=False))

    # JSON file এ save করো
    with open("receipt_output.json", "w", encoding='utf-8') as f:
        json.dump(parsed_data, f, indent=4, ensure_ascii=False)

    print("\n💾 receipt_output.json এ save হয়েছে!")
    return parsed_data


# =============================================
# Run করো
# =============================================
if __name__ == "__main__":
    scan_receipt("receipt.jpg")  # তোমার receipt এর ছবি দাও