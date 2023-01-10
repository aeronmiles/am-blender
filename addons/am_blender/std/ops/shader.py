import re
from ...std import *


class Node:
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
        except Exception as e:
            log.error(
                f'ops.shader.node.load_image(node={node}, img_filepath={img_filepath}) :: Failed to load image into node :: Exception: {e}')
            return False

    @staticmethod
    @log.catch
    def of_type(objs: Union[Iterable['Object'], 'Object', Iterable['Material'], 'Material'], _type: type) -> set:
        if not objs:
            return set()

        _objs = as_iterable(objs)
        mats: Iterable
        if isinstance(_objs[0], bpy.types.Material):
            mats = _objs
        else:
            mats = Shader.materials(_objs)

        nodes = []
        for mat in mats:
            # allow for calling when context does not all data to be accessed
            try:
                mat.use_nodes = True
            except Exception as e:
                pass
                # log.error(
                #     f'ops.shader.node.of_type(objs={objs}, _type={_type}) :: Failed to set material.use_nodes = True "{mat.name}" to use nodes Exception: {e}')
            nodes.extend((n for n in mat.node_tree.nodes if isinstance(
                n, _type)))

        return set(nodes)

    @staticmethod
    @log.catch
    def upstream_nodes(nodes: Union[Iterable['Node'], 'Node'], inclusive: bool = False) -> set['Node']:
        us_nodes: List['Node'] = []
        if inclusive:
            us_nodes.extend(as_iterable(nodes))

        for node in as_iterable(nodes):
            for i in node.inputs:
                for l in i.links:
                    us_nodes.extend(Node.upstream_nodes(l.from_node, True))

        return set(us_nodes)

    @staticmethod
    @log.catch
    def downstream_nodes(nodes: Union[Iterable['Node'], 'Node'], inclusive: bool = False) -> set['Node']:
        _nodes = as_iterable(nodes)
        ds_nodes: List['Node'] = []
        if inclusive:
            ds_nodes.extend(as_iterable(nodes))

        for node in _nodes:
            for o in node.outputs:
                for l in o.links:
                    ds_nodes.extend(Node.downstream_nodes(l.to_node, True))

        return set(ds_nodes)

    @staticmethod
    @log.catch
    def connected_to_input(nodes: Union[Iterable['Node'], 'Node'], inputs: Union[Iterable[str], str], node_type: Union[type, None] = None) -> set['Node']:
        _nodes = as_iterable(nodes)
        _inputs = as_iterable(inputs)
        connected_nodes: List['Node'] = []
        for node in _nodes:
            ds_nodes = Node.downstream_nodes(node, True)
            for n in ds_nodes:
                for o in n.outputs:
                    for l in o.links:
                        if l.to_socket.name in _inputs:
                            if not node_type or isinstance(l.to_node, node_type):
                                # log.info(f'Found socket: {l.to_socket.name}')
                                connected_nodes.append(node)

        return set(connected_nodes)

    @staticmethod
    @log.catch
    def disconnect_inputs(objs: Union[Iterable['Object'], 'Object'], input: str, node_type: type):
        mats = Shader.materials(objs)
        for mat in mats:
            nodes = Node.of_type(mat, node_type)
            for node in nodes:
                if node.inputs.find(input) > -1:
                    for l in node.inputs[input].links:
                        mat.node_tree.links.remove(l)


