from ..std import *


class AM_DU_UnpackImages(bpy.types.Operator):
    bl_idname = 'amblender.du_unpack_images'
    bl_label = 'Unpack Images'
    bl_description = 'Unpack Images'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        ops.data.unpack_images()

        return {'FINISHED'}


class AM_DU_Set_Diffuse_Image_Scale_2048(bpy.types.Operator):
    bl_idname = 'amblender.du_set_diffuse_image_scale_2048'
    bl_label = 'Scale Diffuse Maps :: 2048'
    bl_description = 'Scale Diffuse Maps :: 2048'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        for node in nodes:
            log.info(f'node: {node.name}')

        nodes = ops.shader.node.connected_to_input(
            nodes, 'Base Color', bpy.types.ShaderNodeBsdfPrincipled)
        for node in nodes:
            log.info(f'node: {node.name}')

        ops.data.scale_images_to_maxsize(nodes, Size.P2_2048)

        return {'FINISHED'}


class AM_DU_Set_Diffuse_Image_Scale_1024(bpy.types.Operator):
    bl_idname = 'amblender.du_set_diffuse_image_scale_1024'
    bl_label = 'Scale Diffuse Maps :: 1024'
    bl_description = 'Scale Diffuse Maps :: 1024'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        nodes = ops.shader.node.connected_to_input(
            nodes, 'Base Color', bpy.types.ShaderNodeBsdfPrincipled)
        ops.data.scale_images_to_maxsize(nodes, Size.P2_1024)

        return {'FINISHED'}


class AM_DU_Set_Diffuse_Image_Scale_512(bpy.types.Operator):
    bl_idname = 'amblender.du_set_diffuse_image_scale_512'
    bl_label = 'Scale Diffuse Maps :: 512'
    bl_description = 'Scale Diffuse Maps :: 512'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        nodes = ops.shader.node.connected_to_input(
            nodes, 'Base Color', bpy.types.ShaderNodeBsdfPrincipled)
        ops.data.scale_images_to_maxsize(nodes, Size.P2_512)

        return {'FINISHED'}


class AM_DU_Set_Diffuse_Image_Scale_256(bpy.types.Operator):
    bl_idname = 'amblender.du_set_diffuse_image_scale_256'
    bl_label = 'Scale Diffuse Maps :: 256'
    bl_description = 'Scale Diffuse Maps :: 256'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        nodes = ops.shader.node.connected_to_input(
            nodes, 'Base Color', bpy.types.ShaderNodeBsdfPrincipled)
        ops.data.scale_images_to_maxsize(nodes, Size.P2_256)

        return {'FINISHED'}


class AM_DU_Set_Normal_Image_Scale_2048(bpy.types. Operator):
    bl_idname = 'amblender.du_set_normal_image_scale_2048'
    bl_label = 'Scale Normal Maps :: 2048'
    bl_description = 'Scale Normal Maps :: 2048'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        for node in nodes:
            log.info(f'node: {node.name}')

        nodes = ops.shader.node.connected_to_input(
            nodes, 'Normal', bpy.types.ShaderNodeBsdfPrincipled)
        for node in nodes:
            log.info(f'node: {node.name}')

        ops.data.scale_images_to_maxsize(nodes, Size.P2_2048)

        return {'FINISHED'}


class AM_DU_Set_Normal_Image_Scale_1024(bpy.types.Operator):
    bl_idname = 'amblender.du_set_normal_image_scale_1024'
    bl_label = 'Scale Normal Maps :: 1024'
    bl_description = 'Scale Normal Maps :: 1024'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        nodes = ops.shader.node.connected_to_input(
            nodes, 'Normal', bpy.types.ShaderNodeBsdfPrincipled)
        ops.data.scale_images_to_maxsize(nodes, Size.P2_1024)

        return {'FINISHED'}


class AM_DU_Set_Normal_Image_Scale_512(bpy.types.Operator):
    bl_idname = 'amblender.du_set_normal_image_scale_512'
    bl_label = 'Scale Normal Maps :: 512'
    bl_description = 'Scale Normal Maps :: 512'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        nodes = ops.shader.node.connected_to_input(
            nodes, 'Normal', bpy.types.ShaderNodeBsdfPrincipled)
        ops.data.scale_images_to_maxsize(nodes, Size.P2_512)

        return {'FINISHED'}


class AM_DU_Set_Normal_Image_Scale_256(bpy.types.Operator):
    bl_idname = 'amblender.du_set_normal_image_scale_256'
    bl_label = 'Scale Normal Maps :: 256'
    bl_description = 'Scale Normal Maps :: 256'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        nodes = ops.shader.node.connected_to_input(
            nodes, 'Normal', bpy.types.ShaderNodeBsdfPrincipled)
        ops.data.scale_images_to_maxsize(nodes, Size.P2_256)

        return {'FINISHED'}


class AM_DU_Set_RoughMetallicOcc_Image_Scale_2048(bpy.types.Operator):
    bl_idname = 'amblender.du_set_rough_metallic_occ_image_scale_2048'
    bl_label = 'Scale Roughness Metallic Occlusion Maps :: 2048'
    bl_description = 'Scale Roughness Metallic Occlusion Maps :: 2048'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        nodes = ops.shader.node.connected_to_input(
            nodes, ['Metallic', 'Roughness', 'Occlusion'])
        ops.data.scale_images_to_maxsize(nodes, Size.P2_2048)

        return {'FINISHED'}


