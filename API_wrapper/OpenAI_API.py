import requests
import json
import logging
from utils.configs import Config
from dotenv import load_dotenv

load_dotenv()

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
                "content": f"{system_content} \nRespond strictly with a JSON object. Do not explain, analyze, or include extra text."
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


        response = response.json()
        
        return response['choices'][0]['message']['content']
      
      except Exception as e:
        logger = logging.getLogger(__name__)
        logging.basicConfig(filename=Config.LOG_FILE_NAME, encoding="utf-8", level=logging.ERROR)
        logger.error(f"An Exception occured during calling the LLM API: {str(e)}")
    
    def _log_start_API_call_info(self):
      logger = logging.getLogger(__name__)
      logging.basicConfig(filename=Config.LOG_FILE_NAME, encoding="utf-8", level=logging.INFO)
      logger.info("#################################")
      logger.info("Calling LLM API")
      logger.info(f"Model Name: {self.model}")
      logger.info("#################################")
    
    def _log_API_call_status(self, status_code):
      logger = logging.getLogger(__name__)
      logging.basicConfig(filename=Config.LOG_FILE_NAME, encoding="utf-8", level=logging.INFO)
      if status_code == 200:
        logger.info(f"LLM API call done sucessfully: {status_code}")
      else:
        logger.error(f"LLM API call was unsuccessful: {status_code}")
        raise Exception('Check call parameters; api_key, model, etc.')
