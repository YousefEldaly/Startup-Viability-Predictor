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
from algorithms.parsing.DocumentProcessor import DocumentProcessor
import json

logger = logging.getLogger(__name__)


setup_logging()


# processor = DocumentProcessor()
# path = r"https://www.linkedin.com/in/yousef-eldaly-617420176/"
# extracted_text = processor.extract_document_text(path, r'D:\Study\Level4\grad project\VC-management-system\algorithms\parsing\downloads')
# print(extracted_text[:1000])


startup_info = "DXwand is an Egyptian AI startup founded in 2018 by Ahmed Mahmoud. It specializes in conversational AI for businesses across the MENA region, with a focus on Arabic language support. The platform automates customer interactions via call centers, messaging apps, and websites, combining conversational AI with business intelligence to streamline operations and extract insights. DXwand serves industries like education (lesson planning), finance (risk analysis), and healthcare (service efficiency). In 2024, the startup raised $4 million in Series A funding to expand regionally and enhance R&D in LLMs and generative AI. With offices in Egypt, the UAE, and Saudi Arabia, DXwand aims to lead AI innovation in the Middle East, proving that local talent can compete globally."

prompt = get_prompt("market_keyword")
json_response_format = get_json_response_format("market_keyword")


llm = OpenAI_API()

result = llm.get_json_response(prompt, startup_info, json_response_format)

print(f"result of prompt is:{result}")

google_search_api = GoogleSearch_API()
results = google_search_api.search(result["search_query"])

print(results)