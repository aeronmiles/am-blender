import os
from typing import Iterable


def as_iterable(obj) -> 'Iterable':
    if isinstance(obj, Iterable):
        return obj
    else:
        return (obj,)
    
def of_type(obj, type) -> 'Iterable':
    return (o for o in obj if o.type == type)


def ensure_dir(path: str) -> str:
    import os
    path = os.path.dirname(path)
    if not os.path.exists(path):
        os.makedirs(path)
    
    return path


# def ensure_non_existing(path: str) -> str:
#     dirname = os.path.dirname(path)
#     split = os.path.splitext(os.path.basename(path))
#     i = 0
#     while os.path.exists(path):
#         i += 1
#         path = os.path.join(dirname, f'{split[0]}({i}){split[1]}')

#     return path

def replace(haystack: str, needle: Iterable[str], replacement: str) -> str:
    for n in needle:
        haystack = haystack.replace(n, replacement)
    return haystack
