from elasticsearch import Elasticsearch
from gambit import gambit
from pprint import pprint

es = Elasticsearch()
q1 =  {"from": 0, "size": 2 }
q2 =  {"from": 0, "size": 2 }
q3 =  {"from": 0, "size": 2 }

def test_index_and_doc():

    responses = gambit(es, index='grofers-index-v3', doc='merchant')(q1, q2, q3)
    results = [result for result in responses]
    pprint(results)


def test_index():

    qf = gambit(es, index='grofers-index-v3')
    responses = qf(
        ('merchant', q1),
        ('merchant', q2),
        ('merchant', q3)
    )
    results = [result for result in responses]
    pprint(results)


def test():

    qf = gambit(es)
    responses = qf(
        ('grofers-index-v3', 'merchant', q1),
        ('grofers-index-v3', 'merchant', q2),
        ('grofers-index-v3', 'merchant', q3)
    )
    results = [result for result in responses]
    pprint(results)


test_index_and_doc()
test_index()
test()
