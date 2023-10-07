

class UI:
    nav = nav
    
    @staticmethod
    @log.catch
    def message_popup(message="", title="Message Box", icon='INFO'):
        def draw(self, context):
            self.layout.label(text=message)

        bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)

    @staticmethod
    @log.catch
    def input_dialog(title="Value", description="Enter a value", default: Union[int, float, str] = "") -> Union[int, float, str]:
        bpy.context.window_manager.generic_input_dialog.input_name = title
        bpy.context.window_manager.generic_input_dialog.input_description = description
        bpy.context.window_manager.generic_input_dialog.input_default = default
        bpy.context.window_manager.generic_input_dialog.input_type = PropertyType.get(default, PropertyType.STRING)
        
        result = bpy.ops.amblender.generic_input_dialog('INVOKE_DEFAULT')
        if result == {'FINISHED'}:
            return getattr(bpy.context.window_manager.generic_input_dialog, "user_input", None)
        
        return None

    @staticmethod
    @log.catch
    def redraw(space_type: SpaceType):
        for area in bpy.context.screen.areas:
            if area.type == space_type.value:
                for space in area.spaces:
                    if space.type == space_type.value:
                        area.tag_redraw()