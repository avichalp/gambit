class Gambit(object):

    def __init__(self, es):
        self.requests = []
        self.es = es

    def search(self, *args, **kwargs):
        index_name = kwargs.get('index')
        doc_name = kwargs.get('doc')

        def f1(*args, **kwargs):
            for arg in args:
                req_head = {'index': index_name, 'type': doc_name}
                self.requests.extend([req_head, arg])
            return self.es.msearch(body=self.requests).get('responses')

        def f2(*args, **kwargs):
            for arg in args:
                req_head = {'index': index_name, 'type': arg[0]}
                self.requests.extend([req_head, arg[1]])
            return self.es.msearch(body=self.requests).get('responses')

        def f3(*args, **kwargs):
            for arg in args:
                req_head = {'index': arg[0], 'type': arg[1]}
                self.requests.extend([req_head, arg[2]])
            return self.es.msearch(body=self.requests).get('responses')

        if index_name and doc_name:
            return f1

        elif index_name:
            return f2

        else:
            return f3


    def get(self, *args, **kwargs):
        index_name = kwargs.get('index')
        doc_name = kwargs.get('doc')

        def f1(*args, **kwargs):
            ids = []
            for arg in args:
                ids.append(arg)
            self.requests  = {'ids': ids}
            return self.es.mget(index=index_name, doc_type=doc_name, body=self.requests).get('docs')

        def f2(*args, **kwrgs):
            req_body = []
            for arg in args:
                req_body.append({
                    '_type': arg[0],
                    '_id': arg[1]
                })
            self.requests = {'docs': req_body}
            return self.es.mget(index=index_name, body=self.requests).get('docs')

        def f3(*args, **kwargs):
            req_body = []
            for arg in args:
                req_body.append({
                    '_index': arg[0],
                    '_type': arg[1],
                    '_id': arg[2]
                })
            self.requests = {'docs': req_body}
            return self.es.mget(body=self.requests).get('docs')

        if index_name and doc_name:
            return f1
        elif index_name:
            return f2
        else:
            return f3
