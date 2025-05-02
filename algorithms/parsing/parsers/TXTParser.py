from .BaseDocumentParser import BaseDocumentParser

class TXTParser(BaseDocumentParser):
    def extract_text(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
        