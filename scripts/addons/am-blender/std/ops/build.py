import os
import typing
import bpy
from bpy.types import *
from ..meta import meta
from .fn import *
from ..dtypes import *


class Build:
    @staticmethod
    def empty_mesh(name: str = "EmptyMesh") -> 'Object':
        mesh = bpy.data.meshes.new('Empty.Mesh')
        mesh.from_pydata([], [], [])
        mesh.update()
        obj = bpy.data.objects.new('Empty.Mesh', mesh)
        obj.name = name
        return obj


build = Build()
