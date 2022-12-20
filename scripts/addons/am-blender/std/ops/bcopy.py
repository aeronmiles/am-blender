import os
import typing
import bpy
from bpy.types import *
from ..meta import meta
from .fn import *
from ..dtypes import *


class Copy:
    @staticmethod
    def transform(source_obj: 'Object', dest_obj: 'Object'):
        dest_obj.location = source_obj.location
        dest_obj.rotation_euler = source_obj.rotation_euler
        dest_obj.scale = source_obj.scale

    @staticmethod
    def collections(source_obj: 'Object', dest_obj: 'Object'):
        for c in source_obj.users_collection:
            c.objects.link(dest_obj)

    @staticmethod
    def childs(source_obj: 'Object', dest_obj: 'Object'):
        childs = source_obj.children
        for c in childs:
            c.parent = dest_obj
            c.matrix_parent_inverse = dest_obj.matrix_world.inverted()


copy = Copy()
