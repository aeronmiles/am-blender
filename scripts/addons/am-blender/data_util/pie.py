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


class AM_MT_DataUtilPie(Menu):
    bl_label = "Data Utils"

    def draw(self, context):
        # L
        layout = self.layout
        pie = layout.menu_pie()
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5

        # R
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5
        box.operator("amblender.data_util_unpack_images")
        box.operator("amblender.data_util_reset_scaled_images")
        box.operator("amblender.data_util_set_image_scale_2048")
        box.operator("amblender.data_util_set_image_scale_1024")
        box.operator("amblender.data_util_set_image_scale_512")


def register():
    bpy.utils.register_class(AM_MT_DataUtilPie)


def unregister():
    bpy.utils.unregister_class(AM_MT_DataUtilPie)


if __name__ == "__main__":
    register()
