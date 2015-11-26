from elasticsearch import Elasticsearch
from gambit import gambit
from pprint import pprint

def test_index_and_doc():
    es = Elasticsearch()
    q1 =  {"from": 0, "size": 2 }
    q2 =  {"from": 0, "size": 2 }
    q3 =  {"from": 0, "size": 2 }
    
    response = gambit(es, 'grofers-index-v3', 'merchant')(q1, q2, q3)
    results = [result for result in response.get('responses')]
    pprint(results)
    
test_index_and_doc()
