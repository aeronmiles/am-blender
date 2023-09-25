from ...std import *

class Ui:
    @staticmethod
    @log.catch
    def redraw(space_type: SpaceType):
        for area in bpy.context.screen.areas:
            if area.type == space_type.value:
                for space in area.spaces:
                    if space.type == space_type.value:
                        area.tag_redraw()


ui = Ui()
