# -*- coding: utf-8 -*-
from zope.interface import implementer
from .interfaces import IConfiguratorAdapter


@implementer(IConfiguratorAdapter)
class ConfiguratorAdapter(object):
    pass
