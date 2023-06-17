from ..std import *


class AM_SU_Disconnect_NormalMap(bpy.types.Operator):
    bl_idname = 'amblender.su_disconnect_normal_map'
    bl_label = 'Disconnect Normal Maps'
    bl_description = 'Disconnect Normal Maps'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        return context.selected_objects and \
            ops.shader.node.connected_to_input(
                nodes, "Normal", bpy.types.ShaderNodeBsdfPrincipled)

    def execute(self, context):
        ops.shader.node.disconnect_inputs(
            context.selected_objects, "Normal", bpy.types.ShaderNodeBsdfPrincipled)

        return {'FINISHED'}


class AM_SU_Disconnect_GLTF_OcclusionMap(bpy.types.Operator):
    bl_idname = 'amblender.su_disconnect_gltf_occlusion_map'
    bl_label = 'Disconnect GLTF Occlusion Maps'
    bl_description = 'Disconnect GLTF Occlusion Maps'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        return context.selected_objects and \
            ops.shader.node.connected_to_input(
                nodes, "Occlusion", bpy.types.ShaderNodeGroup)

    def execute(self, context):
        ops.shader.node.disconnect_inputs(
            context.selected_objects, "Occlusion", bpy.types.ShaderNodeGroup)

        return {'FINISHED'}


class AM_SU_Enable_Backface_Culling(bpy.types.Operator):
    bl_idname = 'amblender.su_enabled_backface_culling'
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
    bl_idname = 'amblender.su_disable_backface_culling'
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
    bl_idname = 'amblender.su_set_opaque'
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
    bl_idname = 'amblender.su_set_alpha_blend'
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
    bl_idname = 'amblender.su_set_material_lod0'
    bl_label = 'Material :: LOD_0'
    bl_description = 'Material :: LOD_0'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        mats = ops.shader.materials(context.selected_objects)
        return context.selected_objects and any(m.amb_mat.lod != 0 for m in mats)

    def execute(self, context):
        ops.shader.set_material_lod(context.selected_objects, 0)
        return {'FINISHED'}


class AM_SU_Set_Material_LOD1(bpy.types.Operator):
    bl_idname = 'amblender.su_set_material_lod1'
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


class AM_SU_Set_Duplicate_Materials_To_Base_Material(bpy.types.Operator):
    bl_idname = 'amblender.su_set_duplicate_materials_to_base_material'
    bl_label = 'Set Duplicate Materials To Base Material'
    bl_description = 'Set Duplicate Materials To Base Material'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0

    def execute(self, context):
        ops.shader.set_duplicate_materials_to_base_material(context.selected_objects)

        return {'FINISHED'}


class AM_SU_Rename_UVMaps(bpy.types.Operator):
    bl_idname = 'amblender.su_rename_uvmaps'
    bl_label = 'Rename UV Maps -> uv1, uv2, ...'
    bl_description = 'Rename UV Maps -> uv1, uv2, ...'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.shader.rename_uvmaps(context.selected_objects)

        return {'FINISHED'}


class AM_SU_Rename_Textures(bpy.types.Operator):
    bl_idname = 'amblender.su_rename_textures'
    bl_label = 'Rename Textures After Mat Names'
    bl_description = 'Rename Textures After Mat Names'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        mats = ops.shader.materials(context.selected_objects)
        return context.selected_objects and mats

    def execute(self, context):
        ops.shader.rename_material_textures(context.selected_objects)

        return {'FINISHED'}


class AM_SU_Add_Lightmap_UV2s(bpy.types.Operator):
    bl_idname = 'amblender.su_add_lightmap_uv2s'
    bl_label = 'Add Lightmap UV2s'
    bl_description = 'Add Lightmap UV2s'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.shader.add_lightmap_uv2s(context.selected_objects)

        return {'FINISHED'}


class AM_Remove_Unassigned_Materials(bpy.types.Operator):
    bl_idname = 'amblender.su_remove_unassigned_materials'
    bl_label = 'Remove Unassigned Materials'
    bl_description = 'Remove Unassigned Materials'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.shader.remove_unassigned_materials(context.selected_objects)

        return {'FINISHED'}
    


class AM_Export_To_Select_EeveeMaterialOutputNodes(bpy.types.Operator):
    bl_idname = 'amblender.select_eevee_material_output_nodes'
    bl_label = 'Select Eevee Material Output Nodes'
    bl_description = 'Select Eevee Material Output Nodes'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        for mat in bpy.data.materials:
            mat.use_nodes = True
            for node in mat.node_tree.nodes:
                if node.type == 'OUTPUT_MATERIAL':
                    if node.target == 'EEVEE':
                        # node.select = True
                        mat.node_tree.nodes.active = node

        return {'FINISHED'}


classes = (AM_SU_Disconnect_NormalMap,
           AM_SU_Disconnect_GLTF_OcclusionMap,
           AM_SU_Enable_Backface_Culling,
           AM_SU_Disable_Backface_Culling,
           AM_SU_Set_Blend_Mode_Opaque,
           AM_SU_Set_Blend_Mode_AlphaBlend,
           AM_SU_Set_Material_LOD0,
           AM_SU_Set_Material_LOD1,
           AM_SU_Set_Duplicate_Materials_To_Base_Material,
           AM_SU_Rename_UVMaps,
           AM_SU_Add_Lightmap_UV2s,
           AM_Remove_Unassigned_Materials,
           AM_SU_Rename_Textures,
           AM_Export_To_Select_EeveeMaterialOutputNodes
           )


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
