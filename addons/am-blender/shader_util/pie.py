from ..std import *


bl_info = {
    "name": "Pie Shader Utils",
    "description": "Shader Utils",
    "author": "Aeron Miles",
    "version": (0, 1, 0),
    "blender": (2, 90, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
}


class AM_MT_ShaderUtilPie(Menu):
    bl_label = "Shader Utils"

    def draw(self, context):
        # L
        layout = self.layout
        pie = layout.menu_pie()
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.shader_util_enabled_backface_culling")
        box.operator("amblender.shader_util_disable_backface_culling")
        box.operator("amblender.shader_util_set_opaque")
        box.operator("amblender.shader_util_set_alpha_blend")

        # R
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.shader_util_disconnect_normal_map")
        box.operator("amblender.shader_util_disconnect_gltf_occlusion_map")


def register():
    bpy.utils.register_class(AM_MT_ShaderUtilPie)


def unregister():
    bpy.utils.unregister_class(AM_MT_ShaderUtilPie)


if __name__ == "__main__":
    register()
