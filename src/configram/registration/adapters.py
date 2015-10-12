# -*- coding: utf-8 -*-
from zope.interface import implementer
from .interfaces import IRegistryAdapter


@implementer(IRegistryAdapter)
class RegistryAdapter(object):
    pass
