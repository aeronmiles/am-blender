from ..std import *


bl_info = {
    "name": "Pie Object Properties",
    "description": "Object Property Settings",
    "author": "Aeron Miles",
    "version": (0, 1, 0),
    "blender": (2, 90, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "Pie Menu"
}


class AM_MT_ObjectPropertiesPie(Menu):
    bl_label = "Object Properties"

    def draw(self, context):
        # L
        layout = self.layout
        pie = layout.menu_pie()
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5

        # box.operator("amblender.op_selectable_true")
        box.separator()
        # box.operator("amblender.op_visible_viewport_true")
        box.separator()
        box.operator("amblender.op_visible_render_true")
        box.separator()
        box.label(text="Ray Visibility")
        box.operator("amblender.op_visible_rays_all_true")
        box.separator(factor=0.5)
        box.operator("amblender.op_visible_camera_true")
        box.operator("amblender.op_visible_diffuse_true")
        box.operator("amblender.op_visible_glossy_true")
        box.operator("amblender.op_visible_transmission_true")
        box.operator("amblender.op_visible_volume_scatter_true")
        box.operator("amblender.op_visible_shadow_true")

        # R
        box = pie.split().column()
        row = box.row(align=True)
        row.scale_y = 1.5

        box.operator("amblender.op_selectable_false")
        # box.operator("amblender.op_visible_viewport_false")
        box.operator("amblender.op_visible_render_false")
        box.separator()
        box.label(text="Ray Visibility")
        box.operator("amblender.op_visible_rays_all_false")
        box.separator(factor=0.5)
        box.operator("amblender.op_visible_camera_false")
        box.operator("amblender.op_visible_diffuse_false")
        box.operator("amblender.op_visible_glossy_false")
        box.operator("amblender.op_visible_transmission_false")
        box.operator("amblender.op_visible_volume_scatter_false")
        box.operator("amblender.op_visible_shadow_false")


def register():
    bpy.utils.register_class(AM_MT_ObjectPropertiesPie)


def unregister():
    bpy.utils.unregister_class(AM_MT_ObjectPropertiesPie)


if __name__ == "__main__":
    register()
