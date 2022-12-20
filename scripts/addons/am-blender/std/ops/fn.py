from typing import Iterable


def as_iterable(obj) -> 'Iterable':
    if isinstance(obj, Iterable):
        return obj
    else:
        return (obj,)