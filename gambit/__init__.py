class Gambit(object):

    def __init__(self, es):
        self.requests = []
        self.es = es

    def search(self, *args, **kwargs):
        index_name = kwargs.get('index')
        doc_name = kwargs.get('doc')
        req_body = []

        if index_name and doc_name:
            for arg in args:
                req_head = {'index': index_name, 'type': doc_name}
                req_body.extend([req_head, arg])
            return self.es.msearch(body=req_body).get('responses')

        elif index_name:
            for arg in args:
                req_head = {'index': index_name, 'type': arg[0]}
                req_body.extend([req_head, arg[1]])
            return self.es.msearch(body=req_body).get('responses')

        else:
            for arg in args:
                req_head = {'index': arg[0], 'type': arg[1]}
                req_body.extend([req_head, arg[2]])
            return self.es.msearch(body=req_body).get('responses')

    def get(self, *args, **kwargs):
        index_name = kwargs.get('index')
        doc_name = kwargs.get('doc')
        req_body = []

        if index_name and doc_name:
            ids = []
            for arg in args:
                ids.append(arg)
            self.requests  = {'ids': ids}
            return self.es.mget(index=index_name, doc_type=doc_name, body=self.requests).get('docs')

        elif index_name:
            for arg in args:
                req_body.append({
                    '_type': arg[0],
                    '_id': arg[1]
                })
            self.requests = {'docs': req_body}
            return self.es.mget(index=index_name, body=self.requests).get('docs')

        else:
            for arg in args:
                req_body.append({
                    '_index': arg[0],
                    '_type': arg[1],
                    '_id': arg[2]
                })
            self.requests = {'docs': req_body}
            return self.es.mget(body=self.requests).get('docs')

    def percolate(self, *args, **kwargs):
        index_name = kwargs.get('index')
        doc_name = kwargs.get('doc')
        if index_name and doc_name:
            req_body = []
            for arg in args:
                req_head = {'percolate': {'index': index_name, 'type': doc_name}}
                req_body.extend([req_head, arg])
            return self.es.mpercolate(body=req_body).get('responses')

        elif index_name:
            req_body = []
            for arg in args:
                req_head = {'percolate' : {'index': index_name, 'type': arg[0]}}
                req_body.extend([req_head, arg[1]])
            return self.es.mpercolate(body=req_body).get('responses')

        else:
            req_body = []
            for arg in args:
                req_head = {'percolate' : {'index': arg[0], 'type': arg[1]}}
                req_body.extend([req_head, arg[2]])
            return self.es.mpercolate(body=req_body).get('responses')

    def percolate_and_get(self, percolate_body, *arg, **kwargs):
        index_name = kwargs.get('index')
        doc_name = kwargs.get('doc')
        result = []
        if index_name and doc_name:
            percolate_result = self.es.percolate(
                index=index_name,
                doc_type=doc_name,
                body=percolate_body
            )

            if percolate_result and percolate_result['matches']:
                for match in percolate_result['matches']:
                    result.append(
                        self.es.get_source(
                            index=index_name,
                            doc_type=doc_name,
                            id=match['_id']
                        )
                    )
                return result

            else:
                return []
