# -*- coding: utf-8 -*-
import os.path
import inspect
from logging import getLogger
import zope.dottedname.resolve


_logger = getLogger(__name__)


def get_caller_module(depth=1):
    """Return caller module
    """
    frame = inspect.currentframe()
    for ii in range(depth):
        frame = frame.f_back

    dotted = frame.f_globals['__name__']
    fromlist = []
    if dotted.count('.') > 0:  # sub module or sub package
        fromlist = '.'.join(dotted.split('.')[:-1])

    try:
        module = __import__(dotted, globals={}, locals={}, fromlist=fromlist)
    except ImportError:  # pragma: no cover
        raise

    path = module.__file__
    dirpath = os.path.dirname(path)
    return dotted, module, path, dirpath


def normalize_dotted_name(rel, current):
    """Convert relelative dotted name to abs dotted name

    >>> normalize_dotted_name('...p', 'a.b.c.d.e')
    'a.b.c.p'
    """
    modules = current.split('.')
    modules.append('.')
    if modules[0] == '__main__':
        _logger.error('__main__ package!!')

    if rel.startswith('.'):
        while rel.startswith('.'):
            rel = rel[1:]
            modules = modules[:-1]
    else:
        modules = []
    modules.append(rel)
    abs_dotted_name = '.'.join(modules)
    abs_dotted_name = (
        abs_dotted_name[1:]
        if abs_dotted_name.startswith('.') else abs_dotted_name)
    return abs_dotted_name.strip('.')


def get_abs_dotted_name_caller_module(name, depth=3):
    dotted, module, path, module_dir = get_caller_module(depth=depth)
    return normalize_dotted_name(name, dotted)


def get_includeme(name, target='includeme', resolve=None, depth=0):
    if resolve is None:
        resolve = zope.dottedname.resolve.resolve

    if callable(name):
        return name

    dotted, module, path, module_dir = get_caller_module(depth=depth)
    abs_dotted_name = normalize_dotted_name(name, dotted)
    module = resolve(abs_dotted_name)
    includeme = getattr(module, target)

    return includeme
