import json
import os

class Get_History:

    def put_history_data(self, obj):
        grandSum = obj["grandSummaryStatus"]
        obj["grandSummaryHistory"] = grandSum
        fatherSum = [obj["data"][index]["summaryStatus"] for index in range(len(obj["data"]))]
        for i in range(len(obj["data"])):
            d = obj["data"][i]
            d["summaryHistory"] = fatherSum
            childSum = [d["services"][jndex]["serviceStatus"] for jndex in range(len(d["services"]))]
            for j in range(len(d["services"])):
                d["services"][j]["history"] = childSum
        return obj

    def get_history_status(self ,wpath):
        with open(wpath + "\\sample.json" ,"r") as output:
            sample = json.load(output)
        history = self.put_history_data(sample)
        with open(os.getcwd() + "\\sample_test.json" ,"w") as output:
            sample = json.dump(history, output, indent=4)

if __name__ == '__main__':
    my_data = Get_History().get_history_status('\\'.join(os.getcwd().split('\\')[:-1]))
