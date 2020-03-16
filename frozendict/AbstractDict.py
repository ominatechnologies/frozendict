from __future__ import annotations

import abc


class AbstractDict(metaclass=abc.ABCMeta):
    pass


AbstractDict.register(dict)
