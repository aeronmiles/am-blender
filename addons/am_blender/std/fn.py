from ..std import *
import os
from typing import Iterable, Union


def as_iterable(obj) -> Iterable:
    if isinstance(obj, Iterable) and not isinstance(obj, str) and not isinstance(obj, bytes):
        return obj
    else:
        return (obj,)
    
def of_type(obj, type) -> Iterable:
    return [o for o in obj if o.type == type]

def ensure_dir(path: str) -> str:
    path = os.path.dirname(path)
    if not os.path.exists(path):
        os.makedirs(path)
    
    return path

def replace(haystack: str, needle: Iterable[str], replacement: str) -> str:
    for n in needle:
        haystack = haystack.replace(n, replacement)
    return haystack
