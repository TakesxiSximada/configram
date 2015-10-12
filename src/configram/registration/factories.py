# -*- coding: utf-8 -*-
from zope.interface import implementer
from .core import Registry
from .interfaces import IRegistryFactory
from .interfaces import IRegistry


@implementer(IRegistryFactory)
class RegistryFactory(object):
    def __init__(self, registry_factory=None):
        self._registry_factory = registry_factory if registry_factory else Registry
        self._core = Registry()

    def __call__(self, name='', *args, **kwds):
        registry = self._core.queryUtility(IRegistry, name)
        if registry is None:
            registry = self._registry_factory(name, *args, **kwds)
            self._core.registerUtility(registry, IRegistry, name)
        return self._core.queryUtility(IRegistry, name)
