'''
The following dictionaries is an aliases for the following services - by this order
*) ASK
*) Indexer
*) DLG
*) Rancher
'''

status_dict = {
    "OK": "green",
    "ERROR": "red",
    "WARNING": "orange",

    "color:lightgreen": "green",
    "color:red": "red",

    "up": "green",
    "down": "red",

    "Healthy": "green"
}

service_name_dict = {
    "Micro-services": "Indexer",
    "Solr": "Solr",
    "YARN": "YARN",
    "ZooKeeper": "ZooKeeper",
    "Hive": "Hive",
    "ElasticSearch": "ElasticSearch",
    "Kibana": "Kibana",
    "Logstash": "Logstash",
    "PgAgent": "PgAgent",
    "Query Engine": "Query Engine",
    "PostgreSQL": "PostgreSQL",
    "Synthetic and Comparison": "Synthetic and Comparison",
    "Impala": "Impala",
    "HDFS": "HDFS",
    "Redis": "Redis",
    "mdc_cm3": "k8s-Cloudera Connectivity",
    "SSH connections": "k8s-Cloudera Connectivity",

    "IMPALA STATE:": "Impala",
    "SOLR STATE:": "Solr",
    "REDIS STATE:": "Redis",
    "PG STATE:": "PostgreSQL",

    "ASK_SERVICE": "Dependent Services",
    "QUERY_TOOL_SERVICE": "Dependent Services",
    "DC_DATABASE": "PostgreSQL",
    "MDCLONE_DATABASE": "Dependent Services",
    "REDIS": "Redis",
    "MICRO_MANAGER": "MicroManager",

    "controller-manager": "Contriller Manager",
    "etcd-0": "etcd-0",
    "etcd-1": "etcd-1",
    "etcd-2": "etcd-2",
    "scheduler": "Scheduler"
}

'''
The following lists are for creating new logical groups,
from existing api responses. For example extracting from ASK system-check api,
Cloudera and ELK statuses and creating 2 new logical groups.
'''
cloudera_services_list = ["Solr", "YARN", "HDFS", "ZooKeeper", "Hive", "Impala"]
elk_services_list = ["ElasticSearch", "Kibana", "Logstash"]

if __name__ == '__main__':
    pass