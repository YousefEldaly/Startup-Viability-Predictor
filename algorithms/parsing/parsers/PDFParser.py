from .BaseDocumentParser import BaseDocumentParser
from PyPDF2 import PdfReader

class PDFParser(BaseDocumentParser):
    def extract_text(self, file_path):
        reader = PdfReader(file_path)
        return '\n'.join([page.extract_text() for page in reader.pages if page.extract_text()])
    