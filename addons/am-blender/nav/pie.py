from ..std import *


bl_info = {
    "name": "Pie Nav",
    "description": "Nav",
    "author": "Aeron Miles",
    "version": (0, 1, 0),
    "blender": (2, 90, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
}


class AM_MT_Nav_Workspace_Pie(Menu):
    bl_label = "Workspace"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("amblender.nav_workspace_modeling")
        pie.operator("amblender.nav_workspace_uv_editing")
        # pie.operator("amblender.nav_workspace_layout")
        pie.operator("amblender.nav_workspace_shading")
        pie.operator("amblender.nav_workspace_texture_paint")
        pie.operator("amblender.nav_workspace_sculpting")
        # pie.operator("amblender.nav_workspace_rendering")
        pie.operator("amblender.nav_workspace_assets")
        pie.operator("amblender.nav_workspace_geometry_nodes")
        pie.operator("amblender.nav_workspace_scripting")


def register():
    bpy.utils.register_class(AM_MT_Nav_Workspace_Pie)


def unregister():
    bpy.utils.unregister_class(AM_MT_Nav_Workspace_Pie)


if __name__ == "__main__":
    register()
