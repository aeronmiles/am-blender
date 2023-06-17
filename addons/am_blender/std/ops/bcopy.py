from ...std import *


class Copy:
    @staticmethod
    @log.catch
    def transform(source_obj: 'Object', dest_obj: 'Object'):
        dest_obj.location = source_obj.location
        dest_obj.rotation_euler = source_obj.rotation_euler
        dest_obj.scale = source_obj.scale

    @staticmethod
    @log.catch
    def collections(source_obj: 'Object', dest_obj: 'Object'):
        for c in source_obj.users_collection:
            c.objects.link(dest_obj)

    @staticmethod
    @log.catch
    def childs(source_obj: 'Object', dest_obj: 'Object'):
        childs = source_obj.children
        for c in childs:
            c.parent = dest_obj
            c.matrix_parent_inverse = dest_obj.matrix_world.inverted()

    @staticmethod
    @log.catch
    def duplicate_to_others(source_obj: 'Object', objs: Union['Object', Iterable['Object']], linked: bool = True):
        objs = as_iterable(objs)

        # collect transforms of all objects except active
        transforms = []
        for obj in objs:
            if obj == source_obj:
                continue

            transforms.append(obj.matrix_world.copy())

        # duplicate linked active object to all transform locations and orientations
        for transform in transforms:
            if transform == source_obj.matrix_world:
                continue
            
            bpy.ops.object.select_all(action='DESELECT')
            source_obj.select_set(True)
            bpy.ops.object.duplicate(linked=linked)
            dup = bpy.context.selected_objects[0]
            dup.matrix_world = transform

    @staticmethod
    @log.catch
    def pivot(source_obj: 'Object', objs: Union['Object', Iterable['Object']]):
        objs = as_iterable(objs)
        for obj in objs:
            # Ensure obj is a mesh object and obj_B is any object
            if obj.type != 'MESH':
                pass

            # Get the world matrix of obj_B relative to obj
            offsetMatrix = source_obj.matrix_world.inverted() @ obj.matrix_world

            # Extract the translation, rotation, and scale components from the matrix
            translation_offset, rotation_offset, scale_offset = offsetMatrix.decompose()

            # Offset the mesh data of obj
            mesh_data = obj.data
            for vertex in mesh_data.vertices:
                vertex.co.rotate(rotation_offset)
                vertex.co *= scale_offset
                vertex.co += translation_offset

            obj.matrix_world = source_obj.matrix_world

    

copy = Copy()
