import bpy
from bpy.types import (PropertyGroup, StringProperty)
from bpy.props import *
import uuid
from bpy.app.handlers import persistent
from ..std import log


class AMBlenderIDProps(PropertyGroup):
    id: StringProperty(name="ID", default="")

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


ID_OBJS = set()
ID_MATS = set()


def _set_ids(objs, id_refs):
    for obj in objs:
        if obj not in id_refs:
            log.info(f"Adding {obj} id: {obj.amb_id.id}")
            id_refs.add(obj)


def _set_ids_new(objs, id_refs):
    for obj in objs:
        if obj not in id_refs:
            obj.amb_id.id = str(uuid.uuid4().hex)
            log.info(f"Adding {obj} id: {obj.amb_id.id}")
            id_refs.add(obj)


def _clean_void_ids(objs, id_refs):
    void_objs = id_refs - set(objs)
    for obj in void_objs:
        if obj in id_refs:
            log.info(f"Removing {obj} id: {obj.amb_id.id}")
            id_refs.remove(obj)


@persistent
def set_ids(arg):
    _set_ids(bpy.data.objects.values(), ID_OBJS)
    _set_ids(bpy.data.materials.values(), ID_MATS)


@persistent
@log.catch
def update_ids(self, context):
    _clean_void_ids(bpy.data.objects.values(), ID_OBJS)
    _clean_void_ids(bpy.data.materials.values(), ID_MATS)

    _set_ids_new(bpy.data.objects.values(), ID_OBJS)
    _set_ids_new(bpy.data.materials.values(), ID_OBJS)


# handlers
# bpy.app.handlers.load_post.append(set_ids)
# bpy.app.handlers.depsgraph_update_post.append(update_ids)
