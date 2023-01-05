from ..std import *


class AM_Convert_To_Empty_Mesh(bpy.types.Operator):
    bl_idname = 'amblender.convert_to_empty_mesh'
    bl_label = 'Convert To Empty Mesh'
    bl_description = 'Convert selected item to an empty mesh'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        objs = context.selected_objects
        bpy.ops.object.mode_set(mode='OBJECT')

        for obj in objs:
            empty_mesh = ops.build.empty_mesh(obj.name)
            ops.copy.transform(obj, empty_mesh)
            ops.copy.collections(obj, empty_mesh)
            ops.copy.childs(obj, empty_mesh)

            empty_mesh.select_set(state=True)
            empty_mesh.show_axis = True
        
        ops.data.unlink(objs)

        return {'FINISHED'}


class AM_Deselect_Non_Mesh_Objects(bpy.types.Operator):
    bl_idname = 'amblender.deselect_non_mesh_objects'
    bl_label = 'Deselect Non-Mesh Objects'
    bl_description = 'Deselect non-mesh objects'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects

    def execute(self, context):
        objs = context.selected_objects
        bpy.ops.object.mode_set(mode='OBJECT')

        for obj in objs:
            obj.select_set(obj.type == 'MESH')

        return {'FINISHED'}


classes = (AM_Convert_To_Empty_Mesh, AM_Deselect_Non_Mesh_Objects)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
