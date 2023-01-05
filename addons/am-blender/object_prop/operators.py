from ..std import *


class AM_OP_VisibleCamera_True(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_camera_true'
    bl_label = 'Camera Ray Visiblity : True'
    bl_description = 'Set Camera Ray Visiblity : True'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        return sel and any(not obj.visible_camera for obj in sel)

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_camera = True

        return {'FINISHED'}


class AM_OP_VisibleCamera_False(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_camera_false'
    bl_label = 'Camera Ray Visiblity : False'
    bl_description = 'Set Camera Ray Visiblity : False'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        return sel and any(obj.visible_camera for obj in sel)

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_camera = False

        return {'FINISHED'}


class AM_OP_VisibleDiffuse_True(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_diffuse_true'
    bl_label = 'Diffuse Ray Visiblity : True'
    bl_description = 'Set Diffuse Ray Visiblity : True'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        return sel and any(not obj.visible_diffuse for obj in sel)

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_diffuse = True

        return {'FINISHED'}


class AM_OP_VisibleDiffuse_False(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_diffuse_false'
    bl_label = 'Diffuse Ray Visiblity : False'
    bl_description = 'Set Diffuse Ray Visiblity : False'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        return sel and any(obj.visible_diffuse for obj in sel)

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_diffuse = False

        return {'FINISHED'}


class AM_OP_VisibleGlossy_True(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_glossy_true'
    bl_label = 'Glossy Ray Visiblity : True'
    bl_description = 'Set Glossy Ray Visiblity : True'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        return sel and any(not obj.visible_glossy for obj in sel)

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_glossy = True

        return {'FINISHED'}


class AM_OP_VisibleGlossy_False(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_glossy_false'
    bl_label = 'Glossy Ray Visiblity : False'
    bl_description = 'Set Glossy Ray Visiblity : False'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        return sel and any(obj.visible_glossy for obj in sel)

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_glossy = False

        return {'FINISHED'}


class AM_OP_VisibleTransmission_True(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_transmission_true'
    bl_label = 'Transmission Ray Visiblity : True'
    bl_description = 'Set Transmission Ray Visiblity : True'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        return sel and any(not obj.visible_transmission for obj in sel)

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_transmission = True

        return {'FINISHED'}


class AM_OP_VisibleTransmission_False(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_transmission_false'
    bl_label = 'Transmission Ray Visiblity : False'
    bl_description = 'Set Transmission Ray Visiblity : False'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        return sel and any(obj.visible_transmission for obj in sel)

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_transmission = False

        return {'FINISHED'}


class AM_OP_VisibleVolumeScatter_True(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_volume_scatter_true'
    bl_label = 'Volume Scatter Ray Visiblity : True'
    bl_description = 'Set Volume Scatter Ray Visiblity : True'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        return sel and any(not obj.visible_volume_scatter for obj in sel)

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_volume_scatter = True

        return {'FINISHED'}


class AM_OP_VisibleVolumeScatter_False(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_volume_scatter_false'
    bl_label = 'Volume Scatter Ray Visiblity : False'
    bl_description = 'Set Volume Scatter Ray Visiblity : False'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        return sel and any(obj.visible_volume_scatter for obj in sel)

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_volume_scatter = False

        return {'FINISHED'}


class AM_OP_VisibleShadow_True(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_shadow_true'
    bl_label = 'Shadow Ray Visiblity : True'
    bl_description = 'Set Shadow Ray Visiblity : True'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        return sel and any(not obj.visible_shadow for obj in sel)

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_shadow = True

        return {'FINISHED'}


class AM_OP_VisibleShadow_False(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_shadow_false'
    bl_label = 'Shadow Ray Visiblity : False'
    bl_description = 'Set Shadow Ray Visiblity : False'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        sel = context.selected_objects
        return sel and any(obj.visible_shadow for obj in sel)

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_shadow = False

        return {'FINISHED'}


class AM_OP_VisibleRaysAll_True(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_rays_all_true'
    bl_label = 'All Ray Visibility : True'
    bl_description = 'Set All Ray Visibility : True'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_camera = True
            obj.visible_diffuse = True
            obj.visible_glossy = True
            obj.visible_transmission = True
            obj.visible_volume_scatter = True
            obj.visible_shadow = True

        return {'FINISHED'}


class AM_OP_VisibleRaysAll_False(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_rays_all_false'
    bl_label = 'All Ray Visibility : False'
    bl_description = 'Set All Ray Visibility : False'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.visible_camera = False
            obj.visible_diffuse = False
            obj.visible_glossy = False
            obj.visible_transmission = False
            obj.visible_volume_scatter = False
            obj.visible_shadow = False

        return {'FINISHED'}


class AM_OP_VisibleViewport_True(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_viewport_true'
    bl_label = 'Viewport Visiblity : True'
    bl_description = 'Set Viewport Visiblity : True'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.hide_set(False)
            obj.hide_viewport = False

        return {'FINISHED'}


class AM_OP_VisibleViewport_False(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_viewport_false'
    bl_label = 'Viewport Visiblity : False'
    bl_description = 'Set Viewport Visiblity : False'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.hide_viewport = True

        return {'FINISHED'}


class AM_OP_VisibleRender_True(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_render_true'
    bl_label = 'Render Visiblity : True'
    bl_description = 'Set Render Visiblity : True'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.hide_render = False

        return {'FINISHED'}


class AM_OP_VisibleRender_False(bpy.types.Operator):
    bl_idname = 'amblender.op_visible_render_false'
    bl_label = 'Render Visiblity : False'
    bl_description = 'Set Render Visiblity : False'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.hide_render = True

        return {'FINISHED'}


class AM_OP_Selectable_True(bpy.types.Operator):
    bl_idname = 'amblender.op_selectable_true'
    bl_label = 'Selectable : True'
    bl_description = 'Set Selectable : True'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.hide_set(False)
            obj.hide_select = False

        return {'FINISHED'}


class AM_OP_Selectable_False(bpy.types.Operator):
    bl_idname = 'amblender.op_selectable_false'
    bl_label = 'Selectable : False'
    bl_description = 'Set Selectable : False'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        objs = context.selected_objects

        for obj in objs:
            obj.hide_select = True

        return {'FINISHED'}


classes = (AM_OP_VisibleCamera_True, AM_OP_VisibleCamera_False, AM_OP_VisibleDiffuse_True, AM_OP_VisibleDiffuse_False, AM_OP_VisibleGlossy_True, AM_OP_VisibleGlossy_False,
           AM_OP_VisibleTransmission_True, AM_OP_VisibleTransmission_False,
           AM_OP_VisibleVolumeScatter_True, AM_OP_VisibleVolumeScatter_False,
           AM_OP_VisibleShadow_True, AM_OP_VisibleShadow_False, 
           AM_OP_VisibleRaysAll_True, AM_OP_VisibleRaysAll_False,
           AM_OP_VisibleViewport_True, AM_OP_VisibleViewport_False,
           AM_OP_VisibleRender_True, AM_OP_VisibleRender_False, AM_OP_Selectable_True, AM_OP_Selectable_False)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
