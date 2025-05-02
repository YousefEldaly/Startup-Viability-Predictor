import sys
import os
import re

import requests
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.configs import Config


#TODO: remove comment deploying
#ROOT_DIR = Config.ROOT_DIR
ROOT_DIR = r"D:\Study\Level4\grad project\VC-management-system"


class BaseDocumentParser:

    def extract_text(self, file_path):
        raise NotImplementedError("This function should be used from children classes")



    
    # @staticmethod
    # def extract_linkedin_summary(link):
    #     return f"LinkedIn Profile: {link} \n scrapping linkedin profiles is not legal at the moment. please provide another format" 
    
