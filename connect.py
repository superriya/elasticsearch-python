import json
from typing import Sized
from elasticsearch import Elasticsearch
from config import *


my_instance = Elasticsearch(es_host,http_auth=(es_user, es_password),use_ssl=True, verify_certs=False)

if not my_instance:
    print("Connection Error")
else:
    print("Connection Successful!")


# Execute _search query
def serach_es(es_query, search_index="kibana_sample_data_flights"):
    response = my_instance.search(index=search_index, body=es_query)
    return response


# Search Query
es_query = {
    "query": {
        "match_all": {}
    }
}

if __name__ =="__main__":
    es_result = serach_es(es_query)
    print(json.dumps(es_result.get("hits",{}).get("hits"), indent=2))
    print(len(es_result.get('hits',{}).get('hits')))
else:
    print("connect module imported")


# es_result = serach_es(es_query,search_index="app_wallet_01")
# print(f"found {len(es_result.get('hits',{}).get('hits'))} documents in given query for app_wallet index")

# es_result = serach_es(es_query,search_index="kibana_sample_data_flights")
# print(f"Data here is: {json.dumps(es_result.get('hits',{}).get('hits'), indent=2)}")
# print(f"found {len(es_result.get('hits',{}).get('hits'))} documents in given query for kibana index")