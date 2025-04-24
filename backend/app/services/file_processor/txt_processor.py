class Txt_Processor(File_Processor):
    def __init__(self):
        super().__init__()

    def extract_text(self, file_path):
        """
        Extract text from a TXT file.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            return True, text
        except Exception as e:
            return False, f"An error occurred while extracting text: {str(e)}"