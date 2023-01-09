from bpy.utils import register_class, unregister_class
from ..std import meta
from . import (
    # id,
    material
)

classes = (
    # id.AMBlenderIDProps,
    material.AMBlenderMaterialProps,
)


def register():
    for cls in classes:
        register_class(cls)


def unregister():
    for cls in classes:
        unregister_class(cls)
