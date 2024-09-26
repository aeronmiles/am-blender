from .build import build
from .bcopy import copy
from .data import data
from .geo import geo
from .import_export import io
from .find import find
from .modifier import modifier
from .shader import shader
from .transform import transform
from .select import select


class Ops:
    build = build
    copy = copy
    data = data
    geo = geo
    find = find
    io = io
    modifier = modifier
    shader = shader
    transform = transform
    select = select

ops = Ops()
