from .build import build
from .bcopy import copy
from .data import data
from .export import export
from .find import find
from .nav import nav
from .shader import shader
from .transform import transform

class Ops:
    build = build
    copy = copy
    data = data
    find = find
    export = export
    nav = nav
    shader = shader
    transform = transform

ops = Ops()