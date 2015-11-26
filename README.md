# gambit
Micro library for performing multi-search queries on Elasticsearch using elasticseach-py


Example:

using Elasticsearch-py
```
from elasticsearch import Elasticsearch
from gambit import gambit

es = Elasticsearch()
q1 = {...}
q2 = {...}
q3 = {...}
query_function = gambit(es, 'index_name', 'document_name')
results = query_function(q1, q2, q3)

```  
