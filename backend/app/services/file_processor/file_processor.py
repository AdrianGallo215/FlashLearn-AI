from pathlib import Path
from werkzeug.utils import secure_filename
from abc import ABC, abstractmethod
from ...utils.logger_config import setup_logger

logger = setup_logger(__name__)

class File_Processor(ABC):
    def __init__(self):
        self.allowed_extensions = {'txt', 'pdf', 'doc', 'docx'}
        self.temp_dir = Path(__file__).parent.parent.parent / 'temp'

    def is_file_valid(self, file):
        if not file:
            return False, "No file provided"
        if file.filename == '':
            return False, "No selected file"
        if '.' not in file.filename:
            return False, f"File '{file.filename}' has no extension."

        file_extension = file.filename.rsplit('.', 1)[1].lower()

        if file_extension in self.allowed_extensions:
            return True, "Valid file"
        else:
            return False, "Invalid file extension"

    def save_file(self, file):
        is_valid, validation_message = self.is_file_valid(file)

        if not is_valid:
            return False, validation_message

        try:
            safe_file_name = secure_filename(file.filename)
            if not safe_file_name:
                return False, "Invalid file name"
            
            file_path = self.temp_dir / safe_file_name
            file.save(str(file_path))
            return True, str(file_path)
        except Exception as e:
            return False, f"An error occurred while saving the file: {str(e)}"

    def delete_file(self, file_path):
        try:
            if Path(file_path).exists():
                Path(file_path).unlink()
                logger.info(f"File {file_path} deleted successfully")
            else:
                logger.warning(f"File {file_path} not found")
        except Exception as e:
            logger.error(f"An error occurred while deleting the file: {str(e)}")

    @abstractmethod    
    def extract_text(self, file_path):
        pass