class Shader:
    node = Node()

    @staticmethod
    @log.catch
    def material_slots(objs: Union[Iterable['Object'], 'Object']) -> set['MaterialSlot']:
        slots = []
        _objs = as_iterable(objs)
        for obj in _objs:
            slots.extend(obj.material_slots)

        return set(slots)

    @staticmethod
    @log.catch
    def materials(objs: Union[Iterable['Object'], 'Object']) -> set['Material']:
        materials = []
        _objs = as_iterable(objs)
        for obj in _objs:
            for ms in obj.material_slots:
                materials.append(ms.material)

        return set(materials)

    @staticmethod
    @log.catch
    def blend_mode(objs: Union[Iterable['Object'], 'Object'], mode: BlendMode):
        mats = Shader.materials(objs)
        for mat in mats:
            mat.blend_method = mode.value

    @staticmethod
    @log.catch
    def backface_culling(objs: Union[Iterable['Object'], 'Object'], culling: bool):
        mats = Shader.materials(objs)
        for mat in mats:
            mat.use_backface_culling = culling

    @staticmethod
    @log.catch
    def replace_materials(objs: Union[Iterable['Object'], 'Object'], mats: Iterable[tuple['Material', 'Material']]):
        _objs = as_iterable(objs)
        for mat_old, mat_new in mats:
            for obj in _objs:
                for ms in obj.material_slots:
                    if ms.material == mat_old:
                        ms.material = mat_new
                        if mat_old.users == 0:
                            mat_old.use_fake_user = True

    @staticmethod
    @log.catch
    def duplicate_materials(objs: Union[Iterable['Object'], 'Object'], suffix: str):
        old_mats = Shader.materials(objs)
        new_mats = []
        for mat in old_mats:
            new_mat = mat.copy()
            # TODO: name length checks
            new_mat.name = mat.name + suffix
            new_mats.append(new_mat)

        Shader.replace_materials(objs, zip(old_mats, new_mats))

    @staticmethod
    @log.catch
    def set_material_lod(objs: Union[Iterable['Object'], 'Object'], lod: int):
        mats = Shader.materials(objs)
        mats_to_replace = []
        new_mats = []
        for mat in mats:
            if mat.amb_mat.lod == lod:
                continue

            if '_LOD' not in mat.name:
                mat.amb_mat.lod = 0
                mat.name += f'_LOD0'

            mats_to_replace.append(mat)

            basename = mat.name.replace(f'_LOD{mat.amb_mat.lod}', '')
            new_mat = bpy.data.materials.get(basename + f'_LOD{lod}')
            if not new_mat:
                new_mat = mat.copy()
                # TODO: name length checks
                new_mat.name = basename + f'_LOD{lod}'
                new_mat.amb_mat.lod = lod

            new_mats.append(new_mat)

        Shader.replace_materials(objs, zip(mats_to_replace, new_mats))

    @staticmethod
    @log.catch
    def get_material_lod(objs: Union[Iterable['Object'], 'Object']) -> int:
        mats = Shader.materials(objs)
        for mat in mats:
            if '_LOD' in mat.name:
                return mat.amb_mat.lod

        return 0

    @staticmethod
    @log.catch
    def rename_material_textures(objs: Union[Iterable['Object'], 'Object']):
        Shader._rename_material_textures(
            objs, 'Base Color', 'BaseColor', bpy.types.ShaderNodeBsdfPrincipled)
        Shader._rename_material_textures(
            objs, 'Normal', 'Normal', bpy.types.ShaderNodeBsdfPrincipled)
        Shader._rename_material_textures(
            objs, 'Metallic', 'RoughMetalAO', bpy.types.ShaderNodeBsdfPrincipled)
        Shader._rename_material_textures(
            objs, 'Occlusion', 'RoughMetalAO', bpy.types.ShaderNodeGroup)

    @staticmethod
    @log.catch
    def _rename_material_textures(objs: Union[Iterable['Object'], 'Object'], input: str, input_name: str, node_type: type):
        strip_strs = ['base', 'color', 'normal',
                      'roughness', 'rough', 'metallic', 'occlusion']
        res = [re.compile(re.escape(s), re.IGNORECASE) for s in strip_strs]

        mats = Shader.materials(objs)
        for mat in mats:
            nodes = Node.of_type(mat, bpy.types.ShaderNodeTexImage)
            nodes = [n for n in nodes if n.image]
            connected_nodes = Node.connected_to_input(nodes, input, node_type)
            for node in connected_nodes:
                fp_old = bpy.path.abspath(node.image.filepath_raw)
                if input_name in fp_old and mat.name.replace(" ", "") in fp_old:
                    continue

                img_name = node.image.name
                for r in res:
                    img_name = r.sub('', img_name)

                ext = os.path.splitext(os.path.basename(fp_old))[1]
                fp_new = os.path.join(os.path.dirname(
                    fp_old), f'{mat.name}_{img_name}_{input_name}{ext}'.replace(" ", ""))

                if not os.path.exists(fp_new):
                    os.rename(fp_old, fp_new)

                node.image.filepath_raw = bpy.path.relpath(fp_new)
                node.image.name = os.path.basename(fp_new)
                Node.load_image(node, node.image.filepath_raw)


shader = Shader()
