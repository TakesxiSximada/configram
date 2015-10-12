# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope.component.interfaces import (
    IFactory,
    IComponents,
    )


class IRegistryFactory(IFactory):
    pass


class IRegistry(IComponents):
    pass


class IRegistryAdapter(Interface):
    pass
