from elasticsearch import Elasticsearch
from gambit import  Msearch, Mpercolate, percolate_and_get
from pprint import pprint

es = Elasticsearch('54.254.200.31:9200')
q1 =  {"from": 0, "size": 2 }
q2 =  {"from": 0, "size": 2 }
q3 =  {"from": 0, "size": 2 }

d1 = {
    'doc': {
        'location': {
            'lat': 28.411599,
            'lon': 77.046451
        }
    }
}

d2 = {
    'doc': {
        'location': {
            'lat': 28.411599,
            'lon': 77.046451
        }
    }
}


def test_percolate_and_get():
    results = percolate_and_get(es, d2, index='grofers_throttle_index', doc='locality_throttle')
    pprint(results)


def test_msearch():
    s = Msearch(es)
    s.add(q1, index='grofers-index-v3', doc_type='merchant')
    s.add(q2, index='grofers-index-v3', doc_type='merchant')
    pprint(s.execute())

def test_msearch_index():
    s = Msearch(es, index='grofers-index-v3')
    s.add(q1, doc_type='merchant')
    s.add(q2, doc_type='merchant')
    pprint(s.execute())

def test_mpercolate():
    s = Mpercolate(es)
    s.add(d1, index='grofers_throttle_index', doc_type='locality_throttle')
    s.add(d2, index='grofers_throttle_index', doc_type='locality_throttle')
    pprint(s.execute())

def test_mpercolate_index():
    s = Mpercolate(es, index='grofers_throttle_index')
    s.add(d1, doc_type='locality_throttle')
    s.add(d2, doc_type='locality_throttle')
    pprint(s.execute())


test_percolate_and_get()
test_msearch()
test_msearch_index()
test_mpercolate()
test_mpercolate_index()
