import sys
import os
import requests

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.config.settings import Settings
#from config.settings import Settings

class IndexerStatus:
    def __init__(self) -> None:
        self.user = Settings.indexer_status_user
        self.header = Settings.indexer_status_header
        self.url = Settings.indexer_status_url

    def get_request_data(self):
        request = requests.get(self.url, headers=self.header)
        return request.text


if __name__ == '__main__':
    my_indexer = IndexerStatus()
    my_data = my_indexer.get_request_data()
    print(my_data)