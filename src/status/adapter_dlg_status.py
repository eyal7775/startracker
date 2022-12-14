import jinja2
import zope.interface
import src.status.dict as dict
from src.status.dlg_status import DLGStatus
from src.status.interface_status import IStatus
#from status.dlg_status import DLGStatus
#from status.interface_status import IStatus

@zope.interface.implementer(IStatus)
class AdapterDLGStatus:
    def __init__(self, dlg_inst:DLGStatus) -> None:
        self.dlg = dlg_inst

    def get_status(self):
        obj = []
        status = None
        rel_path = "/static/images/"
        row_data = self.dlg.get_request_data()

        for item in row_data:
            # To Normalize the response status - we use dictionary
            status = dict.status_dict[row_data[item]["status"]]
            obj.append({"serviceName": item, "serviceStatus": status})
        return obj

if __name__ == '__main__':
    my_ask_status = AdapterDLGStatus(DLGStatus()).get_status()
    print(*my_ask_status, sep = "\n")