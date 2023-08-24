import shutil
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
    def copy_images_to(images: Union['Image', Iterable['Image']], dest_dir: str):
        _images = as_iterable(images)
        source_dir = os.path.dirname(bpy.data.filepath)
        _dest_dir = os.path.join(source_dir, dest_dir)
        if not os.path.exists(_dest_dir):
            os.makedirs(_dest_dir)
        for img in _images:
            shutil.copy(os.path.join(source_dir, img.filepath), _dest_dir)

    @staticmethod
    @log.catch
    def unpack(images: Union['Image', Iterable['Image']]):
        bpy.data.use_autopack = False

        mode = bpy.context.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        packed = set((img, img.packed_files)
                  for img in images if img.packed_file)

        log.warning(f"@TODO: Fix extension to match source image for .jpg files currently renamed to .jpeg")
        for img, pfs in packed:
            for pf in pfs:
                pf.filepath = os.path.join(os.path.dirname(
                    bpy.data.filepath), meta.cfg.unpack_tex_dir, os.path.splitext(img.name)[0] + f".{img.file_format}".lower())
                pf.save()
            img.unpack()

        bpy.ops.object.mode_set(mode=mode)

    # @staticmethod
    # @log.catch
    # def archive_textures():
    #     # get all image names from local ./texture folder

    #     bpy.data.use_autopack = False
    #     archive_dir = os.path.join(os.path.dirname(
    #         bpy.data.filepath), meta.cfg.archive_dir)

    #     if not os.path.exists(archive_dir):
    #         os.makedirs(archive_dir)

    #     images = os.listdir(os.path.join(bpy.data.filepath, meta.cfg.texture_dir))
    #     # images filenames


    #     # get all image names from all scene materials
    #     imageNodes = ops.shader.node.of_type(bpy.data.materials, bpy.types.ShaderNodeTexImage)
    #     imagesInScene = []
    #     for imgNode in imageNodes:
    #         if imgNode.image:
    #             iamgesInScene.append(imgNode.image.name)
        
        # images filenames


        


    @staticmethod
    @log.catch
    def unpack_connected_images(objs: Union[Iterable['Object'], 'Object']):
        # iterate all image texture nodes in all scene materials, filter all images that are connected to a ShaderNode type node
        bpy.data.use_autopack = False

        _objs = as_iterable(objs)
        imgNodes = ops.shader.node.of_type(_objs, bpy.types.ShaderNodeTexImage)
        for imgNode in imgNodes:
            ds = ops.shader.node.downstream_nodes(imgNode)
            for d in ds:
                if isinstance(d, bpy.types.ShaderNodeOutputMaterial):
                    Data.unpack(imgNode.image)
        

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
        _nodes = as_iterable(set(nodes))
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
