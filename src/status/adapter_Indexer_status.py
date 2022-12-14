import zope.interface
from bs4 import BeautifulSoup
import src.status.dict as dict
from src.status.indexer_status import IndexerStatus
from src.status.interface_status import IStatus
#from indexer_status import IndexerStatus
#from interface_status import IStatus


@zope.interface.implementer(IStatus)
class AdapterIndexerStatus:
    def __init__(self, indexer_inst:IndexerStatus) -> None:
        self.indexer = indexer_inst

    def get_status(self):
        obj = []
        status = None
        row_data = self.indexer.get_request_data()
        soup = BeautifulSoup(row_data, 'html.parser')

        for element in soup.find_all("h1"):
            # To Normalize the response status - we use dictionary
            status = dict.status_dict[element.get("style")]
            elementContent = element.next
            obj.append({"serviceName": elementContent, "serviceStatus": status})
        return obj

if __name__ == '__main__':
    my_indexer_status = AdapterIndexerStatus(IndexerStatus()).get_status()
    print(*my_indexer_status, sep = "\n")

