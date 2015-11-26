def gambit(es, *args, **kwargs):
    requests = []
    index_name = kwargs.get('index_name')
    doc_name = kwargs.get('doc_name')

    def f1(*args, **kwargs):
        for arg in args:
            req_head = {'index': index_name, 'type': doc_name}
            requests.extend([req_head, arg])
        return es.msearch(body=requests).get('responses')

    def f2():
        pass

    def f3():
        pass

    if index_name and doc_name:
        return f1

    else:
        pass
