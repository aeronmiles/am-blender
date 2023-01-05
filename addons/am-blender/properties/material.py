import bpy
from bpy.types import (PropertyGroup, StringProperty)
from bpy.props import *


class AMBlenderMaterialProps(PropertyGroup):
    lod: IntProperty(name="LOD", default=0)
    # auto_vp_color: BoolProperty(name="Automatic Viewport Color", default=True,
    #                             update=update_auto_vp_color,
    #                             description="Automatically choose a viewport color "
    #                             "from the first nodes in the node tree")
    # node_tree: PointerProperty(name="Node Tree", type=bpy.types.NodeTree)
    # preview: PointerProperty(type=LuxCoreMaterialPreviewProps)

    # use_cycles_nodes: BoolProperty(name="Use Cycles Nodes", default=False, update=update_use_cycles_nodes,
    #                                description="Use the Cycles nodes of this material instead of the LuxCore node tree "
    #                                            "(WARNING: This option is not fully implemented yet, only very few nodes work)")

    @classmethod
    def register(cls):
        bpy.types.Material.amb_mat = PointerProperty(
            name="AMBlender Material",
            description="AMBlender material",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del bpy.types.Material.amb_mat
