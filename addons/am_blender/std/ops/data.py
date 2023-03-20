from ...std import *
from ...std import ops

bpy.ops.outliner.show_hierarchy


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
            if name in obj:
                log.info(f'ops.data.set_custom_property(objs={objs}, name={name}, value={value}) :: Overwriting custom property "{name}" on object "{obj.name}" with value "{value}"')
                obj[name] = value

    @staticmethod
    @log.catch
    def with_custom_property(objs: Union[Iterable['Object'], 'Object'], name: str) -> set['Object']:
        objs = []
        for obj in as_iterable(objs):
            if name in obj:
                objs.append(obj)

        return set(objs)

    @staticmethod
    @log.catch
    def remove_custom_property(objs: Union[Iterable['Object'], 'Object'], name: str):
        for obj in as_iterable(objs):
            if name in obj:
                try:
                    del obj[name]
                except Exception as e:
                    log.error(
                        f'ops.data.remove_custom_property(objs={objs}, name={name}) :: Failed to remove custom property from object "{obj.name}" Exception: {e}')

    @staticmethod
    @log.catch
    def unpack_images():
        bpy.data.use_autopack = False

        bpy.ops.object.mode_set(mode='OBJECT')
        packed = [(img, img.packed_files)
                  for img in bpy.data.images if img.packed_file]

        for img, pfs in packed:
            for pf in pfs:
                pf.filepath = os.path.join(os.path.dirname(
                    bpy.data.filepath), meta.cfg.unpack_tex_dir, img.name + f".{img.file_format}".lower())
                pf.save()
            img.unpack()

    # TODO: sort out texture referencing and naming system
    @staticmethod
    @log.catch
    def reset_scaled_images(objs: Union[Iterable['Object'], 'Object']):
        bpy.ops.object.mode_set(mode='OBJECT')
        nodes: set['ShaderNodeTexImage'] = ops.shader.node.of_type(
            objs, bpy.types.ShaderNodeTexImage)

        for node in nodes:
            img = node.image
            if not img:
                continue

            scaled = Size.from_name(img.filepath_raw)
            if scaled:
                filepath = replace(
                    img.filepath, scaled.compat.filename_suffixes(), ".")
                ops.shader.node.load_image(node, filepath)

    # TODO: sort out texture referencing and naming system
    @staticmethod
    @log.catch
    def scale_images_to_maxsize(nodes: Union[Iterable['ShaderNodeTexImage'], 'ShaderNodeTexImage'], scale: 'Size'):
        if bpy.data.use_autopack:
            Data.unpack_images()

        bpy.ops.object.mode_set(mode='OBJECT')
        _nodes = as_iterable(nodes)
        for node in _nodes:
            img = node.image
            if not img:
                continue

            # img.file_format = 'PNG'

            # try load image
            scaled = Size.from_name(img.filepath_raw)
            filepath = img.filepath_raw
            if scaled:
                filepath = replace(
                    img.filepath_raw, scaled.compat.filename_suffixes(), ".")
                img = bpy.data.images.load(filepath, check_existing=True)
            
            log.info(f'ops.data.scale_images_to_maxsize() :: Rescaling image "{img.filepath_raw}" to {scale.name}')

            filepath = os.path.splitext(filepath)[0]

            img_path = filepath + scale.filename_suffix() + \
                f"{img.file_format}".lower()

            log.info(f'ops.data.scale_images_to_maxsize() :: Loading image "{img_path}"')

            # if ops.shader.node.load_image(node, img_path):
            #     continue

            # load image fail -> rescale existing texture
            f = scale.value / max(img.size[0], img.size[1])

            img.scale(int(img.size[0] * f), int(img.size[1] * f))

            img.filepath_raw = img_path
            # TODO: add name length checks
            img.name = os.path.basename(bpy.path.abspath(img_path))

            img.save()
            ops.shader.node.load_image(node, img.filepath_raw)


data = Data()
