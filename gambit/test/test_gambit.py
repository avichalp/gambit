import pytest
import sys

sys.path.append('/'.join(__file__.split('/')[0:-3]))

from elasticsearch import Elasticsearch
from gambit import  Msearch, Mpercolate, percolate_and_get

es = Elasticsearch('localhost:9200')
q1 =  {"from": 0, "size": 2 }
q2 =  {"from": 0, "size": 2 }
q3 =  {"from": 0, "size": 2 }

dummy_mappings = {
    "test-doc": {
        "properties": {
            "id": {
                "type": "integer"
            },
            "name": {
                "type": "string"
            },
            "color": {
                "type": "string"
            }
        }
    }
}

dummy_percolate_mappings = {
    "test-percolate-doc": {
        "properties": {
            "location": {
                "type": "geo_point"
            }
        }
    }
}

test_doc1 = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
}

test_doc2 = {
    'author': 'pydanny',
    'text': 'Cookiecutter: cool. bonsai cool.',
}


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

polygon_vertices = [[76.2960577, 9.9366668], [76.3041687, 9.947209], [76.3106918, 9.9546484], [76.3180733, 9.9646238], [76.326828, 9.9749371], [76.3343811, 9.9837284], [76.3453674, 9.9888002], [76.3573837, 9.9935338], [76.3680267, 9.9984364], [76.3807297, 10.0036771], [76.3893127, 10.0141581], [76.3946342, 10.0232865], [76.4001274, 10.0317384], [76.3929176, 10.0381618], [76.3846779, 10.0461063], [76.3747215, 10.0548957], [76.3651085, 10.0619946], [76.3556671, 10.0684174], [76.3451958, 10.0760231], [76.3371277, 10.0817695], [76.3316345, 10.0849807], [76.3185883, 10.0810934], [76.3106918, 10.0788963], [76.3043404, 10.0780512], [76.295929, 10.0773752], [76.2885475, 10.0773752], [76.2829686, 10.0771216], [76.2816811, 10.0663891], [76.2784195, 10.0576], [76.2739563, 10.0526983], [76.2705231, 10.0466133], [76.2701797, 10.0413734], [76.2700081, 10.0352882], [76.2700081, 10.0292029], [76.2705231, 10.0207508], [76.2713814, 10.013651], [76.272068, 10.0080724], [76.2724972, 10.0027473], [76.2683773, 9.9937029], [76.2711239, 9.9871942], [76.2737847, 9.9822914], [76.2764454, 9.9766277], [76.2785911, 9.9711331], [76.2809944, 9.9661455], [76.2835693, 9.9611578], [76.2875175, 9.9529576], [76.2944698, 9.9386703], [76.2960577, 9.9366668]]

query = {
    "query": {
        "filtered": {
            "query": {
                "match_all": {}
            },
            "filter": {
                "geo_polygon": {
                    "location": {
                        "points": polygon_vertices
                    }
                }
            }
        }
    }
}


def search_test_env(f):
    def wrap():
        es.indices.create(index='test-index')
        es.indices.put_mapping(index='test-index', doc_type='test-doc', body=dummy_mappings)
        es.index(index='test-index', doc_type='test-doc', body=test_doc1)
        try:
            f()
        except:
            es.indices.delete(index='test-index')
            raise
        else:
            es.indices.delete(index='test-index')
    return wrap


def percolate_test_env(f):
    def wrap():
        es.indices.create(index='test-percolate-index')
        es.indices.put_mapping(index='test-percolate-index', doc_type='test-percolate-doc', body=dummy_percolate_mappings)
        es.create(
            index='test-percolate-index',
            doc_type=".percolator",
            body=query
        )
        try:
            f()
        except:
            es.indices.delete(index='test-percolate-index')
            raise
        else:
            es.indices.delete(index='test-percolate-index')
    return wrap


@percolate_test_env
def test_percolate_and_get():
    results = percolate_and_get(es, d2, index='test-percolate-index', doc='test-percolate-doc')
    assert isinstance(results, list) == True


@search_test_env
def test_msearch():
    s = Msearch(es)
    s.add(q1, index='test-index', doc_type='test-doc')
    s.add(q2, index='test-index', doc_type='test-doc')
    results = s.execute()
    assert isinstance(results, list) == True
    for result in results:
        assert isinstance(result, dict) == True


@search_test_env
def test_msearch_index():
    s = Msearch(es, index='test-index')
    s.add(q1, doc_type='test-doc')
    s.add(q2, doc_type='test-doc')
    results = s.execute()
    assert isinstance(results, list) == True
    for result in results:
        assert isinstance(result, dict) == True


@percolate_test_env
def test_mpercolate():
    s = Mpercolate(es)
    s.add(d1, index='test-percolate-index', doc_type='test-percolate-doc')
    s.add(d1, index='test-percolate-index', doc_type='test-percolate-doc')
    results = s.execute()
    assert isinstance(results, list) == True
    for result in results:
        assert isinstance(result, dict) == True


@percolate_test_env
def test_mpercolate_index():
    s = Mpercolate(es, index='test-percolate-index')
    s.add(d1, doc_type='test-percolate-doc')
    s.add(d2, doc_type='test-percolate-doc')
    results = s.execute()
    assert isinstance(results, list) == True
    for result in results:
        assert isinstance(result, dict) == True


if __name__ == '__main__':
    pytest.main()
