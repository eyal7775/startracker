import sys
import os
import requests

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.config.settings import Settings
#from config.settings import Settings

class DLGStatus:
    def __init__(self) -> None:
        self.user = Settings.dlg_status_user
        self.header = Settings.dlg_status_header
        self.url = Settings.dlg_status_url

    def get_request_data(self):
        request = requests.get(self.url, headers=self.header, verify=False)
        return request.json()

if __name__ == '__main__':
    my_dlg = DLGStatus()
    my_data = my_dlg.get_request_data()
    print(my_data)