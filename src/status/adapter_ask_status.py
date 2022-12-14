import zope.interface
from src.status.ask_status import ASKStatus
from src.status.interface_status import IStatus
import src.status.dict as dict

@zope.interface.implementer(IStatus)
class AdapterASKStatus:
    def __init__(self, ask_inst:ASKStatus) -> None:
        self.ask = ask_inst

    def get_status(self):
        obj = []
        row_data = self.ask.get_request_data()
        for item in row_data["data"]["serviceStatus"]:
            # To Normalize the response status - we use dictionary
            status = dict.status_dict[item["Status"]]
            obj.append({"serviceName": item["Name"], "serviceStatus": status})
        return obj

if __name__ == '__main__':
    my_ask_status = AdapterASKStatus(ASKStatus()).get_status()
    print(*my_ask_status, sep = "\n")