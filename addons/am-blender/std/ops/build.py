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


build = Build()
