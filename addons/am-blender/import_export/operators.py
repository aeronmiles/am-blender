from ..std import *


class AM_Export_Batch_GLTF_EMBEDDED(bpy.types.Operator):
    bl_idname = 'amblender.export_batch_gltf_embedded'
    bl_label = 'Export Selected to GLTF_EMBEDDED files'
    bl_description = 'Export Selected to GLTF_EMBEDDED files'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.io.exp.batch_gltf_embedded(context)

        return {'FINISHED'}


class AM_Export_Batch_GLTF_SEPARATE(bpy.types.Operator):
    bl_idname = 'amblender.export_batch_gltf_separate'
    bl_label = 'Export Selected to GLTF_SEPARATE files'
    bl_description = 'Export Selected to GLTF_SEPARATE files'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.io.exp.batch_gltf_separate(context)

        return {'FINISHED'}
        

class AM_Export_Batch_GLB(bpy.types.Operator):
    bl_idname = 'amblender.export_batch_glb'
    bl_label = 'Export Selected to GLB files'
    bl_description = 'Export Selected to GLB files'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.io.exp.batch_glb(context)

        return {'FINISHED'}
        

class AM_Export_Batch_USDZ(bpy.types.Operator):
    bl_idname = 'amblender.export_batch_usdz'
    bl_label = 'Export Selected to USDZ files'
    bl_description = 'Export Selected to USDZ files'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.io.exp.batch_usdz(context)

        return {'FINISHED'}


classes = (AM_Export_Batch_GLTF_EMBEDDED, AM_Export_Batch_GLTF_SEPARATE, AM_Export_Batch_GLB, AM_Export_Batch_USDZ)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
