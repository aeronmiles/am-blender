from ..std import *


class AM_Nav_Workspace_Modeling(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_modeling'
    bl_label = 'Modeling'
    bl_description = 'Load Modeling Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.workspace(WorkSpaceId.Modeling)
        return {'FINISHED'}


class AM_Nav_Workspace_UV_Editing(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_uv_editing'
    bl_label = 'UV Editing'
    bl_description = 'Load UV Editing Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.workspace(WorkSpaceId.UVEditing)
        return {'FINISHED'}


class AM_Nav_Workspace_Layout(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_layout'
    bl_label = 'Layout'
    bl_description = 'Load Layout Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.workspace(WorkSpaceId.Layout)
        return {'FINISHED'}


class AM_Nav_Workspace_Sculpting(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_sculpting'
    bl_label = 'Sculpting'
    bl_description = 'Load Sculpting Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.workspace(WorkSpaceId.Sculpting)
        return {'FINISHED'}


class AM_Nav_Workspace_Texture_Paint(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_texture_paint'
    bl_label = 'Texture Paint'
    bl_description = 'Load Texture Paint Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.workspace(WorkSpaceId.TexturePaint)
        return {'FINISHED'}


class AM_Nav_Workspace_Shading(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_shading'
    bl_label = 'Shading'
    bl_description = 'Load Shading Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.workspace(WorkSpaceId.Shading)
        return {'FINISHED'}


class AM_Nav_Workspace_Rendering(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_rendering'
    bl_label = 'Rendering'
    bl_description = 'Load Rendering Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.workspace(WorkSpaceId.Rendering)
        return {'FINISHED'}


class AM_Nav_Workspace_Assets(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_assets'
    bl_label = 'Assets'
    bl_description = 'Load Assets Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.workspace(WorkSpaceId.Assets)
        return {'FINISHED'}


class AM_Nav_Workspace_Geometry_Nodes(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_geometry_nodes'
    bl_label = 'Geometry Nodes'
    bl_description = 'Load Geometry Nodes Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.workspace(WorkSpaceId.GeometryNodes)
        return {'FINISHED'}


class AM_Nav_Workspace_Scripting(bpy.types.Operator):
    bl_idname = 'amblender.nav_workspace_scripting'
    bl_label = 'Scripting'
    bl_description = 'Load Scripting Workspace'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.workspace(WorkSpaceId.Scripting)
        return {'FINISHED'}


class AM_Nav_Properties_Tab_Tool(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_tool'
    bl_label = 'Tool'
    bl_description = 'Load Tool'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.TOOL)
        return {'FINISHED'}

class AM_Nav_Properties_Tab_Render(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_render'
    bl_label = 'Render'
    bl_description = 'Load Render'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.RENDER)
        return {'FINISHED'}
    
class AM_Nav_Properties_Tab_Output(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_output'
    bl_label = 'Output'
    bl_description = 'Load Output'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.OUTPUT)
        return {'FINISHED'}
    
class AM_Nav_Properties_Tab_View_Layer(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_view_layer'
    bl_label = 'View Layer'
    bl_description = 'Load View Layer'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.VIEW_LAYER)
        return {'FINISHED'}

class AM_Nav_Properties_Tab_Scene(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_scene'
    bl_label = 'Scene'
    bl_description = 'Load Scene'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.SCENE)
        return {'FINISHED'}

class AM_Nav_Properties_Tab_World(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_world'
    bl_label = 'World'
    bl_description = 'Load World'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.WORLD)
        return {'FINISHED'}
    
class AM_Nav_Properties_Tab_Collection(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_collection'
    bl_label = 'Collection'
    bl_description = 'Load Collection'

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.COLLECTION)
        return {'FINISHED'}
    
class AM_Nav_Properties_Tab_Object(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_object'
    bl_label = 'Object'
    bl_description = 'Load Object'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.OBJECT)
        return {'FINISHED'}

class AM_Nav_Properties_Tab_Modifier(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_modifier'
    bl_label = 'Modifier'
    bl_description = 'Load Modifier'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.MODIFIER)
        return {'FINISHED'}

class AM_Nav_Properties_Tab_Particles(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_particles'
    bl_label = 'Particles'
    bl_description = 'Load Particles'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.PARTICLES)
        return {'FINISHED'}

class AM_Nav_Properties_Tab_Physics(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_physics'
    bl_label = 'Physics'
    bl_description = 'Load Physics'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.PHYSICS)
        return {'FINISHED'}
    
class AM_Nav_Properties_Tab_Constraint(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_constraint'
    bl_label = 'Constraint'
    bl_description = 'Load Constraint'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.CONSTRAINT)
        return {'FINISHED'}
    
class AM_Nav_Properties_Tab_Data(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_data'
    bl_label = 'Data'
    bl_description = 'Load Data'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.DATA)
        return {'FINISHED'}

class AM_Nav_Properties_Tab_Material(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_material'
    bl_label = 'Material'
    bl_description = 'Load Material'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.MATERIAL)
        return {'FINISHED'}

class AM_Nav_Properties_Tab_Texture(bpy.types.Operator):
    bl_idname = 'amblender.nav_properties_tab_texture'
    bl_label = 'Texture'
    bl_description = 'Load Texture'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    def execute(self, context):
        ops.ui.nav.properties_tab(PropertiesTab.TEXTURE)
        return {'FINISHED'}

classes = (AM_Nav_Workspace_Modeling, 
           AM_Nav_Workspace_UV_Editing, 
           AM_Nav_Workspace_Layout,
           AM_Nav_Workspace_Sculpting,
           AM_Nav_Workspace_Texture_Paint,
           AM_Nav_Workspace_Shading,
           AM_Nav_Workspace_Rendering,
           AM_Nav_Workspace_Geometry_Nodes,
           AM_Nav_Workspace_Scripting,
           AM_Nav_Workspace_Assets,
           AM_Nav_Properties_Tab_Tool,
           AM_Nav_Properties_Tab_Render,
           AM_Nav_Properties_Tab_Output,
           AM_Nav_Properties_Tab_View_Layer,
           AM_Nav_Properties_Tab_Scene,
           AM_Nav_Properties_Tab_World,
           AM_Nav_Properties_Tab_Collection,
           AM_Nav_Properties_Tab_Object,
           AM_Nav_Properties_Tab_Modifier,
           AM_Nav_Properties_Tab_Particles,
           AM_Nav_Properties_Tab_Physics,
           AM_Nav_Properties_Tab_Constraint,
           AM_Nav_Properties_Tab_Data,
           AM_Nav_Properties_Tab_Material,
           AM_Nav_Properties_Tab_Texture)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
