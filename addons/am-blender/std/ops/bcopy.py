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


copy = Copy()
