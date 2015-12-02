# gambit
A micro library for performing multi-search/multi-percolate queries on Elasticsearch using elasticseach-py

usage: `pip install gambit`

Example:

using with Elasticsearch-py (https://github.com/elastic/elasticsearch-py)
```
from elasticsearch import Elasticsearch
from gambit import Msearch

es = Elasticsearch()
q1 = {...}
q2 = {...}

search = Msearch(es)
search.add(q1, index='some-index-name', doc_type='some-doc-type')
search.add(q2, index='some-other-index', doc_type='some-other-doc-type')
results = search.execute()
```  
Full documentation at http://gambit.readthedocs.org/en/latest/

