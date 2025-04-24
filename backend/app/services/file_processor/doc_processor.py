from docx import Document

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
                text.append(paragraph.text)
            return True, "\n".join(text)
        except Exception as e:
            return False, f"An error occurred while extracting text: {str(e)}"