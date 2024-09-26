import bpy
from ..log import log
from ..types import SpaceType, WorkSpaceId, PropertiesTab
from bpy.types import Context
from ..dec import dec

class Nav:
    @staticmethod
    @log.catch
    def view_selected(context: SpaceType = SpaceType.VIEW_3D):
        bpy.types.Context
        area = bpy.context.area
        old_type = area.type
        area.type = context.value
        bpy.ops.view3d.view_selected()
        area.type = old_type

    @staticmethod
    @log.catch
    def workspace(workspace: WorkSpaceId, focus_selected: bool = True):
        bpy.context.window.workspace = bpy.data.workspaces[workspace.value]
        if focus_selected:
            Nav.view_selected()

    @staticmethod
    @log.catch
    def properties_tab(tab: 'PropertiesTab'):
        # Iterate through all windows
        for window in bpy.context.window_manager.windows:
            # Iterate through all screens in the window
            for screen in window.screen.areas:
                if screen.type == 'PROPERTIES':
                    # Iterate through the spaces in the area (usually there's just one)
                    for space in screen.spaces:
                        if space.type == 'PROPERTIES':
                            # Set the context to the Mesh tab
                            space.context = tab.value


    @staticmethod
    @log.catch
    def outliner_toggle_hierarchy(context: 'Context', expanded: bool):
        state = 2
        if expanded:
            state = 1

        areas = (a for a in context.screen.areas if a.type == 'OUTLINER')
        for area in areas:
            bpy.ops.outliner.show_hierarchy({'area': area}, 'INVOKE_DEFAULT')
            # first expand, then collapse
            for _ in range(state):
                bpy.ops.outliner.expanded_toggle({'area': area})
            area.tag_redraw()

    @staticmethod
    @log.catch
    @dec.recall.selection
    def outliner_show_selected(context: 'Context'):
        areas = (a for a in context.screen.areas if a.type == 'OUTLINER')
        for obj in context.selected_objects:
            context.view_layer.objects.active = obj
            for area in areas:
                bpy.ops.outliner.show_active({'area': area}, 'INVOKE_DEFAULT')


nav = Nav()
