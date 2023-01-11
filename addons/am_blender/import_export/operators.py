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
        ops.io.exp.batch_export(context, FileFormat.GLTF_EMBEDDED)

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
        ops.io.exp.batch_export(context, FileFormat.GLTF_SEPARATE)
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
        ops.io.exp.batch_export(context, FileFormat.GLB)

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
        log.error('USDZ export is not supported yet')
        ops.io.exp.batch_export(context, FileFormat.USDZ)

        return {'FINISHED'}


class AM_Export_To_GoogleModelViewer(bpy.types.Operator):
    bl_idname = 'amblender.export_google_model_viewer'
    bl_label = 'Export Selected to Google Model Viewer'
    bl_description = 'Export Selected to Google Model Viewer'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        ops.io.exp.to_google_model_viewer(context)

        return {'FINISHED'}


classes = (AM_Export_Batch_GLTF_EMBEDDED, AM_Export_Batch_GLTF_SEPARATE,
           AM_Export_Batch_GLB, AM_Export_Batch_USDZ, AM_Export_To_GoogleModelViewer)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
