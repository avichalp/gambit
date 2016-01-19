class Base(object):
    """
    Base class responsible for building
    generic queries
    """
    def __init__(self, es, *args, **kwargs):
        """
        :param es: object of class Elasticsearch from module elasticseach
        :param str index: name of the index which is to be queried
        :param str doc_type: name of the doc_type which is to be queried
        """
        self.index_name = kwargs.get('index')
        self.doc_type = kwargs.get('doc_type')
        self.es = es

    def _query_builder(self, *args, **kwargs):
        """ returns a tuple of index and doc-type name """
        if self.index_name and self.doc_type:
            index_name = self.index_name
            doc_type = self.doc_type
        elif self.index_name and not self.doc_type:
            index_name = self.index_name
            doc_type = kwargs.get('doc_type')
        elif not self.index_name and self.doc_type:
            index_name = kwargs.get('index')
            doc_type = self.doc_type
        else:
            index_name = kwargs.get('index')
            doc_type = kwargs.get('doc_type')

        if index_name is None or doc_type is None:
            raise Exception('index name or doctype missing')
        return index_name, doc_type


class Msearch(Base):
    """
    Class to build and execute
    multi search queries
    """

    def __init__(self, es, *args, **kwargs):
        """
        :param es: object of class Elasticsearch from module elasticseach
        :param str index: name of the index which is to be queried
        :param str doc_type: name of the doc_type which is to be queried
        """
        self.request_body = []
        super(Msearch, self).__init__(es, *args, **kwargs)

    def add(self, q, *args, **kwargs):
        """
        :param dict q: query in form of a dictionary which is to be added to be executed in parallel
        :param str index: name of the index which is to be queried
        :param str doc_type: name of the doc_type which is to be queried
        """
        index_name, doc_type = self._query_builder(*args, **kwargs)
        req_head = {'index': index_name, 'type': doc_type}
        self.request_body.extend([req_head, q])

    def execute(self):
        """
        This method actually queries on elasticsearch
        """
        return self.es.msearch(body=self.request_body).get('responses')


class Mpercolate(Base):
    """
    Class to build and ececute
    multi percolate queries
    """
    request_body = []

    def __init__(self, es, *args, **kwargs):
        """
        :param es: object of class Elasticsearch from module elasticseach
        :param str index: name of the index which is to be queried
        :param str doc_type: name of the doc_type which is to be queried
        """
        super(Mpercolate, self).__init__(es, *args, **kwargs)

    def add(self, d, *args, **kwargs):
        """
        :param dict d: doc in form of a dictionary which is to be percolated.
        :param str index: name of the index which is to be queried.
        :param str doc_type: name of the doc_type which is to be queried
        """
        index_name, doc_type = self._query_builder(*args, **kwargs)
        req_head = {'percolate' : {'index': index_name, 'type': doc_type}}
        self.request_body.extend([req_head, d])

    def execute(self):
        """
        This method actually queries on elasticsearch
        """
        return self.es.mpercolate(body=self.request_body).get('responses')


def percolate_and_get(es, percolate_body, *arg, **kwargs):
    """
    :param es: object of class Elasticsearch from module elasticseach.
    :param dict d: doc in form of a dictionary which is to be percolated.
    :param str index: name of the index which is to be queried.
    :param str doc_type: name of the doc_type which is to be queried.
    """
    index_name = kwargs.get('index')
    doc_name = kwargs.get('doc')
    result = []
    if index_name and doc_name:
        percolate_result = es.percolate(
            index=index_name,
            doc_type=doc_name,
            body=percolate_body
        )

        if percolate_result and percolate_result['matches']:
            for match in percolate_result['matches']:
                result.append(
                    es.get_source(
                        index=index_name,
                        doc_type=doc_name,
                        id=match['_id']
                    )
                )
        return result
    else:
        return []
