def gambit(es, *args, **kwargs):
    requests = []
    index_name = kwargs.get('index')
    doc_name = kwargs.get('doc')

    def f1(*args, **kwargs):
        for arg in args:
            req_head = {'index': index_name, 'type': doc_name}
            requests.extend([req_head, arg])
        return es.msearch(body=requests).get('responses')

    def f2(*args, **kwargs):
        for arg in args:
            req_head = {'index': index_name, 'type': arg[0]}
            requests.extend([req_head, arg[1]])
        return es.msearch(body=requests).get('responses')

    def f3(*args, **kwargs):
        for arg in args:
            req_head = {'index': arg[0], 'type': arg[1]}
            requests.extend([req_head, arg[2]])
        return es.msearch(body=requests).get('responses')

    if index_name and doc_name:
        return f1

    elif index_name:
        return f2

    else:
        return f3
