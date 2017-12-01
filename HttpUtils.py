# coding : utf-8
import httplib


class HttpUtils(object):
    ALIAS = '_aliases'

    @staticmethod
    def request(host,port, method_type, url, body):
        try:
            with httplib.HTTPConnection(host, port) as connection:
                connection.request(method=method_type, url=url, body=body)
                response = connection.getresponse()
                print 'status is : %s reason is %s' % (response.status, response.reason)
        except IOError, ex:
            print 'IO Exception +...%s' % str(ex.message)
        except Exception, ex:
            print 'ex' + str(ex.message)


