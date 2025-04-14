import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import json
import logging
from utils.configs import Config
from utils import extract_json_from_llm_response
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


class OpenAI_API:
    
    def __init__(self) -> None:
      self.api_key = Config.OPENAI_API_KEY
      self.model = Config.LLM_MODEL

    
    def get_response(self, system_content, user_content):
      
      self._log_start_API_call_info()

      try:
        response = requests.post(
          url="https://openrouter.ai/api/v1/chat/completions",
          headers={
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json",
          },
          data=json.dumps({
            "model": self.model,
            "messages": [
              {
                "role": "system",
                "content": f"{system_content}"
              },
              {
                "role": "user",
                "content": user_content
              }
            ],
            "response_format": {"type": "json_object"},
            "structured_outputs": True,
          })
        )

        self._log_API_call_status(response.status_code)

        
        return response
      
      except Exception as e:
        logger.error(f"An Exception occured during calling the LLM API: {str(e)}")
    
    def get_json_response(self, system_content, user_content, json_format):

      try:
        system_content = f"{system_content}\nRespond strictly with a JSON object following this format {json_format}. Do not explain, analyze, or include extra text."
        extracted_json_object = self._get_json_response(system_content, user_content)
        
        return extracted_json_object
      
      except ValueError as ve:
        logger.error(f"an exception occured while extracting json {ve}")

        for i in range(3):
          logger.warning(f"Trial {i+1} of generating a different response")
          extracted_json_object = self._get_json_response(system_content, user_content)
          if extracted_json_object:
            return extracted_json_object


    def _get_json_response(self, system_content, user_content):
      response = self.get_response(system_content, user_content)
      response_content = response.json()['choices'][0]['message']['content']
      logger.info("Extracting json from response content")
      extracted_json_object = extract_json_from_llm_response(response_content)
      logger.info("JSON extracted successfully")

      return extracted_json_object


    def _log_start_API_call_info(self):
      logger.info("Calling LLM API")
      logger.info(f"Model Name: {self.model}")
    
    def _log_API_call_status(self, status_code):
      if status_code == 200:
        logger.info(f"LLM API call done sucessfully: {status_code}")
      else:
        logger.error(f"LLM API call was unsuccessful: {status_code}")
        raise Exception('Check call parameters; api_key, model, etc.')
