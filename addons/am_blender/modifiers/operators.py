
from ..std import *


class AM_OP_Modifiers_Disable(bpy.types.Operator):
    bl_idname = 'amblender.op_modifiers_disable'
    bl_label = 'Disable Modifiers'
    bl_description = 'Disable Modifiers'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and any(mod.show_render or mod.show_viewport for obj in context.selected_objects for mod in obj.modifiers)

    def execute(self, context):
        ops.modifier.show_render(context.selected_objects, False)
        ops.modifier.show_viewport(context.selected_objects, False)

        return {'FINISHED'}
    

class AM_OP_Modifiers_Enable(bpy.types.Operator):
    bl_idname = 'amblender.op_modifiers_enable'
    bl_label = 'Enable Modifiers'
    bl_description = 'Enable Modifiers'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.selected_objects and not any(mod.show_render or mod.show_viewport for obj in context.selected_objects for mod in obj.modifiers)

    
    def execute(self, context):
        ops.modifier.show_render(context.selected_objects, True)
        ops.modifier.show_viewport(context.selected_objects, True)

        return {'FINISHED'}
    

classes = (AM_OP_Modifiers_Disable,
           AM_OP_Modifiers_Enable
           )


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
