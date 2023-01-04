from typing import Iterable
from multipledispatch import dispatch


def as_iterable(obj) -> 'Iterable':
    if isinstance(obj, Iterable):
        return obj
    else:
        return (obj,)


def ensure_dir(path: str):
    import os
    path = os.path.dirname(path)
    if not os.path.exists(path):
        os.makedirs(path)


@dispatch(str, str, str)
def replace(haystack: str, needle: str, replacement: str) -> str:
    return haystack.replace(needle, replacement)


@dispatch(str, Iterable[str], str)
def replace(haystack: str, needle: Iterable[str], replacement: str) -> str:
    for n in needle:
        haystack = haystack.replace(n, replacement)
    return haystack
