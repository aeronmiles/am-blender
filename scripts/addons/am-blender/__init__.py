from . import setup
from . import (convert, custom_prop, data_util,
               shader_util, object_prop, keymap)
from bpy.app.handlers import persistent
import bpy
from .std.meta import meta


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


packages = (convert, custom_prop, data_util, shader_util, object_prop,
            # ensure keymap is last
            keymap)


@persistent
def load_post_handler(arg):
    meta.load()


def register():
    for package in packages:
        package.register()

    bpy.app.handlers.load_post.append(load_post_handler)


def unregister():
    for package in reversed(packages):
        package.unregister()
        
    bpy.app.handlers.load_post.remove(load_post_handler)
