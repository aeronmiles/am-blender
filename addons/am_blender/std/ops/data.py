import shutil
from ...std import *
from ...std import ops

bpy.ops.outliner.show_hierarchy


class Data:
    @staticmethod
    @log.catch
    def get_driver(obj:'Object', property_path: str):
        """
        Check if the object has a driver for the given property path.
        
        Parameters:
        - obj: The object to check.
        - property_path: The property path to check for a driver.
        
        Returns:
        - True if a driver exists for the property path, False otherwise.
        """
        
        # Check if the object has animation data and drivers
        if obj.animation_data and obj.animation_data.drivers:
            for driver in obj.animation_data.drivers:
                if driver.data_path == property_path:
                    return driver
        return None

    @staticmethod
    @log.catch
    def add_driver_var(objs: Union[Iterable['Object'], 'Object'], property_path: str, var_name: str, var_type: DriverVarType, data_path: str = None, target_type: str = None):
        """Add variables to a driver based on provided details.
        
        Parameters:
        - objs: The objects to add the driver to.
        - property_path: The property path to add the driver to.    
        - var_name: The name of the variable to add.
        - var_type: The type of variable to add.
        - data_path: The data path to use for the variable.
        - target_type: The target type to use for the variable for the following var_types: ('TRANSFORMS', ).
        """
        objs = as_iterable(objs)
        for obj in objs:
            if property_path not in obj:
                log.error(f"Custom property '{property_path}' not found on object '{obj.name}'.")
                return

            driver = Data.get_driver(obj, property_path)
            if property_path in obj.keys(): 
                path = f'["{property_path}"]' 
            else: 
                path = property_path

            if not driver:
                driver = obj.driver_add(path).driver
            
            var = driver.variables.new()
            var.name = var_name
            var.type = var_type.value
            
            if data_path:
                var.targets[0].data_path = data_path
            
            var.targets[0].id = obj
            # @TODO: add target types for 
            if var_type.value == 'TRANSFORMS' and target_type:
                var.targets[0].transform_type = target_type


    @staticmethod
    @log.catch
    def add_driver_expression(objs: Union[Iterable['Object'], 'Object'], property_path: str, expression: str = None):
        """
        Link a property of the objects to a custom property value, with an optional expression.

        Parameters:
        - objs: The objects to link.
        - property_path: The property path to link to.
        - expression: The expression to use for the driver. If not provided, a default expression will be used.
        """
        objs = as_iterable(objs)        
        for obj in objs:
            # Ensure the custom property exists
            if property_path not in obj:
                log.error(f"Custom property '{property_path}' not found on object '{obj.name}'.")
                continue
            
            driver = Data.get_driver(obj, property_path)
            if property_path in obj.keys(): 
                path = f'["{property_path}"]' 
            else: 
                path = property_path
                
            if not driver:
                fcurve = obj.driver_add(path)
                driver = fcurve.driver
                driver.type = 'SCRIPTED'

        # If a lambda expression is provided, set it as the driver's expression
            if expression:
                driver.expression = expression
            else:
                log.error(f"No lambda expression provided for object '{obj.name}'. Using default driver expression.")
    
    @staticmethod
    @log.catch
    def add_color_attribute(objs: Union[Iterable['Object'], 'Object'], name: str):
        objs = as_iterable(objs)
        for obj in objs:
            colors = obj.data.color_attributes
            if colors.find(name) == -1:
                colors.new(name=name,
                            type="FLOAT_COLOR", domain="POINT")
                obj['gl_vertex_color'] = colors.find('gl_color')

            if colors.find("gl_metallic_roughness") == -1:
                colors.new(name="gl_metallic_roughness",
                            type="FLOAT_COLOR", domain="POINT")
                
    @staticmethod
    @log.catch
    def remove_color_attribute(objs: Union[Iterable['Object'], 'Object'], name: str):
        """
        Remove a color attribute from the object's mesh data.
        
        Parameters:
        - objs: The objects to remove the color attribute from.
        - name: The name of the color attribute to remove.
        """
        objs = as_iterable(objs)
        for obj in objs:
            colors = obj.data.color_attributes
            if colors.find(name) != -1:
                colors.remove(colors[name])
                
    @staticmethod
    @log.catch
    def unlink(objs: Union[Iterable['Object'], 'Object']):
        """
        Unlink objects from the scene.
        
        Parameters:
        - objs: The objects to unlink.
        """
        for obj in as_iterable(objs):
            bpy.data.objects.remove(obj, do_unlink=True)

    @staticmethod
    @log.catch
    def get_custom_property_value(objs: Union[Iterable['Object'], 'Object'], name: str) -> Union[any, list[any]]:
        """
        Get the value of a custom property on the object.
        
        Parameters:
        - objs: The objects to get the custom property from.
        - name: The name of the custom property to get.
        
        Returns:
        - The value of the custom property.
        """
        objs = as_iterable(objs)
        if len(objs) == 1:
            return objs[0].get(name)
        
        props = []
        for obj in objs:
            if name in obj:
                props.append(obj[name])
        
        return props

    @staticmethod
    @log.catch
    def set_custom_property(objs: Union[Iterable['Object'], 'Object'], name: str, value):
        """
        Set a custom property on the object.
        
        Parameters:
        - objs: The objects to set the custom property on.
        - name: The name of the custom property to set.
        - value: The value to set the custom property to.
        """
        for obj in as_iterable(objs):
            if name in obj:
                log.info(f'ops.data.set_custom_property(objs={objs}, name={name}, value={value}) :: Overwriting custom property "{name}" on object "{obj.name}" with value "{value}"')
            obj[name] = value

    @staticmethod
    @log.catch
    def with_custom_property(objs: Union[Iterable['Object'], 'Object'], name: str) -> list['Object']:
        """
        Get all objects that have the given custom property.
        
        Parameters:
        - objs: The objects to check for the custom property.
        - name: The name of the custom property to check for.
        
        Returns:
        - A set of objects that have the custom property.
        """
        objs = as_iterable(objs)
        _objs = []
        for obj in objs:
            if name in obj:
                _objs.append(obj)

        return _objs

    @staticmethod
    @log.catch
    def remove_custom_property(objs: Union[Iterable['Object'], 'Object'], name: str):
        """
        Remove a custom property from the object.
        
        Parameters:
        - objs: The objects to remove the custom property from.
        - name: The name of the custom property to remove.
        """
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
        """
        Copy images to a destination directory.
        
        Parameters:
        - images: The images to copy.
        - dest_dir: The destination directory to copy the images to.
        """
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
        """
        Unpack images.
        
        Parameters:
        - images: The images to unpack.
        """
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

    @staticmethod
    @log.catch
    def unpack_connected_images(objs: Union[Iterable['Object'], 'Object']):
        """
        Unpack images connected to shader nodes.
        
        Parameters:
        - objs: The objects to unpack connected images for.
        """
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
        """
        Reset scaled images to their original size.
        
        Parameters:
        - objs: The objects to reset scaled images for.
        """
        bpy.ops.object.mode_set(mode='OBJECT')
        nodes: set['ShaderNodeTexImage'] = ops.shader.node.of_type(
            objs, bpy.types.ShaderNodeTexImage)

        for node in nodes:
            img = node.image
            if not img:
                continue

            scaled = Size.from_name(img.filepath_raw)
            if scaled:
                filepath = img.filepath_raw.replace(scaled.filename_suffix(), ".")
                ops.shader.node.load_image(node, filepath)

    # TODO: sort out texture referencing and naming system
    @staticmethod
    @log.catch
    def scale_images_to_maxsize(nodes: Union[Iterable['ShaderNodeTexImage'], 'ShaderNodeTexImage'], scale: 'Size'):
        """
        Scale images to the given size.
        
        Parameters:
        - nodes: The image nodes to scale.
        - scale: The size to scale the images to.
        """
        if bpy.data.use_autopack:
            Data.unpack_images()

        bpy.ops.object.mode_set(mode='OBJECT')
        _nodes = as_iterable(set(nodes))
        for node in _nodes:
            img = node.image
            if not img:
                continue

            # try load image
            scaled = Size.from_name(img.filepath_raw)
            filepath = img.filepath_raw
            if scaled:
                filepath = img.filepath_raw.replace(scaled.filename_suffix(), ".")
                img = bpy.data.images.load(filepath, check_existing=True)
            
            log.info(f'ops.data.scale_images_to_maxsize() :: Rescaling image "{img.filepath_raw}" to {scale.name}')

            filepath = os.path.splitext(filepath)[0]

            img_path = filepath + scale.filename_suffix() + \
                f"{img.file_format}".lower()

            # load image fail -> rescale existing texture
            f = scale.value / max(img.size[0], img.size[1])

            img.scale(int(img.size[0] * f), int(img.size[1] * f))

            img.filepath_raw = img_path
            # TODO: add name length checks
            img.name = os.path.basename(bpy.path.abspath(img_path))

            img.save()
            ops.shader.node.load_image(node, img.filepath_raw)
    
    
    # @TODO : implement texture archiving
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


data = Data()
