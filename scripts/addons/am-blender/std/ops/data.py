import os
import typing
import bpy
from bpy.types import *
from ..meta import meta
from .fn import *
from ..dtypes import *

class Data:
    @staticmethod
    def unlink(objs: typing.Union[typing.Iterable['Object'], 'Object']):
        for obj in as_iterable(objs):
            bpy.data.objects.remove(obj, do_unlink=True)

    @staticmethod
    def set_custom_property(objs: typing.Union[typing.Iterable['Object'], 'Object'], name: str, value):
        for obj in as_iterable(objs):
            obj[name] = value

    @staticmethod
    def remove_custom_property(objs: typing.Union[typing.Iterable['Object'], 'Object'], name: str):
        for obj in as_iterable(objs):
            try:
                del obj[name]
            except:
                pass

    @staticmethod
    def unpack_images():
        packed = [(img, img.packed_files)
                  for img in bpy.data.images if img.packed_file]
        for img, pfs in packed:
            for pf in pfs:
                pf.filepath = os.path.join(os.path.dirname(
                    bpy.data.filepath), meta.cfg.unpack_tex_dir, img.name + f".{img.file_format}".lower())
                pf.save()
            img.unpack()

    @staticmethod
    def reset_scaled_images(objs: typing.Union[typing.Iterable['Object'], 'Object']):
        nodes = []
        for obj in as_iterable(objs):
            for ms in obj.material_slots:
                mat = ms.material
                mat.use_nodes = True
                nodes.extend((n for n in mat.node_tree.nodes if isinstance(
                    n, bpy.types.ShaderNodeTexImage)))

        for node in nodes:
            img = node.image
            if not img:
                continue

            scale = ImageScale.from_image(img)
            appended = ""
            if scale:
                appended = scale.append_str()                

            image = bpy.data.images.load(
                node.image.filepath.replace(appended, ""), check_existing=True)
            if image:
                # node settings
                interp = node.interpolation
                proj = node.projection
                extension = node.extension
                color = node.image.colorspace_settings.name
                alpha = node.image.alpha_mode

                node.image = image

                # restore previous node settings
                node.interpolation = interp
                node.projection = proj
                node.extension = extension
                node.image.colorspace_settings.name = color
                node.image.alpha_mode = alpha

    @staticmethod
    def scale_images_to_maxsize(objs: typing.Union[typing.Iterable['Object'], 'Object'], scale: 'ImageScale'):
        nodes = []

        for obj in as_iterable(objs):
            for ms in obj.material_slots:
                mat = ms.material
                mat.use_nodes = True
                nodes.extend((n for n in mat.node_tree.nodes if isinstance(
                    n, bpy.types.ShaderNodeTexImage)))

        for node in nodes:
            img = node.image
            if not img:
                continue

            # scale current image
            maxD = max(img.size[0], img.size[1])
            if not maxD > scale.value:
                continue

            # check for exisiting scaled image
            imgPath = os.path.join(os.path.dirname(
                bpy.data.filepath), meta.cfg.unpack_tex_dir, os.path.splitext(
                img.name)[0] + scale.append_str() + f".{img.file_format}".lower())

            try:
                image = bpy.data.images.load(imgPath, check_existing=True)
                node.image = image
                continue
            except:
                pass

            # rescale existing texture
            f = scale.value / maxD

            img.scale(int(img.size[0] * f), int(img.size[1] * f))

            img.filepath_raw = os.path.splitext(img.filepath_raw)[0] + \
                f"{scale.append_str()}." + img.file_format.lower()
            img.name = os.path.splitext(
                img.name)[0] + scale.append_str() + f".{img.file_format}".lower()

            img.save()
            node.image = bpy.data.images.get(img.name)


data = Data()
