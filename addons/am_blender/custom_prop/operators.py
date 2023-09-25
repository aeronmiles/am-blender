from ..std import *


class AM_CP_Add_GL_SeaparateCullingPass(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_separate_culling_pass'
    bl_label = 'Add ::  gl_separate_culling_pass'
    bl_description = 'Add Custom Property ::  gl_separate_culling_pass'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not len(ops.data.with_custom_property(context.selected_objects, 'gl_separate_culling_pass')) == len(context.selected_objects)

    def execute(self, context):
        ops.data.set_custom_property(
            context.selected_objects, 'gl_separate_culling_pass', 1.0)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_GL_SeaparateCullingPass(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_separate_culling_pass'
    bl_label = 'Remove ::  gl_separate_culling_pass'
    bl_description = 'Remove Custom Property ::  gl_separate_culling_pass'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and ops.data.with_custom_property(context.selected_objects, 'gl_separate_culling_pass')

    def execute(self, context):
        ops.data.remove_custom_property(
            context.selected_objects, 'gl_separate_culling_pass')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Add_GL_AlphaIndex(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_alpha_index'
    bl_label = 'Add ::  gl_alpha_index'
    bl_description = 'Add Custom Property ::  gl_alpha_index'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not len(ops.data.with_custom_property(context.selected_objects, 'gl_alpha_index')) == len(context.selected_objects)

    def execute(self, context):
        ops.data.set_custom_property(
            context.selected_objects, 'gl_alpha_index', -10)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_GL_AlphaIndex(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_alpha_index'
    bl_label = 'Remove ::  gl_alpha_index'
    bl_description = 'Remove Custom Property ::  gl_alpha_index'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and ops.data.with_custom_property(context.selected_objects, 'gl_alpha_index')

    def execute(self, context):
        ops.data.remove_custom_property(
            context.selected_objects, 'gl_alpha_index')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Add_GL_DepthPrePass(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_depth_pre_pass'
    bl_label = 'Add ::  gl_depth_pre_pass'
    bl_description = 'Add Custom Property ::  gl_depth_pre_pass'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not len(ops.data.with_custom_property(context.selected_objects, 'gl_depth_pre_pass')) == len(context.selected_objects)

    def execute(self, context):
        ops.data.set_custom_property(
            context.selected_objects, 'gl_depth_pre_pass', 1.0)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_GL_DepthPrePass(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_depth_pre_pass'
    bl_label = 'Remove ::  gl_depth_pre_pass'
    bl_description = 'Remove Custom Property ::  gl_depth_pre_pass'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and ops.data.with_custom_property(context.selected_objects, 'gl_depth_pre_pass')

    def execute(self, context):
        ops.data.remove_custom_property(
            context.selected_objects, 'gl_depth_pre_pass')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}

class AM_CP_Add_GL_Translucency(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_translucency'
    bl_label = 'Add ::  gl_translucency'
    bl_description = 'Add Custom Property ::  gl_translucency'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not len(ops.data.with_custom_property(context.selected_objects, 'gl_translucency')) == len(context.selected_objects)

    def execute(self, context):
        ops.data.set_custom_property(
            context.selected_objects, 'gl_translucency', 1.0)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_GL_Translucency(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_translucency'
    bl_label = 'Remove ::  gl_translucency'
    bl_description = 'Remove Custom Property ::  gl_translucency'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and ops.data.with_custom_property(context.selected_objects, 'gl_translucency')

    def execute(self, context):
        ops.data.remove_custom_property(
            context.selected_objects, 'gl_translucency')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Add_GL_BlendMultiply(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_blend_multiply'
    bl_label = 'Add ::  gl_blend_multiply'
    bl_description = 'Add Custom Property ::  gl_blend_multiply'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not len(ops.data.with_custom_property(context.selected_objects, 'gl_blend_multiply')) == len(context.selected_objects)

    def execute(self, context):
        ops.data.set_custom_property(
            context.selected_objects, 'gl_blend_multiply', 1.0)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_GL_BlendMultiply(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_blend_multiply'
    bl_label = 'Remove ::  gl_blend_multiply'
    bl_description = 'Remove Custom Property ::  gl_blend_multiply'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and ops.data.with_custom_property(context.selected_objects, 'gl_blend_multiply')

    def execute(self, context):
        ops.data.remove_custom_property(
            context.selected_objects, 'gl_blend_multiply')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


# @TODO: move implementation
class AM_CP_Add_GL_VertexColorMetallicRougness(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_vertex_color_metallic_roughness'
    bl_label = 'Add ::  gl_vertex_color_metallic_roughness'
    bl_description = 'Add Custom Property ::  gl_vertex_color_metallic_roughness'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        l = len(context.selected_objects)
        return context.selected_objects and not len(ops.data.with_custom_property(context.selected_objects, 'gl_vertex_color')) == l and not len(ops.data.with_custom_property(context.selected_objects, 'gl_metallic_roughness')) == l

    def execute(self, context):
        objs = of_type(context.selected_objects, 'MESH')
        for obj in objs:
            colors = obj.data.color_attributes
            # context.view_layer.objects.active = obj
            # index = colors.active_color_index

            if colors.find("gl_color") == -1:
                colors.new(name="gl_color",
                            type="FLOAT_COLOR", domain="POINT")
                obj['gl_vertex_color'] = colors.find('gl_color')

            if colors.find("gl_metallic_roughness") == -1:
                colors.new(name="gl_metallic_roughness",
                            type="FLOAT_COLOR", domain="POINT")
                ops.data.set_custom_property(
                    obj, 'gl_vertex_metallic_roughness', colors.find('gl_metallic_roughness'))

            # bpy.ops.geometry.color_attribute_render_set(name="gl_color")
            # colors.active_color_index = index

        ops.ui.redraw(SpaceType.PROPERTIES)
        # context.view_layer.objects.active = active
        return {'FINISHED'}


# @TODO: move implementation
class AM_CP_Remove_GL_VertexColorMetallicRougness(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_vertex_color_metallic_roughness'
    bl_label = 'Remove ::  gl_vertex_color_metallic_roughness'
    bl_description = 'Remove Custom Property ::  gl_vertex_color_metallic_roughness'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and ops.data.with_custom_property(context.selected_objects, 'gl_vertex_metallic_roughness') and ops.data.with_custom_property(context.selected_objects, 'gl_vertex_color')

    def execute(self, context):
        objs = context.selected_objects
        ops.data.remove_custom_property(objs, 'gl_vertex_metallic_roughness')
        ops.data.remove_custom_property(objs, 'gl_vertex_color')

        for obj in objs:
            colors = obj.data.color_attributes
            if colors.get('gl_color'):
                colors.remove(colors.get('gl_color'))
            if colors.get('gl_metallic_roughness'):
                colors.remove(colors.get('gl_metallic_roughness'))
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Add_GL_Lightmap(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_lightmap'
    bl_label = 'Add ::  gl_lightmap'
    bl_description = 'Add Custom Property ::  gl_lightmap'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):        
        return context.selected_objects and not len(ops.data.with_custom_property(context.selected_objects, 'gl_lightmap')) == len(context.selected_objects)

    def execute(self, context):
        # raise Exception("Not implemented yet")
        ops.data.set_custom_property(
            context.selected_objects, 'gl_lightmap', 1)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_GL_Lightmap(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_lightmap'
    bl_label = 'Remove ::  gl_lightmap'
    bl_description = 'Remove Custom Property ::  gl_lightmap'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and ops.data.with_custom_property(context.selected_objects, 'gl_lightmap')

    def execute(self, context):
        ops.data.remove_custom_property(
            context.selected_objects, 'gl_lightmap')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Add_Collider(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_collider'
    bl_label = 'Add ::  collider'
    bl_description = 'Add Custom Property ::  collider'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):        
        return context.selected_objects and not len(ops.data.with_custom_property(context.selected_objects, 'collider')) == len(context.selected_objects)

    def execute(self, context):
        # raise Exception("Not implemented yet")
        ops.build.collider(context.selected_objects)
        ops.data.set_custom_property(
            context.selected_objects, 'collider', 1)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_Collider(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_collider'
    bl_label = 'Remove ::  collider'
    bl_description = 'Remove Custom Property ::  collider'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and ops.data.with_custom_property(context.selected_objects, 'collider')

    def execute(self, context):
        ops.data.remove_custom_property(
            context.selected_objects, 'collider')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


classes = (AM_CP_Add_GL_SeaparateCullingPass,
           AM_CP_Remove_GL_SeaparateCullingPass,
           AM_CP_Add_GL_AlphaIndex,
           AM_CP_Remove_GL_AlphaIndex,
           AM_CP_Add_GL_Translucency, AM_CP_Remove_GL_Translucency, AM_CP_Add_GL_BlendMultiply, AM_CP_Remove_GL_BlendMultiply, AM_CP_Add_GL_VertexColorMetallicRougness, AM_CP_Remove_GL_VertexColorMetallicRougness,
           AM_CP_Add_GL_Lightmap,
           AM_CP_Remove_GL_Lightmap,
           AM_CP_Add_Collider,
           AM_CP_Remove_Collider)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
