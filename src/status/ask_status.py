import sys
import os
import requests

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.config.settings import Settings

class ASKStatus:
    def __init__(self) -> None:
        self.user = Settings.ask_status_user
        self.header = Settings.ask_status_header
        self.url = Settings.ask_status_url

    def get_request_data(self):
        request = requests.get(self.url, headers=self.header)
        return request.json()

if __name__ == '__main__':
    my_ask = ASKStatus()
    my_data = my_ask.get_request_data()
    print(my_data)