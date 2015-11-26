def gambit(es, index_name=None, doc_name=None):
    requests = []

    def f1(*args, **kwargs):
        for arg in args:
            req_head = {'index': index_name, 'type': doc_name}
            requests.extend([req_head, arg])
        return es.msearch(body=requests)

    def f2():
        pass

    def f3():
        pass

    if index_name and doc_name:
        return f1

    else:
        pass
