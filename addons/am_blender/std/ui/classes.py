import bpy

class InputDialog(bpy.types.Operator):
    bl_idname = 'amblender.input_dialog'
    bl_label = 'Input Dialog'
    bl_description = 'Input Dialog with input type'
    bl_options = {'REGISTER', 'INTERNAL'}
    
    # These properties will store the user's desired settings for the dialog
    input_name: bpy.props.StringProperty(default="Value")
    input_description: bpy.props.StringProperty(default="Enter a value")
    input_default: bpy.props.StringProperty(default="")
    input_type: bpy.props.StringProperty(default="bpy.props.StringProperty()")

    # This property will store the user's input
    user_input: bpy.props.StringProperty()

    def execute(self, context):
        return {'FINISHED'}

    def draw(self, context):
        row = self.layout
        row.prop(self, "user_input", text=self.input_name)
        row.active = True
        row.scale_y = 1.5
        row.alert = True

    def invoke(self, context, event):
        # Dynamically create the property based on the user's desired data type
        setattr(InputDialog, "user_input", eval(self.input_type))
        return context.window_manager.invoke_props_dialog(self)
    

classes = (InputDialog,
           )


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)