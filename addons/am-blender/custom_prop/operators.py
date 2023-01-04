from ..std import *


class AM_CP_Add_GL_SeaparateCullingPass(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_separate_culling_pass'
    bl_label = 'Add ::  gl_separate_culling_pass'
    bl_description = 'Add Custom Property ::  gl_separate_culling_pass'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.data.set_custom_property(
            context.selected_objects, 'gl_separate_culling_pass', 1.0)

        return {'FINISHED'}


class AM_CP_Remove_GL_SeaparateCullingPass(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_separate_culling_pass'
    bl_label = 'Remove ::  gl_separate_culling_pass'
    bl_description = 'Remove Custom Property ::  gl_separate_culling_pass'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.data.remove_custom_property(
            context.selected_objects, 'separate_culling_pass')

        return {'FINISHED'}


class AM_CP_Add_GL_DepthPrePass(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_separate_culling_pass'
    bl_label = 'Add ::  gl_separate_culling_pass'
    bl_description = 'Add Custom Property ::  gl_separate_culling_pass'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.data.set_custom_property(
            context.selected_objects, 'gl_separate_culling_pass', 1.0)

        return {'FINISHED'}


class AM_CP_Remove_GL_DepthPrePass(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_separate_culling_pass'
    bl_label = 'Remove ::  gl_separate_culling_pass'
    bl_description = 'Remove Custom Property ::  gl_separate_culling_pass'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.data.remove_custom_property(
            context.selected_objects, 'separate_culling_pass')

        return {'FINISHED'}

class AM_CP_Add_GL_Translucency(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_translucency'
    bl_label = 'Add ::  gl_translucency'
    bl_description = 'Add Custom Property ::  gl_translucency'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.data.set_custom_property(
            context.selected_objects, 'gl_translucency', 1.0)

        return {'FINISHED'}


class AM_CP_Remove_GL_Translucency(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_translucency'
    bl_label = 'Remove ::  gl_translucency'
    bl_description = 'Remove Custom Property ::  gl_translucency'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.data.remove_custom_property(
            context.selected_objects, 'gl_translucency')

        return {'FINISHED'}


class AM_CP_Add_GL_BlendMultiply(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_blend_multiply'
    bl_label = 'Add ::  gl_blend_multiply'
    bl_description = 'Add Custom Property ::  gl_blend_multiply'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.data.set_custom_property(
            context.selected_objects, 'gl_blend_multiply', 1.0)

        return {'FINISHED'}


class AM_CP_Remove_GL_BlendMultiply(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_blend_multiply'
    bl_label = 'Remove ::  gl_blend_multiply'
    bl_description = 'Remove Custom Property ::  gl_blend_multiply'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.data.remove_custom_property(
            context.selected_objects, 'gl_blend_multiply')

        return {'FINISHED'}


# @TODO: move implementation to std fn
class AM_CP_Add_GL_VertexColorMetallicRougness(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_vertex_color_metallic_roughness'
    bl_label = 'Add ::  gl_vertex_color_metallic_roughness'
    bl_description = 'Add Custom Property ::  gl_vertex_color_metallic_roughness'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        objs = context.selected_objects
        # active = context.active_object
        for obj in objs:
            if obj.type == 'MESH':
                colors = obj.data.color_attributes
                # context.view_layer.objects.active = obj
                # index = colors.active_color_index

                if colors.find("gl_color") == -1:
                    colors.new(name="gl_color",
                               type="FLOAT_COLOR", domain="POINT")
                    obj['gl_vertex_color'] = colors.find('gl_color')

                print("GL_METALLIC " + str(colors.find("gl_metallic_roughness")))
                if colors.find("gl_metallic_roughness") == -1:
                    colors.new(name="gl_metallic_roughness",
                               type="FLOAT_COLOR", domain="POINT")
                    ops.data.set_custom_property(
                        obj, 'gl_vertex_metallic_roughness', colors.find('gl_metallic_roughness'))

                # bpy.ops.geometry.color_attribute_render_set(name="gl_color")
                # colors.active_color_index = index

        # context.view_layer.objects.active = active
        return {'FINISHED'}


# @TODO: move implementation to std fn
class AM_CP_Remove_GL_VertexColorMetallicRougness(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_vertex_color_metallic_roughness'
    bl_label = 'Remove ::  gl_vertex_color_metallic_roughness'
    bl_description = 'Remove Custom Property ::  gl_vertex_color_metallic_roughness'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

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

        return {'FINISHED'}


class AM_CP_Add_GL_Lightmap(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_lightmap'
    bl_label = 'Add ::  gl_lightmap = {name}_lightmap'
    bl_description = 'Add Custom Property ::  gl_lightmap = {name}_lightmap'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.data.set_custom_property(
            context.selected_objects, 'gl_lightmap', obj.name + "_lightmap")

        return {'FINISHED'}


class AM_CP_Remove_GL_Lightmap(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_lightmap'
    bl_label = 'Remove ::  gl_lightmap'
    bl_description = 'Remove Custom Property ::  gl_lightmap'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.data.remove_custom_property(
            context.selected_objects, 'gl_lightmap')

        return {'FINISHED'}


classes = (AM_CP_Add_GL_SeaparateCullingPass,
           AM_CP_Remove_GL_SeaparateCullingPass,
           AM_CP_Add_GL_Translucency, AM_CP_Remove_GL_Translucency, AM_CP_Add_GL_BlendMultiply, AM_CP_Remove_GL_BlendMultiply, AM_CP_Add_GL_VertexColorMetallicRougness, AM_CP_Remove_GL_VertexColorMetallicRougness,
           AM_CP_Add_GL_Lightmap,
           AM_CP_Remove_GL_Lightmap)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
