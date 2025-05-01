from docx import Document
from .file_processor import File_Processor
from ...utils.logger_config import setup_logger

logger = setup_logger(__name__)

class Doc_Processor(File_Processor):
    def __init__(self):
        super().__init__()

    def extract_text(self, file_path):
        """
        Extract text from a DOCX file.
        """
        try:
            doc = Document(file_path)
            text = []
            for paragraph in doc.paragraphs:
                # Check if the paragraph is not empty
                if paragraph.text.strip():
                    # Append the text of the paragraph to the list
                    text.append(paragraph.text)
            return True, "\n".join(text)
        except Exception as e:
            return False, f"An error occurred while extracting text: {str(e)}"