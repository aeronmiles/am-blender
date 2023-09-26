from ..std import *


class AM_CP_Set_Layer(bpy.types.Operator):
    bl_idname = 'amblender.cp_set_layer'
    bl_label = 'Set :: layer'
    bl_description = 'Set Custom Property :: layer'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    layer: bpy.props.StringProperty(
        name="layer",
        description="Enter layer separated by commas",
        default=""
    )

    @classmethod
    def poll(cls, context):   
        return context.selected_objects

    def execute(self, context):
        ops.data.set_custom_property(context.selected_objects, 'layer', self.layer)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}

    def invoke(self, context, event):
        # This invoke function opens the operator's properties before executing it.
        self.layer = ""
        return context.window_manager.invoke_props_dialog(self)


class AM_CP_Remove_Layer(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_layer'
    bl_label = 'Remove ::  layer'
    bl_description = 'Remove Custom Property ::  layer'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = context.selected_objects     
        return objs and len(ops.data.with_custom_property(objs, 'layer')) > 0

    def execute(self, context):
        ops.data.remove_custom_property(context.selected_objects, 'layer')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}
    

class AM_CP_Add_Tags(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_tags'
    bl_label = 'Add :: tags'
    bl_description = 'Add Custom Property :: tags'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    tags_to_add: bpy.props.StringProperty(
        name="Tags",
        description="Enter tags separated by commas",
        default=""
    )

    @classmethod
    def poll(cls, context):   
        return context.selected_objects

    def execute(self, context):
        tags_to_add_list = [tag.strip() for tag in self.tags_to_add.split(',')]
        for obj in context.selected_objects:
            existing_tags_list = [tag.strip() for tag in (ops.data.get_custom_property_value(obj, 'tags') or "").split(',')]
            combined_tags = ','.join(set(existing_tags_list + tags_to_add_list))
            ops.data.set_custom_property(obj, 'tags', combined_tags.strip(','))

        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}

    def invoke(self, context, event):
        # This invoke function opens the operator's properties before executing it.
        self.tags_to_add = ""
        return context.window_manager.invoke_props_dialog(self)



class AM_CP_Remove_Tags(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_tags'
    bl_label = 'Remove ::  tags'
    bl_description = 'Remove Custom Property ::  tags'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = context.selected_objects     
        return objs and len(ops.data.with_custom_property(objs, 'tags')) > 0

    def execute(self, context):
        ops.data.remove_custom_property(context.selected_objects, 'tags')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}
    

