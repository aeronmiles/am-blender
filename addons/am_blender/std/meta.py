import os
import bpy


class Cfg(object):
    def __init__(self) -> None:
        self.log_to_txt = True
        self.install_packages = True
        self.unpack_tex_dir = "textures"
        # this should be used with caution, with large scenes, interaction can be slowed
        self._use_internal_ids = False

    @property
    def use_internal_ids(self) -> bool:
        return self._use_internal_ids

    @use_internal_ids.setter
    def use_internal_ids(self, value: bool):
        self._use_internal_ids = value
        if value:
            bpy.context.scene.use_fake_user = True
        else:
            bpy.context.scene.use_fake_user = False


class MetaData(object):
    def __init__(self) -> None:
        self.cfg = Cfg()

    @property
    def datafile_dir(self) -> str:
        return os.path.join(os.path.dirname(
            os.path.realpath(__file__)),  '..', 'datafiles')

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
        if 'startup.blend' in bpy.context.blend_data.filepath:
            meta.user_clear()

        import jsonpickle as jp
        meta.write(jp.encode(self, indent=2))


meta = MetaData()
