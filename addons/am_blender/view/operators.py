from ..std import *


class AM_V_Show_Colliders(bpy.types.Operator):
    bl_idname = 'amblender.v_show_colliders'
    bl_label = 'Show Colliders'
    bl_description = 'Show all collider objects in the viewport.'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def _get_colliders(self, context) -> set['Object']:
        objs = of_type(context.selected_objects, 'MESH')
        return set(o for o in objs if o.hide_viewport and any('collider' in prop_name for prop_name in o.keys()))

    @classmethod
    def poll(cls, context):
        return len(cls._get_colliders(context)) > 0

    def execute(self, context):
        objs = self._get_colliders(context)
        for o in objs:
            o.hide_viewport = False

        return {'FINISHED'}


class AM_V_Hide_Colliders(bpy.types.Operator):
    bl_idname = 'amblender.v_hide_colliders'
    bl_label = 'Hide Colliders'
    bl_description = 'Hide all collider objects in the viewport.'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def _get_colliders(self, context) -> set['Object']:
        objs = of_type(context.selected_objects, 'MESH')
        return set(o for o in objs if not o.hide_viewport and any('collider' in prop_name for prop_name in o.keys()))

    @classmethod
    def poll(cls, context):
        return len(cls._get_colliders(context)) > 0

    def execute(self, context):
        objs = self._get_colliders(context)
        for o in objs:
            o.hide_viewport = True

        return {'FINISHED'}

classes = (AM_V_Show_Colliders,
              AM_V_Hide_Colliders
           )


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