class AM_DU_Set_RoughMetallicOcc_Image_Scale_1024(bpy.types.Operator):
    bl_idname = 'amblender.du_set_rough_metallic_occ_image_scale_1024'
    bl_label = 'Scale Roughness Metallic Occlusion Maps :: 1024'
    bl_description = 'Scale Roughness Metallic Occlusion Maps :: 1024'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        nodes = ops.shader.node.connected_to_input(
            nodes, ['Metallic', 'Roughness', 'Occlusion'])
        ops.data.scale_images_to_maxsize(nodes, Size.P2_1024)

        return {'FINISHED'}


class AM_DU_Set_RoughMetallicOcc_Image_Scale_512(bpy.types.Operator):
    bl_idname = 'amblender.du_set_rough_metallic_occ_image_scale_512'
    bl_label = 'Scale Roughness Metallic Occlusion Maps :: 512'
    bl_description = 'Scale Roughness Metallic Occlusion Maps :: 512'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        nodes = ops.shader.node.connected_to_input(
            nodes, ['Metallic', 'Roughness', 'Occlusion'])
        ops.data.scale_images_to_maxsize(nodes, Size.P2_512)

        return {'FINISHED'}


class AM_DU_Set_RoughMetallicOcc_Image_Scale_256(bpy.types.Operator):
    bl_idname = 'amblender.du_set_rough_metallic_occ_image_scale_256'
    bl_label = 'Scale Roughness Metallic Occlusion Maps :: 256'
    bl_description = 'Scale Roughness Metallic Occlusion Maps :: 256'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        nodes = ops.shader.node.connected_to_input(
            nodes, ['Metallic', 'Roughness', 'Occlusion'])
        ops.data.scale_images_to_maxsize(nodes, Size.P2_256)

        return {'FINISHED'}


class AM_DU_Set_RoughMetallicOcc_Image_Scale_128(bpy.types.Operator):
    bl_idname = 'amblender.du_set_rough_metallic_occ_image_scale_128'
    bl_label = 'Scale Roughness Metallic Occlusion Maps :: 128'
    bl_description = 'Scale Roughness Metallic Occlusion Maps :: 128'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        nodes = ops.shader.node.connected_to_input(
            nodes, ['Metallic', 'Roughness', 'Occlusion'])
        ops.data.scale_images_to_maxsize(nodes, Size.P2_128)

        return {'FINISHED'}


class AM_DU_Set_RoughMetallicOcc_Image_Scale_64(bpy.types.Operator):
    bl_idname = 'amblender.du_set_rough_metallic_occ_image_scale_64'
    bl_label = 'Scale Roughness Metallic Occlusion Maps :: 64'
    bl_description = 'Scale Roughness Metallic Occlusion Maps :: 64'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        nodes = ops.shader.node.of_type(
            context.selected_objects, bpy.types.ShaderNodeTexImage)
        nodes = ops.shader.node.connected_to_input(
            nodes, ['Metallic', 'Roughness', 'Occlusion'])
        ops.data.scale_images_to_maxsize(nodes, Size.P2_64)

        return {'FINISHED'}


class AM_DU_Reset_Scaled_Images(bpy.types.Operator):
    bl_idname = 'amblender.du_reset_scaled_images'
    bl_label = 'Reset Map Scales'
    bl_description = 'Reset Map Scales'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack

    def execute(self, context):
        ops.data.reset_scaled_images(context.selected_objects)

        return {'FINISHED'}


class AM_DU_Clear_CustomSplitNormals(bpy.types.Operator):
    bl_idname = 'amblender.du_clear_custom_split_normals'
    bl_label = 'Clear Custom Split Normals'
    bl_description = 'Clear Custom Split Normals'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not bpy.data.use_autopack and any([o.data for o in context.selected_objects if o.type == 'MESH'])

    def execute(self, context):

        return {'FINISHED'}


classes = (AM_DU_UnpackImages,
           AM_DU_Reset_Scaled_Images,
           AM_DU_Set_Diffuse_Image_Scale_2048,
           AM_DU_Set_Diffuse_Image_Scale_1024,
           AM_DU_Set_Diffuse_Image_Scale_512,
           AM_DU_Set_Diffuse_Image_Scale_256,
           AM_DU_Set_Normal_Image_Scale_2048,
           AM_DU_Set_Normal_Image_Scale_1024,
           AM_DU_Set_Normal_Image_Scale_512,
           AM_DU_Set_Normal_Image_Scale_256,
           AM_DU_Set_RoughMetallicOcc_Image_Scale_2048,
           AM_DU_Set_RoughMetallicOcc_Image_Scale_1024,
           AM_DU_Set_RoughMetallicOcc_Image_Scale_512,
           AM_DU_Set_RoughMetallicOcc_Image_Scale_256,
           AM_DU_Set_RoughMetallicOcc_Image_Scale_128,
           AM_DU_Set_RoughMetallicOcc_Image_Scale_64)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
