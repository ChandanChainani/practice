# Implementation copied from xmlrpclib._Method
class _Method(object):
    """
    Provides a way to call HTTP APIs in RPC way.
    Supports "nested" methods (e.g. examples.getStateName)
    """

    def __init__(self, send, name):
        self.__send = send
        self.__name = name

    def __getattr__(self, name):
        return _Method(self.__send, '%s.%s' % (self.__name, name))

    def __call__(self, *args, **kwargs):
        if args:
            raise Exception("Args not supported. Pass only kwargs")

        return self.__send(self.__name, kwargs)
class A:
    def __getattr__(self, name):
        return _Method(lambda x, y: print(x, y), name)

a = A()
a.b.c.d.e(f = {})
