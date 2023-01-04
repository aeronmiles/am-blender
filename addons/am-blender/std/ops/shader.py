from ...std import *


class Shader:
    @staticmethod
    @log.catch
    def disconnect_inputs(objs: Union[Iterable['Object'], 'Object'], node_type: type, input: str):
        for obj in as_iterable(objs):
            for ms in obj.material_slots:
                mat = ms.material
                mat.use_nodes = True
                nodes = (
                    n for n in mat.node_tree.nodes if isinstance(n, node_type))

                for node in nodes:
                    if node.inputs.find(input) > -1:
                        for l in node.inputs[input].links:
                            mat.node_tree.links.remove(l)

    @staticmethod
    @log.catch
    def nodes_of_type(objs: Union[Iterable['Object'], 'Object'], _type: type) -> List:
        nodes = []
        for obj in as_iterable(objs):
            for ms in obj.material_slots:
                mat = ms.material
                mat.use_nodes = True
                nodes.extend((n for n in mat.node_tree.nodes if isinstance(
                    n, _type)))

        return nodes

    @staticmethod
    @log.catch
    def load_image(node: 'ShaderNodeTexImage', img_filepath: str) -> bool:
        try:
            # node settings
            interp = node.interpolation
            proj = node.projection
            extension = node.extension

            image = bpy.data.images.load(img_filepath, check_existing=True)
            image.colorspace_settings.name = node.image.colorspace_settings.name
            image.alpha_mode = node.image.alpha_mode

            node.image = image

            # restore previous node settings
            node.interpolation = interp
            node.projection = proj
            node.extension = extension
            return True
        except:
            return False


shader = Shader()
