import sys
import os
import logging
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from utils.configs import Config
logger = logging.getLogger(__name__)

class GoogleSearch_API:
    def __init__(self):
        self.api_key = Config.GOOGLEA_SEARCH_API_KEY
        self.search_engine_id = Config.VC_SEARCH_ENGINE_ID

    def search(self, query, results_num=1):
        logging.info("Calling Google Search API")
        try:
            url = 'https://www.googleapis.com/customsearch/v1'
            params = {
                'q' : query,
                'key' : self.api_key,
                'cx' : self.search_engine_id,
                'dateRestrict' : 'y[1]',
                'filter' : '1',
                'gl' : 'countryEG',
                'num' : results_num,
                'safe' : 'active'
            }

            response = requests.get(url, params)

            self._log_API_call_status(response.status_code)

            return response.json()
        
        except Exception as e:
            logger.exception(f"An Exception occured during calling the LLM API: {str(e)}")


    def _log_API_call_status(self, status_code):
        if status_code == 200:
            logger.info(f"LLM API call done sucessfully: {status_code}")
        else:
            logger.exception(f"LLM API call was unsuccessful: {status_code}")
            raise Exception('Check call parameters; api_key, model, etc.')


# testing the api call
if __name__ == "__main__":
    google_search_api = GoogleSearch_API()
    results = google_search_api.search("AI market")
    print(results)




