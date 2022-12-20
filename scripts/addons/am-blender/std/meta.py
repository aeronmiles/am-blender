from time import sleep
import jsonpickle
import bpy
from .dtypes import ImageScale


class Cfg(object):
    def __init__(self) -> None:
        self.unpack_tex_dir = "textures"
        self.scale = ImageScale.SCALE_1024


class MetaData(object):
    def __init__(self) -> None:
        self.cfg = Cfg()

    def load(self) -> bool:
        index = bpy.data.texts.find("amblender-metadata")
        if index > -1:
            self = jsonpickle.decode(bpy.data.texts[index].as_string())
            return True
        else:
            self.save()
            return False

    def save(self):
        meta = bpy.data.texts.new("amblender-metadata")
        meta.write(jsonpickle.encode(self, indent=2))


meta = MetaData()
