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


if __name__ == "__main__":
    tool = ESUtils()
    tool.test_method("aa")
