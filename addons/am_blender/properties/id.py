import time
import bpy
from bpy.types import (PropertyGroup, StringProperty, ID)
from bpy.props import *
from bpy.app.handlers import persistent
from ..std import (log)


def _on_update(self, context):
    log.info(f"AMBlenderIDProps.on_update({self.id}, {context})")


class AMBlenderIDProps(PropertyGroup):
    id: StringProperty(name="ID", default="", update=_on_update)
    prev_id: StringProperty(name="Previous ID", default="")

    @classmethod
    def register(cls):
        bpy.types.ID.amb_id = PointerProperty(
            name="AMBlender ID",
            description="AMBlender id",
            type=cls
        )

    @classmethod
    def unregister(cls):
        del bpy.types.ID.amb_id


def _check_ids(objs):
    for obj in objs:
        if obj.amb_id.id != obj.name:
            obj.amb_id.prev_id = obj.amb_id.id
            obj.amb_id.id = obj.name


@persistent
def _update_ids(self, context):
    start = time.time()
    _check_ids(bpy.data.objects)
    _check_ids(bpy.data.materials)
    log.info(
        f'AMBlenderIDProps._update_ids() took {time.time() - start} seconds. (1 thread)')



# @TODO: this is way too slow, look into implementing persistent UUID in Blender Source: https://developer.blender.org/T83019
bpy.app.handlers.depsgraph_update_post.append(_update_ids)
