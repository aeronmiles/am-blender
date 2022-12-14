# import typing
# from ...std.fn import as_iterable
# from bpy.types import (Object)

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

# Class to provide ops as extension methods
#     def __init__(self, objs: typing.Union['Object', typing.Iterable['Object']]) -> None:
#         self._objs = as_iterable(objs)


# def ops(objs: typing.Union['Object', typing.Iterable['Object']]) -> Ops:
#     return Ops(objs)


ops = Ops()
