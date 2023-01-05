from ..std import *


class AM_SU_Disconnect_NormalMap(bpy.types.Operator):
    bl_idname = 'amblender.shader_util_disconnect_normal_map'
    bl_label = 'Disconnect Normal Maps'
    bl_description = 'Disconnect Normal Maps'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.shader.disconnect_inputs(
            context.selected_objects, bpy.types.ShaderNodeBsdfPrincipled, "Normal")

        return {'FINISHED'}


class AM_SU_Disconnect_GLTF_OcclusionMap(bpy.types.Operator):
    bl_idname = 'amblender.shader_util_disconnect_gltf_occlusion_map'
    bl_label = 'Disconnect GLTF Occlusion Maps'
    bl_description = 'Disconnect GLTF Occlusion Maps'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.shader.disconnect_inputs(
            context.selected_objects, bpy.types.ShaderNodeGroup, "Occlusion")

        return {'FINISHED'}


class AM_SU_Enable_Backface_Culling(bpy.types.Operator):
    bl_idname = 'amblender.shader_util_enabled_backface_culling'
    bl_label = 'Backface Culling :: True'
    bl_description = 'Backface Culling :: True'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.shader.backface_culling(context.selectable_objects, True)

        return {'FINISHED'}


class AM_SU_Disable_Backface_Culling(bpy.types.Operator):
    bl_idname = 'amblender.shader_util_disable_backface_culling'
    bl_label = 'Backface Culling :: False'
    bl_description = 'Backface Culling :: False'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.shader.backface_culling(context.selectable_objects, False)

        return {'FINISHED'}


class AM_SU_Set_Blend_Mode_Opaque(bpy.types.Operator):
    bl_idname = 'amblender.shader_util_set_opaque'
    bl_label = 'Blend Mode :: Opaque'
    bl_description = 'Blend Mode :: Opaque'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.shader.blend_mode(context.selectable_objects, BlendMode.OPAQUE)

        return {'FINISHED'}


class AM_SU_Set_Blend_Mode_AlphaBlend(bpy.types.Operator):
    bl_idname = 'amblender.shader_util_set_alpha_blend'
    bl_label = 'Blend Mode :: Alpha Blend'
    bl_description = 'Blend Mode :: Alpha Blend'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object

    def execute(self, context):
        ops.shader.blend_mode(context.selectable_objects, BlendMode.BLEND)

        return {'FINISHED'}


classes = (AM_SU_Disconnect_NormalMap,
           AM_SU_Disconnect_GLTF_OcclusionMap,
           AM_SU_Enable_Backface_Culling,
           AM_SU_Disable_Backface_Culling,
           AM_SU_Set_Blend_Mode_Opaque,
           AM_SU_Set_Blend_Mode_AlphaBlend
           )


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
