from .file_processor import File_Processor
import fitz

class Pdf_Processor(File_Processor):
    def __init__(self):
        super().__init__()

    def extract_text(self, file_path):
        """
        Extract text from a PDF file.
        """
        try:
            text = ""
            with fitz.open(file_path) as file:
                for page in file:
                    text += page.get_text()
            return True, text
        except Exception as e:
            return False, f"An error occurred while extracting text: {str(e)}"