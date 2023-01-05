from ...std import *
import threading


class Nav:
    @staticmethod
    @log.catch
    #@ TODO: add context Enum
    def view_selected(context: str = 'VIEW_3D'):
        bpy.types.Context
        area = bpy.context.area
        old_type = area.type
        area.type = context
        bpy.ops.view3d.view_selected()
        area.type = old_type

    @staticmethod
    @log.catch
    def workspace(workspace: WorkSpaceId, focus_selected: bool = True):
        bpy.context.window.workspace = bpy.data.workspaces[workspace.value]
        if focus_selected:
            Nav.view_selected()

nav = Nav()
