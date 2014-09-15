import sys

PY2 = sys.version_info[0] == 2

if PY2:
    from future_builtins import zip as izip, map as imap
    xrange = xrange
else:
    izip, imap, xrange = zip, map, range

if PY2:
    def iteritems(dict):
        return dict.iteritems()

    def itervalues(dict):
        return dict.itervalues()

else:
    def iteritems(dict):
        return iter(dict.items())

    def itervalues(dict):
        return iter(dict.values())

try:
    memoryview = memoryview
except NameError:
    # Python 2.6
    memoryview = buffer

def func_closure(func):
    if PY2:
        return func.func_closure
    else:
        return func.__closure__

def func_code(func):
    if PY2:
        return func.func_code
    else:
        return func.__code__

def im_func(method):
    if PY2:
        return method.im_func
    else:
        return method.__func__

def im_self(method):
    if PY2:
        return method.im_self
    else:
        return method.__self__

def im_class(method):
    if PY2:
        return method.im_class
    else:
        return method.__self__.__class__

try:
    import cPickle as pickle
except ImportError:
    import pickle

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

try:
    import builtins
except ImportError:
    import __builtin__ as builtins

def with_metaclass(metaclass, *bases):
    class Metaclass(metaclass):
        def __new__(cls, name, this_bases, d):
            return metaclass(name, bases, d)
    return type.__new__(Metaclass, 'temporary_class', (), {})

if PY2:
    exec("""def reraise(exc_class, exc, tb=None): 
    raise exc_class, exc, tb
""")
else:
    def reraise(exc_class, exc, tb=None):
        if exc is None:
            exc = exc_class()
        if exc.__traceback__ is not tb:
            raise exc.with_traceback(tb)
        raise exc