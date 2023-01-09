from ..std import *


bl_info = {
    "name": "Import Export Pie",
    "description": "Import Export",
    "author": "Aeron Miles",
    "version": (0, 1, 0),
    "blender": (2, 90, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
}


class AM_MT_ImportExportPie(Menu):
    bl_label = "Import Export"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("amblender.export_batch_gltf_embedded")
        pie.operator("amblender.export_batch_gltf_separate")
        pie.operator("amblender.export_batch_glb")
        pie.operator("amblender.export_batch_usdz")


def register():
    bpy.utils.register_class(AM_MT_ImportExportPie)


def unregister():
    bpy.utils.unregister_class(AM_MT_ImportExportPie)


if __name__ == "__main__":
    register()
