from ...std import *
from ...std import ops


class Data:
    @staticmethod
    @log.catch
    def unlink(objs: Union[Iterable['Object'], 'Object']):
        for obj in as_iterable(objs):
            bpy.data.objects.remove(obj, do_unlink=True)

    @staticmethod
    @log.catch
    def set_custom_property(objs: Union[Iterable['Object'], 'Object'], name: str, value):
        for obj in as_iterable(objs):
            obj[name] = value

    @staticmethod
    @log.catch
    def remove_custom_property(objs: Union[Iterable['Object'], 'Object'], name: str):
        for obj in as_iterable(objs):
            try:
                del obj[name]
            except:
                pass

    @staticmethod
    @log.catch
    def unpack_images():
        bpy.ops.object.mode_set(mode='OBJECT')
        packed = [(img, img.packed_files)
                  for img in bpy.data.images if img.packed_file]
        for img, pfs in packed:
            for pf in pfs:
                pf.filepath = os.path.join(os.path.dirname(
                    bpy.data.filepath), meta.cfg.unpack_tex_dir, img.name + f".{img.file_format}".lower())
                pf.save()
            img.unpack()

    @staticmethod
    @log.catch
    def reset_scaled_images(objs: Union[Iterable['Object'], 'Object']):
        bpy.ops.object.mode_set(mode='OBJECT')
        nodes: List['ShaderNodeTexImage'] = ops.shader.nodes_of_type(
            objs, bpy.types.ShaderNodeTexImage)

        for node in nodes:
            img = node.image
            if not img:
                continue

            scale = Size.from_image(img)
            filename_suffixes = ""
            if scale:
                filename_suffixes = scale.compat.filename_suffixes()

            filepath = replace(img.filepath, filename_suffixes, ".")

            ops.shader.load_image(node, filepath)

    @staticmethod
    @log.catch
    def scale_images_to_maxsize(objs: Union[Iterable['Object'], 'Object'], scale: 'Size'):
        bpy.ops.object.mode_set(mode='OBJECT')

        nodes: List['ShaderNodeTexImage'] = ops.shader.nodes_of_type(
            objs, bpy.types.ShaderNodeTexImage)

        for node in nodes:
            img = node.image
            if not img:
                continue

            scaled = Size.from_image(img)
            filepath = img.filepath

            if scaled:
                for filename_suffix in scaled.compat.filename_suffixes():
                    filepath = filepath.replace(filename_suffix, ".")

            print(f"filepath: {filepath}")

            # check for exisiting scaled image
            imgPath = os.path.join(os.path.dirname(
                bpy.data.filepath), meta.cfg.unpack_tex_dir, os.path.splitext(
                filepath)[0] + scale.filename_suffix() + f"{img.file_format}".lower())

            # scale current image
            maxD = max(img.size[0], img.size[1])
            if not maxD > scale.value:
                ops.shader.load_image(node, imgPath)
                continue
            elif ops.shader.load_image(node, imgPath):
                continue

            # rescale existing texture
            f = scale.value / maxD

            img.scale(int(img.size[0] * f), int(img.size[1] * f))

            img.filepath = os.path.splitext(img.filepath)[0] + \
                f"{scale.filename_suffix()}" + img.file_format.lower()
            img.name = os.path.splitext(
                img.name)[0] + scale.filename_suffix() + f"{img.file_format}".lower()

            img.save()
            ops.shader.load_image(node, img.filepath)


data = Data()
