# -*- coding: utf-8 -*-
import six
from logging import getLogger as get_logger
from zope.interface import implementer
from zope.interface.registry import Components
from .interfaces import IConfigurator
from .utils import (
    get_includeme,
    get_abs_dotted_name_caller_module,
    )


_logger = get_logger(__name__)


@implementer(IConfigurator)
class PackageConfigurator(object):
    default_depth = 3

    def __init__(self, registry, resolve=None, target='includeme'):
        self.registry = registry
        self._resolve = resolve
        self._target = target
        self._depth = self.default_depth
        self._configurator_registry = Components()

    def add_configurator(self, configurator, name=''):
        self._configurator_registry.registerUtility(configurator, IConfigurator, name)

    def include(self, name, *args, **kwargs):
        _logger.debug('start include: name=%s, args=%s, kwds=%s', name, args, kwargs)
        includeme = name if callable(name) else get_includeme(name, resolve=self._resolve, depth=self._depth)
        _logger.debug('include -> %s.%s', includeme.__module__, includeme.__name__)
        return includeme(self)

    def scan(self, package=None, **kw):
        name = 'scan'
        if package is None:
            package = '.'

        if isinstance(package, (six.string_types, six.text_type, six.binary_type)):
            package = get_abs_dotted_name_caller_module(package, **kw)

        for cfg in self._configurator_registry.getAllUtilitiesRegisteredFor(IConfigurator):
            if hasattr(cfg, name) and callable(getattr(cfg, name)):
                _logger.debug('scanning...: %s: %s', cfg.__module__, package)
                cfg.scan(package)

    def __getattr__(self, name):
        if name.startswith('_'):
            raise AttributeError(name)

        configs = [cfg
                   for cfg in self._configurator_registry.getAllUtilitiesRegisteredFor(IConfigurator)
                   if hasattr(cfg, name) and callable(getattr(cfg, name))]

        if configs:
            for config in configs:
                return getattr(config, name)
        else:
            raise AttributeError(name)
