import typing
from bpy.types import *
from ..meta import meta
from .fn import *


class Shader:
    @staticmethod
    def disconnect_inputs(objs: typing.Union[typing.Iterable['Object'], 'Object'], node_type: type, input: str):
        for obj in as_iterable(objs):
            for ms in obj.material_slots:
                mat = ms.material
                mat.use_nodes = True
                nodes = (
                    n for n in mat.node_tree.nodes if isinstance(n, node_type))

                for node in nodes:
                    if node.inputs.find(input) > -1:
                        for l in node.inputs[input].links:
                            mat.node_tree.links.remove(l)


shader = Shader()
