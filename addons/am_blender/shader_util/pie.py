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
        box.operator("amblender.su_enabled_backface_culling")
        box.operator("amblender.su_set_opaque")
        box.operator("amblender.su_set_material_lod0")
        box.operator("amblender.su_set_material_lod1")
        box.operator("amblender.su_rename_textures")
        box.operator("amblender.su_set_duplicate_materials_to_base_material")

        # R
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.su_disable_backface_culling")
        box.operator("amblender.su_set_alpha_blend")
        box.operator("amblender.su_disconnect_normal_map")
        box.operator("amblender.su_disconnect_gltf_occlusion_map")
        box.operator("amblender.select_eevee_material_output_nodes")


def register():
    bpy.utils.register_class(AM_MT_ShaderUtilPie)


def unregister():
    bpy.utils.unregister_class(AM_MT_ShaderUtilPie)


if __name__ == "__main__":
    register()
