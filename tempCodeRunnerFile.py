import os
import sys

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
os.environ['ROOT_DIR'] = ROOT_DIR
sys.path.insert(0, ROOT_DIR)
print(ROOT_DIR)


from API_wrapper import OpenAI_API, GoogleSearch_API
from utils.configs import Config
import logging.config
import atexit
from utils.utils import get_prompt, get_json_response_format, setup_logging, update_root_dir_in_env
from algorithms.parsing import DocumentProcessor
import json