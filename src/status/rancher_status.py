import sys
import os
import requests
from requests.structures import CaseInsensitiveDict


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.config.settings import Settings
#from config.settings import Settings

class RancherStatus:
    def __init__(self) -> None:
        self.headers = None
        self.ver_url = None
        self.cluster_id = None
        self.url = None

    def get_cluster_id(self):
        self.headers = CaseInsensitiveDict()
        self.headers["content-type"] = "application/json"
        self.headers["Authorization"] = "Bearer "+ Settings.rancher_status_token
        self.ver_url = Settings.rancher_status_ver_url

        request = requests.get(self.ver_url, headers=self.headers, verify=False)
        self.cluster_id = request.json()['data'][0]['id']

    def get_request_data(self):
        self.get_cluster_id()
        self.url = Settings.rancher_status_url + self.cluster_id
        request = requests.get(self.url, headers=self.headers, verify=False)
        return request.json()

if __name__ == '__main__':
    my_rancher = RancherStatus()
    my_data = my_rancher.get_request_data()
    print(my_rancher.headers)
    print(my_rancher.ver_url)
    print(my_rancher.cluster_id)
    print(my_rancher.url)
    print(my_data)
