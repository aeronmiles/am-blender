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

            scaled = Size.from_image(img)
            if scaled:
                filepath = replace(
                    img.filepath, scaled.compat.filename_suffixes(), ".")
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
            filepath = img.filepath_raw
            if scaled:
                filepath = replace(
                    img.filepath_raw, scaled.compat.filename_suffixes(), ".")
                img = bpy.data.images.load(filepath, check_existing=True)
                
            filepath = os.path.splitext(filepath)[0]

            img_path = filepath + scale.filename_suffix() + f"{img.file_format}".lower()

            if ops.shader.load_image(node, img_path):
                continue
            
            # rescale existing texture
            f = scale.value / max(img.size[0], img.size[1])

            img.scale(int(img.size[0] * f), int(img.size[1] * f))

            img.filepath_raw = img_path
            img.name = os.path.basename(bpy.path.abspath(img_path))

            img.save()
            ops.shader.load_image(node, img.filepath_raw)


data = Data()
