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


class AM_MT_Nav_Properties_Tab(Menu):
    bl_label = "Properties Tab"

    def draw(self, context):
        # L
        layout = self.layout
        pie = layout.menu_pie()
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.nav_properties_tab_tool")
        box.operator("amblender.nav_properties_tab_object")
        box.operator("amblender.nav_properties_tab_modifier")
        box.operator("amblender.nav_properties_tab_data")
        box.operator("amblender.nav_properties_tab_texture")
        box.operator("amblender.nav_properties_tab_material")
        box.operator("amblender.nav_properties_tab_render")

        # R
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.nav_properties_tab_output")
        box.operator("amblender.nav_properties_tab_scene")
        box.operator("amblender.nav_properties_tab_world")
        box.operator("amblender.nav_properties_tab_collection")
        box.operator("amblender.nav_properties_tab_constraint")
        box.operator("amblender.nav_properties_tab_physics")
        box.operator("amblender.nav_properties_tab_particle")
        box.operator("amblender.nav_properties_tab_view_layer")
        


def register():
    bpy.utils.register_class(AM_MT_Nav_Workspace_Pie)
    bpy.utils.register_class(AM_MT_Nav_Properties_Tab)


def unregister():
    bpy.utils.unregister_class(AM_MT_Nav_Workspace_Pie)
    bpy.utils.unregister_class(AM_MT_Nav_Properties_Tab)

if __name__ == "__main__":
    register()