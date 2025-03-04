import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from utils.configs import Config




class GoogleSearch_API:
    def __init__(self):
        self.api_key = Config.GOOGLEA_SEARCH_API_KEY
        self.search_engine_id = Config.VC_SEARCH_ENGINE_ID

    def search(self, query, results_num=1):
        url = 'https://www.googleapis.com/customsearch/v1'
        params = {
            'q' : query,
            'key' : self.api_key,
            'cx' : self.search_engine_id

        }

        response = requests.get(url, params)

        return response.json()
    

if __name__ == "__main__":
    google_search_api = GoogleSearch_API()
    results = google_search_api.search("AI market")
    print(results)




