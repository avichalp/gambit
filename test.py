from elasticsearch import Elasticsearch
from gambit import Gambit
from pprint import pprint

es = Elasticsearch()
q1 =  {"from": 0, "size": 2 }
q2 =  {"from": 0, "size": 2 }
q3 =  {"from": 0, "size": 2 }

def test_index_and_doc():

    g = Gambit(es)
    responses = g.search(index='grofers-index-v3', doc='merchant')(q1, q2, q3)
    results = [result for result in responses]
    pprint(results)


def test_index():

    g = Gambit(es)
    qf = g.search(index='grofers-index-v3')
    responses = qf(
        ('merchant', q1),
        ('merchant', q2),
        ('merchant', q3)
    )
    results = [result for result in responses]
    pprint(results)


def test():

    g = Gambit(es)
    qf = g.search()
    responses = qf(
        ('grofers-index-v3', 'merchant', q1),
        ('grofers-index-v3', 'merchant', q2),
        ('grofers-index-v3', 'merchant', q3)
    )
    results = [result for result in responses]
    pprint(results)


def test_index_doc_get():

    g = Gambit(es)
    responses = g.get(index='grofers-index-v3', doc='merchant')(1,39,91,256,546)
    results = [result for result in responses]
    pprint(results)


def test_doc_get():

    g = Gambit(es)
    responses = g.get(index='grofers-index-v3')(
        ('merchant', 1),
        ('merchant', 2)
    )
    results = [result for result in responses]
    pprint(results)

def test_get():

    g = Gambit(es)
    responses = g.get()(
        ('grofers-index-v3', 'merchant', 1),
        ('grofers-index-v3', 'merchant', 2)
    )
    results = [result for result in responses]
    pprint(results)


test_index_and_doc()
test_index()
test()
test_get()
test_doc_get()
test_index_doc_get()
