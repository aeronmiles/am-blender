import os
import sys
import functools as ft
import itertools as it
from .log import log
import bpy
import mathutils

# std modules last
from .types import *
from .fn import *
from .dec import dec
from .meta import meta
from .ui import ui
from .ops import ops


modules = (ui,)


def register():
    for m in modules:
        m.register()

def unregister():
    for m in modules:
        m.unregister()