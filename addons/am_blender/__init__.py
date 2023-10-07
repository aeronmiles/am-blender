from . import packages
from . import (convert, build, custom_prop, data_util, modifiers, nav, import_export,
               shader_util, object_prop, properties, keymap, util, view, std)
from bpy.app.handlers import persistent
import bpy
from .std.meta import meta


# type: ignore
bl_info = {
    "name": "AM Blender",
    "author": "Aeron Miles",
    "version": (1, 0, 3),
    "blender": (2, 90, 0),
    "location": "See keymap",
    "description": "Blender tools, scripts & presets.",
    "warning": "",
    "doc_url": "",
    "category": "3D"
}


modules = (convert, build, custom_prop, data_util, import_export, shader_util, object_prop,
           util, modifiers, nav, properties,view, std,
           # ensure keymap is last
           keymap)


@persistent
def load_post_handler(arg):
    meta.load()
    # bpy.ops.wm.console_toggle()


def register():
    for m in modules:
        m.register()

    bpy.app.handlers.load_post.append(load_post_handler)


def unregister():
    for m in reversed(modules):
        m.unregister()

    bpy.app.handlers.load_post.remove(load_post_handler)


if __name__ == "__main__":
    register()
