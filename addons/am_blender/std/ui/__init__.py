from typing import Union
from . import classes
from .nav import nav
from ..log import log
from ..types import SpaceType, PropertyType
import bpy


modules = (classes,)

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

class UI:
    nav = nav

    @staticmethod
    def register():
        for m in modules:
            m.register()

    @staticmethod
    def unregister():
        for m in modules:
            m.unregister()
        
    @staticmethod
    @log.catch
    def message_popup(message="", title="Message Box", icon='INFO'):
        def draw(self, context):
            self.layout.label(text=message)

        bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)

    @staticmethod
    @log.catch
    def input_dialog(title="Value", description="Enter a value", default: Union[int, float, str] = "") -> Union[int, float, str]:
        
        # Define the property type based on the default value
        prop_type = PropertyType.get(default, PropertyType.STRING)
        
        result = bpy.ops.amblender.input_dialog('INVOKE_DEFAULT', 
                                                input_name=title, 
                                                input_description=description, 
                                                input_default=default, 
                                                input_type=prop_type)
        
        if result == {'FINISHED'}:
            # After the operator runs, retrieve the result
            return getattr(bpy.context.window_manager, "user_input", None)
        
        return None



    @staticmethod
    @log.catch
    def redraw(space_type: SpaceType):
        for area in bpy.context.screen.areas:
            if area.type == space_type.value:
                for space in area.spaces:
                    if space.type == space_type.value:
                        area.tag_redraw()


            
ui = UI()