import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    GOOGLEA_SEARCH_API_KEY = os.getenv('GOOGLE_SEARCH_API_KEY')
    VC_SEARCH_ENGINE_ID = os.getenv('VC_SEARCH_ENGINE_ID')
    LLM_MODEL = os.getenv('LLM_MODEL')
    LOG_FILE_NAME = os.getenv('LOG_FILE_NAME')
    ROOT_DIR = os.getenv('ROOT_DIR')