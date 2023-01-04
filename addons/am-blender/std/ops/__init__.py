from .build import build
from .bcopy import copy
from .find import find
from .data import data
from .export import export
from .shader import shader
from .transform import transform

class Ops:
    build = build
    copy = copy
    find = find
    data = data
    export = export
    shader = shader
    transform = transform

ops = Ops()