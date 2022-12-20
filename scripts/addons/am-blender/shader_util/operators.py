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
        bpy.ops.object.mode_set(mode='OBJECT')
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
        bpy.ops.object.mode_set(mode='OBJECT')
        ops.shader.disconnect_inputs(
            context.selected_objects, bpy.types.ShaderNodeGroup, "Occlusion")

        return {'FINISHED'}


classes = (AM_SU_Disconnect_NormalMap,
           AM_SU_Disconnect_GLTF_OcclusionMap,
           )


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
