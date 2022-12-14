import zope.interface
import src.status.dict as dict
from src.status.rancher_status import RancherStatus
from src.status.interface_status import IStatus
#from rancher_status import RancherStatus
#from interface_status import IStatus

@zope.interface.implementer(IStatus)
class AdapterRanchertatus:
    def __init__(self, rancher_inst:RancherStatus) -> None:
        self.rancher = rancher_inst

    def get_status(self):
        obj = []
        status = None
        row_data = self.rancher.get_request_data()

        for item in row_data["componentStatuses"]:
            # To Normalize the response status - we use dictionary
            status = dict.status_dict[item["conditions"][0]["type"]]
            obj.append({"serviceName": item["name"], "serviceStatus": status})
        return obj

if __name__ == '__main__':
    my_ask_status = AdapterRanchertatus(RancherStatus()).get_status()
    print(*my_ask_status, sep = "\n")