class AM_CP_Add_GL_SeaparateCullingPass(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_separate_culling_pass'
    bl_label = 'Add ::  gl_separate_culling_pass'
    bl_description = 'Add Custom Property ::  gl_separate_culling_pass'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and not len(ops.data.with_custom_property(objs, 'gl_separate_culling_pass')) == len(objs)

    def execute(self, context):
        ops.data.set_custom_property(
            context.selected_objects, 'gl_separate_culling_pass', 1.0)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_GL_SeaparateCullingPass(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_separate_culling_pass'
    bl_label = 'Remove ::  gl_separate_culling_pass'
    bl_description = 'Remove Custom Property ::  gl_separate_culling_pass'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and ops.data.with_custom_property(objs, 'gl_separate_culling_pass')

    def execute(self, context):
        ops.data.remove_custom_property(
            context.selected_objects, 'gl_separate_culling_pass')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Add_GL_AlphaIndex(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_alpha_index'
    bl_label = 'Add ::  gl_alpha_index'
    bl_description = 'Add Custom Property ::  gl_alpha_index'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and not len(ops.data.with_custom_property(objs, 'gl_alpha_index')) == len(objs)

    def execute(self, context):
        ops.data.set_custom_property(
            context.selected_objects, 'gl_alpha_index', -10)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_GL_AlphaIndex(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_alpha_index'
    bl_label = 'Remove ::  gl_alpha_index'
    bl_description = 'Remove Custom Property ::  gl_alpha_index'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and ops.data.with_custom_property(objs, 'gl_alpha_index')

    def execute(self, context):
        objs = of_type(context.selected_objects, 'MESH')
        ops.data.remove_custom_property(objs, 'gl_alpha_index')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Add_GL_DepthPrePass(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_depth_pre_pass'
    bl_label = 'Add ::  gl_depth_pre_pass'
    bl_description = 'Add Custom Property ::  gl_depth_pre_pass'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and not len(ops.data.with_custom_property(objs, 'gl_depth_pre_pass')) == len(objs)

    def execute(self, context):
        objs = of_type(context.selected_objects, 'MESH')
        ops.data.set_custom_property(objs, 'gl_depth_pre_pass', 1.0)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_GL_DepthPrePass(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_depth_pre_pass'
    bl_label = 'Remove ::  gl_depth_pre_pass'
    bl_description = 'Remove Custom Property ::  gl_depth_pre_pass'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and ops.data.with_custom_property(objs, 'gl_depth_pre_pass')

    def execute(self, context):
        objs = of_type(context.selected_objects, 'MESH')
        ops.data.remove_custom_property(objs, 'gl_depth_pre_pass')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}

class AM_CP_Add_GL_Translucency(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_translucency'
    bl_label = 'Add ::  gl_translucency'
    bl_description = 'Add Custom Property ::  gl_translucency'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and not len(ops.data.with_custom_property(objs, 'gl_translucency')) == len(objs)

    def execute(self, context):
        objs = of_type(context.selected_objects, 'MESH')
        ops.data.set_custom_property(objs, 'gl_translucency', 1.0)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_GL_Translucency(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_translucency'
    bl_label = 'Remove ::  gl_translucency'
    bl_description = 'Remove Custom Property ::  gl_translucency'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and ops.data.with_custom_property(objs, 'gl_translucency')

    def execute(self, context):
        objs = of_type(context.selected_objects, 'MESH')
        ops.data.remove_custom_property(objs, 'gl_translucency')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Add_GL_BlendMultiply(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_blend_multiply'
    bl_label = 'Add ::  gl_blend_multiply'
    bl_description = 'Add Custom Property ::  gl_blend_multiply'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and not len(ops.data.with_custom_property(objs, 'gl_blend_multiply')) == len(objs)

    def execute(self, context):
        objs = of_type(context.selected_objects, 'MESH')
        ops.data.set_custom_property(objs, 'gl_blend_multiply', 1.0)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_GL_BlendMultiply(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_blend_multiply'
    bl_label = 'Remove ::  gl_blend_multiply'
    bl_description = 'Remove Custom Property ::  gl_blend_multiply'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and ops.data.with_custom_property(objs, 'gl_blend_multiply')

    def execute(self, context):
        objs = of_type(context.selected_objects, 'MESH')
        ops.data.remove_custom_property(objs, 'gl_blend_multiply')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


# @TODO: move implementation
class AM_CP_Add_GL_VertexColorMetallicRougness(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_vertex_color_metallic_roughness'
    bl_label = 'Add ::  gl_vertex_color_metallic_roughness'
    bl_description = 'Add Custom Property ::  gl_vertex_color_metallic_roughness'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        l = len(objs)
        return objs and not len(ops.data.with_custom_property(objs, 'gl_vertex_color')) == l and not len(ops.data.with_custom_property(objs, 'gl_metallic_roughness')) == l

    def execute(self, context):
        objs = of_type(context.selected_objects, 'MESH')
        ops.data.add_color_attribute(objs, 'gl_color')
        ops.data.add_color_attribute(objs, 'gl_metallic_roughness')
        ops.data.set_custom_property(objs, 'gl_vertex_color', 1)
        ops.data.set_custom_property(objs, 'gl_vertex_metallic_roughness', 1)

        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


# @TODO: move implementation
class AM_CP_Remove_GL_VertexColorMetallicRougness(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_vertex_color_metallic_roughness'
    bl_label = 'Remove ::  gl_vertex_color_metallic_roughness'
    bl_description = 'Remove Custom Property ::  gl_vertex_color_metallic_roughness'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and ops.data.with_custom_property(objs, 'gl_vertex_metallic_roughness') and ops.data.with_custom_property(objs, 'gl_vertex_color')

    def execute(self, context):
        objs = objs
        ops.data.remove_custom_property(objs, 'gl_vertex_metallic_roughness')
        ops.data.remove_custom_property(objs, 'gl_vertex_color')
        ops.data.remove_color_attribute(objs, 'gl_color')
        ops.data.remove_color_attribute(objs, 'gl_metallic_roughness')

        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Add_GL_Lightmap(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_lightmap'
    bl_label = 'Add ::  gl_lightmap'
    bl_description = 'Add Custom Property ::  gl_lightmap'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):        
        objs = of_type(context.selected_objects, 'MESH')
        return objs and not len(ops.data.with_custom_property(objs, 'gl_lightmap')) == len(objs)

    def execute(self, context):
        objs = of_type(context.selected_objects, 'MESH')
        ops.data.set_custom_property(objs, 'gl_lightmap', 1)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_GL_Lightmap(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_lightmap'
    bl_label = 'Remove ::  gl_lightmap'
    bl_description = 'Remove Custom Property ::  gl_lightmap'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and ops.data.with_custom_property(objs, 'gl_lightmap')

    def execute(self, context):
        objs = of_type(context.selected_objects, 'MESH')
        ops.data.remove_custom_property(objs, 'gl_lightmap')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Add_Cast_Shadows(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_cast_shadows'
    bl_label = 'Add ::  gl_cast_shadows'
    bl_description = 'Add Custom Property ::  gl_cast_shadows'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):   
        objs = of_type(context.selected_objects, 'MESH')    
        return objs and not len(ops.data.with_custom_property(objs, 'gl_cast_shadows')) == len(objs)

    def execute(self, context):
        ops.data.set_custom_property(context.selected_objects, 'gl_cast_shadows', 1)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_Cast_Shadows(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_cast_shadows'
    bl_label = 'Remove ::  gl_cast_shadows'
    bl_description = 'Remove Custom Property ::  gl_cast_shadows'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')    
        return objs and len(ops.data.with_custom_property(objs, 'gl_cast_shadows')) > 0

    def execute(self, context):
        ops.data.remove_custom_property(context.selected_objects, 'gl_cast_shadows')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Add_Render_Layer(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_gl_render_layer'
    bl_label = 'Add ::  gl_render_layer'
    bl_description = 'Add Custom Property ::  gl_render_layer'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):   
        objs = of_type(context.selected_objects, 'MESH')  
        return objs and not len(ops.data.with_custom_property(objs, 'gl_render_layer')) == len(objs)

    def execute(self, context):
        ops.data.set_custom_property(context.selected_objects, 'gl_render_layer', 0)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_Render_Layer(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_gl_render_layer'
    bl_label = 'Remove ::  gl_render_layer'
    bl_description = 'Remove Custom Property ::  gl_render_layer'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and len(ops.data.with_custom_property(objs, 'gl_render_layer')) > 0

    def execute(self, context):
        objs = of_type(context.selected_objects, 'MESH')
        ops.data.remove_custom_property(objs, 'gl_render_layer')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}



class AM_CP_Add_Collider_Sphere(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_collider_sphere'
    bl_label = 'Add ::  collider_sphere'
    bl_description = 'Add Custom Property ::  collider_sphere'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):        
        objs = context.selected_objects
        return objs and not len(ops.data.with_custom_property(objs, 'collider_sphere')) == len(objs)

    def execute(self, context):
        objs = of_type(context.selected_objects, 'EMPTY')
        spheres = (o for o in objs if o.empty_display_type == 'SPHERE')

        ops.data.set_custom_property(spheres, 'collider_sphere', 1.0)
        ops.data.add_driver_var(spheres,'collider_sphere', 'scale_x', 'TRANSFORMS', 'scale[0]', 'SCALE_X')
        ops.data.add_driver_var(spheres,'collider_sphere', 'scale_y', 'TRANSFORMS', 'scale[1]', 'SCALE_Y')
        ops.data.add_driver_var(spheres,'collider_sphere', 'scale_z', 'TRANSFORMS', 'scale[2]', 'SCALE_Z')
        ops.data.add_driver_var(spheres,'collider_sphere', 'size', 'SINGLE_PROP', 'empty_display_size')
        ops.data.add_driver_expression(spheres,'collider_sphere', '(scale_x + scale_y + scale_z) / 3 * size')

        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_Collider_Sphere(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_collider_sphere'
    bl_label = 'Remove ::  collider_sphere'
    bl_description = 'Remove Custom Property ::  collider_sphere'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = context.selected_objects
        return objs and ops.data.with_custom_property(objs, 'collider_sphere')

    def execute(self, context):
        ops.data.remove_custom_property(context.selected_objects, 'collider_sphere')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Add_Collider_Mesh(bpy.types.Operator):
    bl_idname = 'amblender.cp_add_collider_mesh'
    bl_label = 'Add ::  collider_mesh'
    bl_description = 'Add Custom Property ::  collider_mesh'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):   
        objs = of_type(context.selected_objects, 'MESH')
        return objs and not len(ops.data.with_custom_property(objs, 'collider_mesh')) == len(objs)

    def execute(self, context):
        ops.data.set_custom_property(context.selected_objects, 'collider_mesh', 1)
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}


class AM_CP_Remove_Collider_Mesh(bpy.types.Operator):
    bl_idname = 'amblender.cp_remove_collider_mesh'
    bl_label = 'Remove ::  collider_mesh'
    bl_description = 'Remove Custom Property ::  collider_mesh'
    bl_options = {'REGISTER', 'INTERNAL', 'UNDO'}

    @classmethod
    def poll(cls, context):
        objs = of_type(context.selected_objects, 'MESH')
        return objs and len(ops.data.with_custom_property(objs, 'collider_mesh')) > 0

    def execute(self, context):
        ops.data.remove_custom_property(context.selected_objects, 'collider_mesh')
        ops.ui.redraw(SpaceType.PROPERTIES)

        return {'FINISHED'}

    
classes = (
            AM_CP_Set_Layer,
            AM_CP_Remove_Layer,
            AM_CP_Add_Tags,
            AM_CP_Remove_Tags,
            AM_CP_Add_GL_SeaparateCullingPass,
            AM_CP_Remove_GL_SeaparateCullingPass,
            AM_CP_Add_GL_AlphaIndex,
            AM_CP_Remove_GL_AlphaIndex,
            AM_CP_Add_GL_Translucency, AM_CP_Remove_GL_Translucency, AM_CP_Add_GL_BlendMultiply, AM_CP_Remove_GL_BlendMultiply, AM_CP_Add_GL_VertexColorMetallicRougness, AM_CP_Remove_GL_VertexColorMetallicRougness,
            AM_CP_Add_GL_Lightmap,
            AM_CP_Remove_GL_Lightmap,
            AM_CP_Add_Render_Layer,
            AM_CP_Remove_Render_Layer,
            AM_CP_Add_Collider_Sphere,
            AM_CP_Remove_Collider_Sphere,
            AM_CP_Add_Collider_Mesh,
            AM_CP_Remove_Collider_Mesh,
            AM_CP_Add_Cast_Shadows,
            AM_CP_Remove_Cast_Shadows,
           )


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
