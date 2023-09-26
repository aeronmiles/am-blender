from ..std import *

bl_info = {
    "name": "Pie View",
    "description": "View",
    "author": "Aeron Miles",
    "version": (0, 1, 0),
    "blender": (2, 90, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
}

class AM_MT_ViewPie(Menu):
    bl_label = "View"

    def draw(self, context):
        # L
        layout = self.layout
        pie = layout.menu_pie()
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.v_show_colliders")

        # R
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.v_hide_colliders")
        


def register():
    bpy.utils.register_class(AM_MT_ViewPie)


def unregister():
    bpy.utils.unregister_class(AM_MT_ViewPie)


if __name__ == "__main__":
    register()
