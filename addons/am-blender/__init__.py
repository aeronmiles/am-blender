from . import packages
from . import (convert, custom_prop, data_util, import_export,
               shader_util, object_prop, keymap, util)
from bpy.app.handlers import persistent
import bpy
from .std.meta import meta


# type: ignore
bl_info = {
    "name": "AM Blender",
    "author": "Aeron Miles",
    "version": (1, 0, 1),
    "blender": (2, 90, 0),
    "location": "See keymap",
    "description": "Blender tools, scripts & presets.",
    "warning": "",
    "doc_url": "",
    "category": "3D"
}


modules = (convert, custom_prop, data_util, import_export, shader_util, object_prop,
           util,
           # ensure keymap is last
           keymap)


@persistent
def load_post_handler(arg):
    meta.load()


def register():
    for mod in modules:
        mod.register()

    bpy.app.handlers.load_post.append(load_post_handler)


def unregister():
    for mod in reversed(modules):
        mod.unregister()

    bpy.app.handlers.load_post.remove(load_post_handler)