from ..std import *


class AM_SU_Disconnect_NormalMap(bpy.types.Operator):
    bl_idname = 'amblender.shader_util_disconnect_normal_map'
    bl_label = 'Disconnect Normal Maps'
    bl_description = 'Disconnect Normal Maps'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and ops.shader.node.inputs(
            context.selected_objects, bpy.types.ShaderNodeBsdfPrincipled, "Normal")

    def execute(self, context):
        ops.shader.node.disconnect_inputs(
            context.selected_objects, bpy.types.ShaderNodeBsdfPrincipled, "Normal")

        return {'FINISHED'}


class AM_SU_Disconnect_GLTF_OcclusionMap(bpy.types.Operator):
    bl_idname = 'amblender.shader_util_disconnect_gltf_occlusion_map'
    bl_label = 'Disconnect GLTF Occlusion Maps'
    bl_description = 'Disconnect GLTF Occlusion Maps'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and ops.shader.node.inputs(
            context.selected_objects, bpy.types.ShaderNodeGroup, "Occlusion")

    def execute(self, context):
        ops.shader.node.disconnect_inputs(
            context.selected_objects, bpy.types.ShaderNodeGroup, "Occlusion")

        return {'FINISHED'}


class AM_SU_Enable_Backface_Culling(bpy.types.Operator):
    bl_idname = 'amblender.shader_util_enabled_backface_culling'
    bl_label = 'Backface Culling :: True'
    bl_description = 'Backface Culling :: True'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        mats = ops.shader.materials(context.selected_objects)
        return context.selected_objects and any(not m.use_backface_culling for m in mats)

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
        mats = ops.shader.materials(context.selected_objects)
        return context.selected_objects and any(m.use_backface_culling for m in mats)

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
        mats = ops.shader.materials(context.selected_objects)
        return context.selected_objects and any(m.blend_method != BlendMode.OPAQUE.value for m in mats)

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
        mats = ops.shader.materials(context.selected_objects)
        return context.selected_objects and any(m.blend_method != BlendMode.BLEND.value for m in mats)

    def execute(self, context):
        ops.shader.blend_mode(context.selectable_objects, BlendMode.BLEND)

        return {'FINISHED'}


class AM_SU_Set_Material_LOD0(bpy.types.Operator):
    bl_idname = 'amblender.shader_util_set_material_lod0'
    bl_label = 'Material :: LOD_0'
    bl_description = 'Material :: LOD_0'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.shader.set_material_lod(context.selected_objects, 0)
        return {'FINISHED'}


class AM_SU_Set_Material_LOD1(bpy.types.Operator):
    bl_idname = 'amblender.shader_util_set_material_lod1'
    bl_label = 'Material :: LOD_1'
    bl_description = 'Material :: LOD_1'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        mats = ops.shader.materials(context.selected_objects)
        return context.selected_objects and any(m.amb_mat.lod != 1 for m in mats)

    def execute(self, context):
        ops.shader.set_material_lod(context.selected_objects, 1)

        return {'FINISHED'}


classes = (AM_SU_Disconnect_NormalMap,
           AM_SU_Disconnect_GLTF_OcclusionMap,
           AM_SU_Enable_Backface_Culling,
           AM_SU_Disable_Backface_Culling,
           AM_SU_Set_Blend_Mode_Opaque,
           AM_SU_Set_Blend_Mode_AlphaBlend,
           AM_SU_Set_Material_LOD0,
           AM_SU_Set_Material_LOD1
           )


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
