from .BaseDocumentParser import BaseDocumentParser
from docx import Document

class DOCXParser(BaseDocumentParser):
    def extract_text(self, file_path):
        doc = Document(file_path)
        text = []

        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        
        return "\n".join(text)