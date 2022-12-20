import typing
import bpy
from bpy.types import *
from ..meta import meta
from .fn import *


class Find:
    @staticmethod
    def users_of(ID: 'ID'):
        def users(col):
            ret = tuple(o for o in col if o.user_of_id(ID))
            return ret if ret else None

        return filter(None, (
            users(getattr(bpy.data, p))
            for p in dir(bpy.data)
            if isinstance(
                getattr(bpy.data, p, None),
                bpy.types.bpy_prop_collection
            )
        )
        )


find = Find()
