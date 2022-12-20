import os
import typing
import bpy
from bpy.types import *
from ..meta import meta
from .fn import *
from ..dtypes import *


class Transform:
    @staticmethod
    def align(obj: 'Object', dest_obj: 'Object'):
        obj.location = dest_obj.location
        obj.rotation_euler = dest_obj.rotation_euler
        obj.scale = dest_obj.scale


transform = Transform()