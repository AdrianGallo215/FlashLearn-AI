from pathlib import Path
from pdf_processor import PDFProcessor
from doc_processor import DocProcessor
from txt_processor import TxtProcessor	

def get_processor(file_path: str):
    ext = Path(file_path).suffix.lower()

    ext_dict = {".pdf": PDFProcessor(), ".txt": TxtProcessor(), ".doc": DocProcessor(), ".docx": DocProcessor()}
    return ext_dict.get(ext, None)
