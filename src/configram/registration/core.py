# -*- coding: utf-8 -*-
from zope.interface import implementer
from zope.interface.registry import Components
from .interfaces import IRegistry


@implementer(IRegistry)
class Registry(Components):
    pass
