"""
d2lfg/__version__
=================

This file determines the currently running version of d2lfg.
"""

from importlib.metadata import version as _v

_module_name = __name__.split(".")[0]
__version__ = _v(_module_name)

del _v
del _module_name
