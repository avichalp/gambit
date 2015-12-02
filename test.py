from elasticsearch import Elasticsearch
from gambit import Gambit
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

    g = Gambit(es)
    results = g.percolate_and_get(d2, index='grofers_throttle_index', doc='locality_throttle')
    pprint(results)

def test_percolate_index_doc():

    g = Gambit(es)
    responses = g.percolate(d1, d2, index='grofers_throttle_index', doc='locality_throttle')
    results = [result for result in responses]
    pprint(results)

def test_percolate_index():

    g = Gambit(es)
    responses = g.percolate(
        ('locality_throttle', d1),
        ('locality_throttle', d2),
        index='grofers_throttle_index'
    )
    results = [result for result in responses]
    pprint(results)


def test_percolate():

    g = Gambit(es)
    responses = g.percolate(
        ('grofers_throttle_index', 'locality_throttle', d1),
        ('grofers_throttle_index', 'locality_throttle', d2)
    )
    results = [result for result in responses]
    pprint(results)

def test_index_and_doc():

    g = Gambit(es)
    responses = g.search(q1, q2, q3, index='grofers-index-v3', doc='merchant')
    results = [result for result in responses]
    pprint(results)


def test_index():

    g = Gambit(es)
    responses = g.search(
        ('merchant', q1),
        ('merchant', q2),
        ('merchant', q3),
        index='grofers-index-v3'
    )
    results = [result for result in responses]
    pprint(results)


def test():

    g = Gambit(es)
    responses = g.search(
        ('grofers-index-v3', 'merchant', q1),
        ('grofers-index-v3', 'merchant', q2),
        ('grofers-index-v3', 'merchant', q3)
    )
    results = [result for result in responses]
    pprint(results)


def test_index_doc_get():

    g = Gambit(es)
    responses = g.get(
        1,39,91,256,546,
        index='grofers-index-v3',
        doc='merchant'
    )
    results = [result for result in responses]
    pprint(results)


def test_doc_get():

    g = Gambit(es)
    responses = g.get(
        ('merchant', 1),
        ('merchant', 2),
        index='grofers-index-v3'
    )
    results = [result for result in responses]
    pprint(results)

def test_get():

    g = Gambit(es)
    responses = g.get(
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
test_percolate()
test_percolate_index_doc()
test_percolate_index()
test_percolate_and_get()
