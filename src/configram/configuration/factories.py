# -*- coding: utf-8 -*-
from zope.interface import implementer
from .core import PackageConfigurator
from .interfaces import IConfiguratorFactory
from .interfaces import IConfigurator


@implementer(IConfiguratorFactory)
class ConfiguratorFactory(object):
    def __init__(self, registry, factory=None):
        self._factory = factory if factory else PackageConfigurator
        self._core = registry

    def __call__(self, name='', *args, **kwds):
        obj = self._core.queryUtility(IConfigurator, name)
        if obj is None:
            obj = self._factory(*args, **kwds)
            self._core.registerUtility(obj, IConfigurator, name)
        return self._core.queryUtility(IConfigurator, name)
