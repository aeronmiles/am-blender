from ..std import *


bl_info = {
    "name": "Pie Convert",
    "description": "Convert",
    "author": "Aeron Miles",
    "version": (0, 1, 0),
    "blender": (2, 90, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
}


class AM_MT_ConvertPie(Menu):
    bl_label = "Convert"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("amblender.convert_to_empty_mesh")
        pie.operator("amblender.deselect_non_mesh_objects")
        pie.operator("amblender.parent_in_place")
        pie.operator("amblender.reset_parent_transform")
        pie.operator("amblender.duplicate_active_to_others")
        pie.operator("amblender.pivots_to_active")


def register():
    bpy.utils.register_class(AM_MT_ConvertPie)


def unregister():
    bpy.utils.unregister_class(AM_MT_ConvertPie)


if __name__ == "__main__":
    register()
