# -*- coding: utf-8 -*-
from .interfaces import (
    IRegistry,
    IRegistryFactory,
    IRegistryAdapter,
    )
from .core import Registry
from .factories import RegistryFactory
from .adapters import RegistryAdapter


__all__ = [
    'RegistryFactory', 'RegistryAdapter', 'Registry',
    'IRegistryFactory', 'IRegistryAdapter', 'IRegistry',
    ]
