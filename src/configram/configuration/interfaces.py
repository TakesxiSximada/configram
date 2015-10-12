# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope.component.interfaces import (
    IFactory,
    IComponents,
    )


class IConfiguratorFactory(IFactory):
    pass


class IConfigurator(IComponents):
    pass


class IConfiguratorAdapter(Interface):
    pass
