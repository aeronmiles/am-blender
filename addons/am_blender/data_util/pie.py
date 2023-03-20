from ..std import *

bl_info = {
    "name": "Pie Data Utils",
    "description": "Data Utils",
    "author": "Aeron Miles",
    "version": (0, 1, 0),
    "blender": (2, 90, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
}

# TODO: Add shader editor select images context resizing
class AM_MT_DataUtilPie(Menu):
    bl_label = "Data Utils"

    def draw(self, context):
        # L
        layout = self.layout
        pie = layout.menu_pie()
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.du_set_diffuse_image_scale_2048")
        box.operator("amblender.du_set_diffuse_image_scale_1024")
        box.operator("amblender.du_set_diffuse_image_scale_512")
        box.operator("amblender.du_set_diffuse_image_scale_256")
        box.separator()
        box.operator("amblender.du_set_normal_image_scale_2048")
        box.operator("amblender.du_set_normal_image_scale_1024")
        box.operator("amblender.du_set_normal_image_scale_512")
        box.operator("amblender.du_set_normal_image_scale_256")
        box.separator()
        box.operator("amblender.du_set_rough_metallic_occ_image_scale_2048")
        box.operator("amblender.du_set_rough_metallic_occ_image_scale_1024")
        box.operator("amblender.du_set_rough_metallic_occ_image_scale_512")
        box.operator("amblender.du_set_rough_metallic_occ_image_scale_256")
        box.operator("amblender.du_set_rough_metallic_occ_image_scale_128")
        box.operator("amblender.du_set_rough_metallic_occ_image_scale_64")

        # R
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.du_unpack_images")
        box.operator("amblender.du_reset_scaled_images")


def register():
    bpy.utils.register_class(AM_MT_DataUtilPie)


def unregister():
    bpy.utils.unregister_class(AM_MT_DataUtilPie)


if __name__ == "__main__":
    register()
