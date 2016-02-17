# Gambit
A micro library for performing multi-search/multi-percolate queries on Elasticsearch using elasticseach-py

[![Build Status](https://travis-ci.org/avichalp/gambit.svg?branch=master)](https://travis-ci.org/avichalp/gambit)

#### Installation
`pip install gambit`

#### API

Let queries be expressed in the form of python dictionaries.
```
query1 = {...}
query2 = {...}
query3 = {...}

document1 = {...}
```
<br>
###### `Msearch`
To perform a multisearch use `Msearch` class<br>
```
from elasticsearch import Elasticsearch
from gambit import Msearch
search = Msearch(Elasticsearch(), index='some-index', doc-type='some-doc-type')
```
Use `add` method of `Msearch` class to build a query.
```
search.add(query1)
search.add(query2)
search.add(query3)
```
Use `execute` method of `Msearch` class to fire the aggregated query.
``` 
list_of_results = search.execute()
```
<br>
###### `percolate_and_get`

Use `percolate_and_get` function to percolate and fetch all matching documents.
```
matching_docs = precolate_and_get(Elasticsearch(), document1,
                                    index='some-index', doc-type='some-doc-type')
```

### Docs
Look at full documentation [here](http://gambit.readthedocs.org/en/latest/)

