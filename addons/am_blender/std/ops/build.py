from ..fn import *
from ..types import *
from .. import *
from . import *

class Build:
    @staticmethod
    @log.catch
    def empty_mesh(name: str = "EmptyMesh") -> 'Object':
        mesh = bpy.data.meshes.new('EmptyMesh')
        mesh.from_pydata([], [], [])
        mesh.update()
        obj = bpy.data.objects.new('EmptyMesh', mesh)
        obj.name = name
        return obj
    
    @staticmethod
    @log.catch
    def collider_sphere(objs: Union[Iterable['Mesh'], 'Mesh']):
        """
        Create a collider sphere for each object in the list. The collider sphere is parented to the object and is scaled to fit the object's bounding box.

        Parameters:
        - objs: The objects to check for the custom property.
        """
        objs = as_iterable(objs)
        collider_objs = []  # To keep track of newly created collider objects
        # Deselect all objects to start freshA
        bpy.ops.object.select_all(action='DESELECT')

        for obj in objs:
            xform = obj.matrix_world.copy()
            bounds_center = sum((Vector(b) for b in obj.bound_box), Vector()) / 8
            world_center = xform @ bounds_center
            radius = max(map(lambda v: (xform @ v.co - world_center).length, obj.data.vertices)) 
            radius += 0.02
            bpy.ops.object.empty_add(type='SPHERE', radius=radius, align='WORLD', location=world_center, scale=(1, 1, 1))
            collider = bpy.context.active_object
            collider.parent = obj
            collider.location = world_center
            collider.name = obj.name + "_collider_sphere"
            collider_objs.append(collider)
            if not bpy.data.collections.get('Colliders'):
                bpy.data.collections.new('Colliders')

            collider.users_collection = 'Colliders'

        data.set_custom_property(collider_objs, 'collider_sphere', 1.0)
        data.add_driver_var(collider_objs,'collider_sphere', 'scale_x', DriverVarType.TRANSFORMS, 'scale[0]', 'SCALE_X')
        data.add_driver_var(collider_objs,'collider_sphere', 'scale_y', DriverVarType.TRANSFORMS, 'scale[1]', 'SCALE_Y')
        data.add_driver_var(collider_objs,'collider_sphere', 'scale_z', DriverVarType.TRANSFORMS, 'scale[2]', 'SCALE_Z')
        data.add_driver_var(collider_objs,'collider_sphere', 'size', 'SINGLE_PROP', 'empty_display_size')
        data.add_driver_expression(collider_objs,'collider_sphere', '(scale_x + scale_y + scale_z) / 3 * size')

        # Select all new collider models
        bpy.ops.object.select_all(action='DESELECT')
        for collider_obj in collider_objs:
            collider_obj.select_set(True)
        
    @staticmethod
    @log.catch
    def collider_mesh(objs: Union[Iterable['Mesh'], 'Mesh']):
        """
        Create a collider mesh for each object in the list. The collider mesh is parented to the object and is scaled to fit the object's bounding box.
        
        Parameters:
        - objs: The objects to check for the custom property.
        """
        objs = as_iterable(objs)

        # Check if the "collider" material exists, if not create it
        collider_material = bpy.data.materials.get("collider")
        if not collider_material:
            collider_material = bpy.data.materials.new(name="collider")
            collider_material.use_nodes = True
            collider_material.blend_method = 'BLEND'  # Set alpha blend mode
            collider_material.use_backface_culling = True  # Enable backface culling

            # Ensure Principled BSDF shader is used and set its Alpha value
            if collider_material.node_tree:
                node_tree = collider_material.node_tree
                principled_node = node_tree.nodes.get('Principled BSDF')
                if principled_node:
                    principled_node.inputs["Base Color"].default_value = (1.0, 0.0, 0.0, 1.0)
                    principled_node.inputs["Alpha"].default_value = 0.2

        # Deselect all objects to start fresh
        bpy.ops.object.select_all(action='DESELECT')

        collider_objs = []  # To keep track of newly created collider objects

        for obj in objs:
            # Duplicate the object
            obj.select_set(True)
            name = obj.name
            bpy.ops.object.duplicate()
            collider = bpy.context.active_object
            collider.users_collection = 'Colliders'
            xform = collider.matrix_world.copy()
            collider.parent = obj
            collider.matrix_world = xform
            # append collider mesh name
            collider.name = name + "_collider_mesh"
            # disable rendering
            collider.hide_render = True
            # apply all modifiers
            bpy.ops.object.convert(target='MESH')
            # add decimate modifier
            bpy.ops.object.modifier_add(type='DECIMATE')
            # set decimate ratio
            collider.modifiers["Decimate"].ratio = 0.2
            collider_objs.append(collider)  # Add to the list
            data.set_custom_property(collider, 'collider_mesh', 1)

            # Convert the duplicated object to a convex hull
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.convex_hull()
            bpy.ops.object.mode_set(mode='OBJECT')

            # Assign the collider material
            collider.data.materials.clear()
            collider.data.materials.append(collider_material)

        # Select all new collider models
        bpy.ops.object.select_all(action='DESELECT')
        for collider_obj in collider_objs:
            collider_obj.select_set(True)


build = Build()
