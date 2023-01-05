from .build import build
from .bcopy import copy
from .data import data
from .import_export import io
from .find import find
from .nav import nav
from .shader import shader
from .transform import transform

class Ops:
    build = build
    copy = copy
    data = data
    find = find
    io = io
    nav = nav
    shader = shader
    transform = transform

ops = Ops()