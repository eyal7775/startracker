'''
from src.status.ask_status import ASKStatus
from src.status.adapter_ask_status import AdapterASKStatus
from src.status.indexer_status import IndexerStatus
from src.status.adapter_Indexer_status import AdapterIndexerStatus
from src.status.rancher_status import RancherStatus
from src.status.adapter_rancher_status import AdapterRanchertatus
from src.status.dlg_status import DLGStatus
from src.status.adapter_dlg_status import AdapterDLGStatus
'''

# for debug
import json
from src.status.ask_status import ASKStatus
from src.status.adapter_ask_status import AdapterASKStatus
from src.status.indexer_status import IndexerStatus
from src.status.adapter_Indexer_status import AdapterIndexerStatus
from src.status.rancher_status import RancherStatus
from src.status.adapter_rancher_status import AdapterRanchertatus
from src.status.dlg_status import DLGStatus
from src.status.adapter_dlg_status import AdapterDLGStatus
import status.dicts_and_lists as dicts_and_lists

class Facade:
    def __init__(self) -> None:
        pass

    def get_summary_status(self, obj):
        summary_status = "green"
        for element in obj:
            if element["serviceStatus"] == "red":
                summary_status = "red"
            elif element["serviceStatus"] == "orange" and summary_status != "red":
                    summary_status = "orange"
            element["history_data"] = []
        return summary_status

    def get_grand_summary_status(self, obj):
        grand_summary_status = "green"
        for element in obj:
            if element["summaryStatus"] == "red":
                grand_summary_status = "red"
            elif element["summaryStatus"] == "orange" and grand_summary_status != "red":
                    grand_summary_status = "orange"
        return grand_summary_status

    def get_history_status(self, obj):
        history = []


    def get_all_status_data(self):
        merged_obj = dict()
        final_obj = []
        #====================================================
        #=====================ASK============================
        #====================================================
        ask_cloudera_elk_status = AdapterASKStatus(ASKStatus()).get_status()
        ask_status = [i for i in ask_cloudera_elk_status if not (i["serviceName"] in dicts_and_lists.cloudera_services_list)
                                                        and not (i["serviceName"] in dicts_and_lists.elk_services_list)]
        ask_summary_status = self.get_summary_status(ask_status)
        final_obj.append({"name": "ASK", "summaryStatus": ask_summary_status, "summaryHistory": [], "services": ask_status})

        #====================================================
        #=====================ELK============================
        #====================================================
        elk_status = [i for i in ask_cloudera_elk_status if (i["serviceName"] in dicts_and_lists.elk_services_list)]
        elk_summary_status = self.get_summary_status(elk_status)
        final_obj.append({"name": "ELK", "summaryStatus": elk_summary_status, "summaryHistory": [], "services": elk_status})

        #====================================================
        #=====================Cloudera=======================
        #====================================================
        cloudera_status = [i for i in ask_cloudera_elk_status if (i["serviceName"] in dicts_and_lists.cloudera_services_list)]
        cloudera_summary_status = self.get_summary_status(cloudera_status)
        final_obj.append({"name": "Cloudera", "summaryStatus": cloudera_summary_status, "summaryHistory": [], "services": cloudera_status})

        #====================================================
        #=====================Indexer========================
        #====================================================
        indexer_status = AdapterIndexerStatus(IndexerStatus()).get_status()
        indexer_summary_status = self.get_summary_status(indexer_status)
        final_obj.append({"name": "Indexer", "summaryStatus": indexer_summary_status, "summaryHistory": [], "services": indexer_status})

        #====================================================
        #=====================rancher========================
        #====================================================
        rancher_status = AdapterRanchertatus(RancherStatus()).get_status()
        rancher_summary_status = self.get_summary_status(rancher_status)
        final_obj.append({"name": "Rancher", "summaryStatus": rancher_summary_status, "summaryHistory": [], "services": rancher_status})

        #====================================================
        #=========================DLG========================
        #====================================================
        dlg_status = AdapterDLGStatus(DLGStatus()).get_status()
        dlg_summary_status = self.get_summary_status(dlg_status)
        final_obj.append({"name": "DLG", "summaryStatus": dlg_summary_status, "summaryHistory": [], "services": dlg_status})

        grand_summary_status = self.get_grand_summary_status(final_obj)
        merged_obj["grandSummaryStatus"] = grand_summary_status
        merged_obj["grandSummaryHistory"] = []
        merged_obj["data"] = final_obj

        # ask_history_status = self.get_history_status(final_obj)

        return merged_obj

if __name__ == '__main__':
    '''
        ask_cloudera_elk_status = AdapterASKStatus(ASKStatus()).get_status()
    ask = [i for i in ask_cloudera_elk_status if not (i["serviceName"] in dict.cloudera_services_list) and not (i["serviceName"] in dict.elk_services_list)]
    elk = [i for i in ask_cloudera_elk_status if (i["serviceName"] in dict.elk_services_list)]
    cloudera = [i for i in ask_cloudera_elk_status if (i["serviceName"] in dict.cloudera_services_list)]
    print("==========================================")
    print(ask_cloudera_elk_status)
    print("==========================================")
    print(ask)
    print("==========================================")
    print(elk)
    print("==========================================")
    print(cloudera)
    print("==========================================")
    '''
    my_data = Facade().get_all_status_data()
    #print(my_data)

    with open("sample.json", "w") as outfile:
        json.dump(my_data, outfile, indent=4)


