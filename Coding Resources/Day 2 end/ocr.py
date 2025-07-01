import pytesseract
from PIL import Image

def ocr_from_image(image_path):
    """
    Perform OCR on the given image and return the transcribed text.

    :param image_path: Path to the image file
    :return: Transcribed text from the image
    """
    try:
        # Open the image file
        image = Image.open(image_path)
        
        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(image)
        
        return text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Perform OCR and display the result
    result = ocr_from_image('example.png')
    print("\nTranscribed Text:")
    print(result)