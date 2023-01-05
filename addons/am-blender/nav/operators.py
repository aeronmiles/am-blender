from ..std import *


class AM_Nav_Workspace_Modeling(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_modeling'
    bl_label = 'Modeling'
    bl_description = 'Load Modeling Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.nav.workspace(WorkSpaceId.Modeling)
        return {'FINISHED'}


class AM_Nav_Workspace_UV_Editing(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_uv_editing'
    bl_label = 'UV Editing'
    bl_description = 'Load UV Editing Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.nav.workspace(WorkSpaceId.UVEditing)
        return {'FINISHED'}


class AM_Nav_Workspace_Layout(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_layout'
    bl_label = 'Layout'
    bl_description = 'Load Layout Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.nav.workspace(WorkSpaceId.Layout)
        return {'FINISHED'}


class AM_Nav_Workspace_Sculpting(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_sculpting'
    bl_label = 'Sculpting'
    bl_description = 'Load Sculpting Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.nav.workspace(WorkSpaceId.Sculpting)
        return {'FINISHED'}


class AM_Nav_Workspace_Texture_Paint(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_texture_paint'
    bl_label = 'Texture Paint'
    bl_description = 'Load Texture Paint Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.nav.workspace(WorkSpaceId.TexturePaint)
        return {'FINISHED'}


class AM_Nav_Workspace_Shading(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_shading'
    bl_label = 'Shading'
    bl_description = 'Load Shading Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.nav.workspace(WorkSpaceId.Shading)
        return {'FINISHED'}


class AM_Nav_Workspace_Rendering(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_rendering'
    bl_label = 'Rendering'
    bl_description = 'Load Rendering Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.nav.workspace(WorkSpaceId.Rendering)
        return {'FINISHED'}


class AM_Nav_Workspace_Assets(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_assets'
    bl_label = 'Assets'
    bl_description = 'Load Assets Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.nav.workspace(WorkSpaceId.Assets)
        return {'FINISHED'}


class AM_Nav_Workspace_Geometry_Nodes(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_geometry_nodes'
    bl_label = 'Geometry Nodes'
    bl_description = 'Load Geometry Nodes Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.nav.workspace(WorkSpaceId.GeometryNodes)
        return {'FINISHED'}


class AM_Nav_Workspace_Scripting(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_scripting'
    bl_label = 'Scripting'
    bl_description = 'Load Scripting Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.nav.workspace(WorkSpaceId.Scripting)
        return {'FINISHED'}


classes = (AM_Nav_Workspace_Modeling, AM_Nav_Workspace_UV_Editing, AM_Nav_Workspace_Layout, AM_Nav_Workspace_Sculpting, AM_Nav_Workspace_Texture_Paint, AM_Nav_Workspace_Shading, AM_Nav_Workspace_Rendering, AM_Nav_Workspace_Geometry_Nodes, AM_Nav_Workspace_Scripting,
           AM_Nav_Workspace_Assets)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
