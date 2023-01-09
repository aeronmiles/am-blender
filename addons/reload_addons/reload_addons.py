import bpy
import os
import addon_utils
from loguru import logger as log

bl_info = {
    "name": "Reload Addons",
    "author": "Aeron Miles",
    "version": (1, 0, 1),
    "blender": (2, 90, 0),
    "location": "SpaceBar Search -> Reload All Addons",
    "category": "Development",
}

# TODO: test bpy.script.reload_scripts()
def reload_addons():
    # Get the path to the user's addons directory
    user_addons_path = bpy.utils.user_resource('SCRIPTS', path="addons")

    for dir in os.listdir(user_addons_path):
        # Check if the current addon is enabled and not this
        check = addon_utils.check(dir)
        if check and not check[1] or 'reload_addons' in dir:
            continue

        log.info(f"Reloading {dir}")
        # If it is, disable the addon
        bpy.ops.preferences.addon_disable(module=dir)
        # # Re-enable the addon, which will trigger a reload
        bpy.ops.preferences.addon_enable(module=dir)

    # Update the list of available addons
    bpy.ops.preferences.addon_refresh()


class ReloadEnabledAddons(bpy.types.Operator):
    """Reload Addons"""
    bl_idname = "reload_addons.enabled"
    bl_label = "Reload Enabled Addons"

    def execute(self, context):
        reload_addons()
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ReloadEnabledAddons)


def unregister():
    bpy.utils.unregister_class(ReloadEnabledAddons)
