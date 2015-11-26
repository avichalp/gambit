from elasticsearch import Elasticsearch
from gambit import gambit
from pprint import pprint

es = Elasticsearch()
q1 =  {"from": 0, "size": 2 }
q2 =  {"from": 0, "size": 2 }
q3 =  {"from": 0, "size": 2 }

def test_index_and_doc():
    
    responses = gambit(es, index_name='grofers-index-v3', doc_name='merchant')(q1, q2, q3)
    results = [result for result in responses]
    pprint(results)
    
test_index_and_doc()
