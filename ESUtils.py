# coding : utf-8

from HttpUtils import HttpUtils
from LoggerWrapper import LoggerWrapper


class ESUtils(object):
    def __init__(self, host='127.0.0.1', port=9200):
        self.host = host
        self.port = port

    ALIAS = '_aliases'

    def update_alias(self, index_name, alias):
        msg_body = '{"actions" : [{ "add" : { "index" : "%s","alias" : "%s" } }]}' % (index_name, alias)
        HttpUtils.request('POST', self.ALIAS, msg_body)

    @LoggerWrapper.log
    def test_method(self):
        print 11

    def is_index_exists(self, index_name):
        """
        判断索引是否存在
        :param index_name:
        :return:
        """
        response = HttpUtils.request(method='GET', url=index_name)
        code = response.status
        print '[index] %s  exist http code is %s' % (index_name, code)
        return int(code) != 404


