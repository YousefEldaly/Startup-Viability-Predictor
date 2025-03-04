from API_wrapper import OpenAI_API
from utils.configs import Config
from utils import extract_json_from_llm_response, get_prompt, get_json_response_format
import json


startup_info = "DXwand is an Egyptian AI startup founded in 2018 by Ahmed Mahmoud. It specializes in conversational AI for businesses across the MENA region, with a focus on Arabic language support. The platform automates customer interactions via call centers, messaging apps, and websites, combining conversational AI with business intelligence to streamline operations and extract insights. DXwand serves industries like education (lesson planning), finance (risk analysis), and healthcare (service efficiency). In 2024, the startup raised $4 million in Series A funding to expand regionally and enhance R&D in LLMs and generative AI. With offices in Egypt, the UAE, and Saudi Arabia, DXwand aims to lead AI innovation in the Middle East, proving that local talent can compete globally."

prompt = get_prompt("market_keyword")
json_response_format = get_json_response_format("market_keyword")


llm = OpenAI_API()

result = llm.get_json_response(prompt, startup_info, json_response_format)

print(f"result of prompt2 is:{result}")

print("################the extracted json############")