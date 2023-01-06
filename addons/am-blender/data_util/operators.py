from ..std import *


class AM_DU_UnpackImages(bpy.types.Operator):
    bl_idname = 'amblender.data_util_unpack_images'
    bl_label = 'Unpack Images'
    bl_description = 'Unpack Images'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        ops.data.unpack_images()

        return {'FINISHED'}


class AM_DU_Set_Image_Scale_2048(bpy.types.Operator):
    bl_idname = 'amblender.data_util_set_image_scale_2048'
    bl_label = 'Scale Image Maps to 2048'
    bl_description = 'Scale Image Maps to 2048'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.data.scale_images_to_maxsize(context.selected_objects, Size.P2_2048)

        return {'FINISHED'}


class AM_DU_Set_Image_Scale_1024(bpy.types.Operator):
    bl_idname = 'amblender.data_util_set_image_scale_1024'
    bl_label = 'Scale Image Maps to 1024'
    bl_description = 'Scale Image Maps to 1024'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.data.scale_images_to_maxsize(context.selected_objects, Size.P2_1024)

        return {'FINISHED'}


class AM_DU_Set_Image_Scale_512(bpy.types.Operator):
    bl_idname = 'amblender.data_util_set_image_scale_512'
    bl_label = 'Scale Image Maps to 512'
    bl_description = 'Scale Image Maps to 512'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.data.scale_images_to_maxsize(context.selected_objects, Size.P2_512)

        return {'FINISHED'}


class AM_DU_Set_Image_Scale_256(bpy.types.Operator):
    bl_idname = 'amblender.data_util_set_image_scale_256'
    bl_label = 'Scale Image Maps to 256'
    bl_description = 'Scale Image Maps to 256'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.data.scale_images_to_maxsize(context.selected_objects, Size.P2_256)

        return {'FINISHED'}


class AM_DU_Reset_Scaled_Images(bpy.types.Operator):
    bl_idname = 'amblender.data_util_reset_scaled_images'
    bl_label = 'Reset Map Scales'
    bl_description = 'Reset Map Scales'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.data.reset_scaled_images(context.selected_objects)

        return {'FINISHED'}


class AM_DU_Clear_CustomSplitNormals(bpy.types.Operator):
    bl_idname = 'amblender.data_util_clear_custom_split_normals'
    bl_label = 'Clear Custom Split Normals'
    bl_description = 'Clear Custom Split Normals'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and any([o.data for o in context.selected_objects if o.type == 'MESH'])

    def execute(self, context):
        
        return {'FINISHED'}


classes = (AM_DU_UnpackImages,
           AM_DU_Reset_Scaled_Images,
           AM_DU_Set_Image_Scale_2048,
           AM_DU_Set_Image_Scale_1024,
           AM_DU_Set_Image_Scale_512,
           AM_DU_Set_Image_Scale_256)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
