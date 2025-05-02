from parsers.DOCXParser import DOCXParser
from parsers.PDFParser import PDFParser
from parsers.PPTXParser import PPTXParser
from parsers.TXTParser import TXTParser
from algorithms.services.DocumentDownloader import DocumentDownloader
from algorithms.parsing.DocumentFormatDetector import DocumentFormatDetector

#TODO: handle unkown formats
#TODO: add logging
#TODO: add constant downloads directory
#TODO: use dynamic path calls from project root
class DocumentProcessor:
    def __init__(self):
        self.parser = None
        self.format_detector = DocumentFormatDetector()
        self.document_downloader = DocumentDownloader()
        self.file_path = None


    def extract_document_text(self, document_entry, output_dir):
        fmt = self.format_detector.detect_format(document_entry)
        if fmt == 'google_docs':
            self.file_path = self.document_downloader.download_google_doc_file(document_entry, output_dir)
            print(f'the file path is {self.file_path}')
            fmt = self.format_detector.detect_format(self.file_path)
            print(fmt)
        elif fmt == 'google_slides':
            self.file_path = self.document_downloader.download_google_slides_file(document_entry, output_dir)
            fmt = self.format_detector.detect_format(self.file_path)
            print(fmt)
        elif fmt == 'google_drive':
            self.file_path = self.document_downloader.download_google_drive_file(document_entry, output_dir)
            fmt = self.format_detector.detect_format(self.file_path)
            print(fmt)
        else:
            self.file_path = document_entry

        self.parser = self.parser_factory(fmt)

        
        if self.parser != None:
            return self.parser.extract_text(self.file_path)

    def parser_factory(self, fmt):
        try:
            if fmt == 'pdf':
                return PDFParser()
            elif fmt == 'txt':
                return TXTParser()
            elif fmt == 'pptx':
                return PPTXParser()
            elif fmt == 'docx':
                return DOCXParser()
            else:
                return None
        except Exception as e:
            return f"Error extracting: {str(e)}"

if __name__ == "__main__":

    processor = DocumentProcessor()
    # txt = processor.extract_document_text(r'C:\Users\Yusuf Aldaly\Desktop\AutoInspecta pitch Presentation.pptx', r'D:\Study\Level4\grad project\VC-management-system\algorithms\parsing')
    # print(txt)

    local_pptx_pitch_path = r"C:\Users\Yusuf Aldaly\Desktop\AutoInspecta pitch Presentation.pptx"
    local_pdf_cv_path = r"D:\college research& Applications\Graduate\YousefEldaly_cv.pdf"
    local_docx_cv_path = r"D:\college research& Applications\Graduate\samples\YousefEldaly_cv.docx"
    google_drive_pdf_cv_path = r"https://drive.google.com/file/d/1ttDR1vjYXVY0f1Mbs67n4sbr2d4hEuj4/view?usp=sharing"
    drive_docx_path = r"https://docs.google.com/document/d/1HFYH7BQ53PQqko3FtUCW16bUWFE0DRWY4yTMXv5Wjps/edit?usp=sharing"
    drive_slides_path = r"https://docs.google.com/presentation/d/12cZRRasxAtzRu4ghxQ0aHLxMcTUXdP6M/edit?usp=sharing&ouid=103231827187311264285&rtpof=true&sd=true"
    local_txt_file_path = r"D:\Study\Level4\semester2\IR\A1\is322_HW_1\collections\2.txt"
    linkedin_profile_url = r"https://www.linkedin.com/in/yousef-eldaly-617420176/"


    test_cases = {
        "Local PPTX Pitch": local_pptx_pitch_path,
        "Local PDF CV": local_pdf_cv_path,
        "Local DOCX CV": local_docx_cv_path,
        "Google Drive PDF CV": google_drive_pdf_cv_path,
        "Google docx docs": drive_docx_path,
        "Google docx slides" : drive_slides_path,
        "TXT File": local_txt_file_path,
        "LinkedIn Profile": linkedin_profile_url
    }
    
    for name, path in test_cases.items():
        print(f"\n--- Testing: {name} ---")
        extracted_text = processor.extract_document_text(path, r'D:\Study\Level4\grad project\VC-management-system\algorithms\parsing')
        print(extracted_text[:1000])
