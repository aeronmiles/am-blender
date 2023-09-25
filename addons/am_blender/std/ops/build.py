from ...std import *

class Build:
    @staticmethod
    @log.catch
    def empty_mesh(name: str = "EmptyMesh") -> 'Object':
        mesh = bpy.data.meshes.new('Empty.Mesh')
        mesh.from_pydata([], [], [])
        mesh.update()
        obj = bpy.data.objects.new('Empty.Mesh', mesh)
        obj.name = name
        return obj

    @staticmethod
    @log.catch
    def collider(objs: Union[Iterable['Object'], 'Object']):
        objs = as_iterable(objs)

        # Check if the "collision" material exists, if not create it
        collision_material = bpy.data.materials.get("collision")
        if not collision_material:
            collision_material = bpy.data.materials.new(name="collision")
            collision_material.diffuse_color = (1.0, 0.0, 0.0, 0.3)  # Red with alpha of 0.3
            collision_material.use_nodes = True
            collision_material.blend_method = 'BLEND'  # Set alpha blend mode
            collision_material.show_backface_culling = True  # Enable backface culling

            # Ensure Principled BSDF shader is used and set its Alpha value
            if collision_material.node_tree:
                node_tree = collision_material.node_tree
                principled_node = node_tree.nodes.get('Principled BSDF')
                if principled_node:
                    principled_node.inputs["Alpha"].default_value = 0.3

        # Deselect all objects to start fresh
        bpy.ops.object.select_all(action='DESELECT')

        collision_objs = []  # To keep track of newly created collision objects

        for obj in objs:
            # Duplicate the object
            obj.select_set(True)
            bpy.ops.object.duplicate()
            duplicated_obj = bpy.context.active_object
            collision_objs.append(duplicated_obj)  # Add to the list

            # Convert the duplicated object to a convex hull
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.convex_hull()
            bpy.ops.object.mode_set(mode='OBJECT')

            # Assign the collision material
            duplicated_obj.data.materials.clear()
            duplicated_obj.data.materials.append(collision_material)

        # Select all new collision models
        for collision_obj in collision_objs:
            collision_obj.select_set(True)


build = Build()
