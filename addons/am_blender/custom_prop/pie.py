from ..std import *


bl_info = {
    "name": "Pie Add/Remove Custom Properties",
    "description": "Add/Remove Custom Properties",
    "author": "Aeron Miles",
    "version": (0, 1, 0),
    "blender": (2, 90, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
}


class AM_MT_CustomPropPie(Menu):
    bl_label = "Custom Properties"

    def draw(self, context):
        # L
        layout = self.layout
        pie = layout.menu_pie()
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.cp_add_gl_separate_culling_pass")
        box.operator("amblender.cp_add_gl_translucency")
        box.operator("amblender.cp_add_gl_blend_multiply")
        box.operator("amblender.cp_add_gl_vertex_color_metallic_roughness")
        box.operator("amblender.cp_add_gl_lightmap")
        box.operator("amblender.cp_add_gl_alpha_index")
        box.separator()
        box.operator("amblender.cp_add_collider")

        # R
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.cp_remove_gl_separate_culling_pass")
        box.operator("amblender.cp_remove_gl_translucency")
        box.operator("amblender.cp_remove_gl_blend_multiply")
        box.operator("amblender.cp_remove_gl_vertex_color_metallic_roughness")
        box.operator("amblender.cp_remove_gl_lightmap")
        box.operator("amblender.cp_remove_gl_alpha_index")
        box.separator()
        box.operator("amblender.cp_remove_collider")


def register():
    bpy.utils.register_class(AM_MT_CustomPropPie)


def unregister():
    bpy.utils.unregister_class(AM_MT_CustomPropPie)


if __name__ == "__main__":
    register()
