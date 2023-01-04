from . import reload_addons

bl_info = {
    "name": "Reload Add-Ons",
    "description": "Reload all / enabled Add-Ons",
    "author": "Aeron Miles",
    "version": (1, 0, 1),
    "blender": (2, 90, 0),
    "location": "",
    "warning": "",
    "support": "COMMUNITY",
    "wiki_url": "",
    "tracker_url": "",
    "category": "System"
}

def register():
    reload_addons.register()


def unregister():
    reload_addons.unregister()
