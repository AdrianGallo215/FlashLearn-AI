from pathlib import Path
from .pdf_processor import Pdf_Processor
from .doc_processor import Doc_Processor
from .txt_processor import Txt_Processor	

def get_processor(file_path: str):
    ext = Path(file_path).suffix.lower()

    ext_dict = {".pdf": Pdf_Processor(), ".txt": Txt_Processor(), ".doc": Doc_Processor(), ".docx": Doc_Processor()}
    return ext_dict.get(ext, None)
