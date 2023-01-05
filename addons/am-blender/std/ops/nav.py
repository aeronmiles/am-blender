from ...std import *

class Nav:
    @staticmethod
    @log.catch
    def workspace(workspace: WorkSpaceId):
        bpy.context.window.workspace = bpy.data.workspaces[workspace.value]


nav = Nav()