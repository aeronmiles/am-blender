import bpy


class Cfg(object):
    def __init__(self) -> None:
        self.log_to_txt = True
        self.install_packages = True
        self.unpack_tex_dir = "textures"


class MetaData(object):
    def __init__(self) -> None:
        self.cfg = Cfg()

    def load(self) -> bool:
        index = bpy.data.texts.find("amblender-metadata")
        import jsonpickle as jp
        if index > -1:
            self = jp.decode(bpy.data.texts[index].as_string())
            return True
        else:
            self.save()
            return False

    def save(self):
        meta = bpy.data.texts.new("amblender-metadata")
        import jsonpickle as jp
        meta.write(jp.encode(self, indent=2))


meta = MetaData()
