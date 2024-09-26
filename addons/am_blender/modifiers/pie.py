from ..std import *

bl_info = {
    "name": "Pie Modifiers",
    "description": "Modifiers",
    "author": "Aeron Miles",
    "version": (0, 1, 0),
    "blender": (2, 90, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
}

class AM_MT_ModifiersPie(Menu):
    bl_label = "Modifiers"

    def draw(self, context):
        # L
        layout = self.layout
        pie = layout.menu_pie()
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.op_modifiers_disable")
        # R
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.op_modifiers_enable")


def register():
    bpy.utils.register_class(AM_MT_ModifiersPie)


def unregister():
    bpy.utils.unregister_class(AM_MT_ModifiersPie)


if __name__ == "__main__":
    register()
