import re


class DocumentFormatDetector():
    def detect_format(self, document_entry):
        if isinstance(document_entry, str):
            if re.search(r'https://docs\.google\.com/document/d/', document_entry):
                return 'google_docs'
            elif re.search(r'https://docs\.google\.com/presentation/d/', document_entry):
                return 'google_slides'
            elif re.search(r'drive\.google\.com', document_entry, re.IGNORECASE):
                return 'google_drive'
            elif document_entry.lower().endswith('.pdf'):
                return 'pdf'
            elif document_entry.lower().endswith('.txt'):
                return 'txt'
            elif document_entry.lower().endswith('.pptx'):
                return 'pptx'
            elif document_entry.lower().endswith('.ppt'):
                return 'ppt'
            elif document_entry.lower().endswith('.docx'):
                print('docx')
                return 'docx'
            else:
                raise ValueError(f"Can not detect format of given input: {document_entry}")
        raise ValueError('Input should be a string')