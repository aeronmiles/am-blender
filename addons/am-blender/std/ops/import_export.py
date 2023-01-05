from ...std import *


class Import:
    pass


class Export:
    @staticmethod
    @log.catch
    @check.saved(f"Export -> _batch()")
    @recall.selection
    def _batch(format: FileFormat, context: 'Context'):
        # export to blend file location
        basedir = os.path.dirname(bpy.data.filepath)
        view_layer = context.view_layer
        for obj in as_iterable(context.selected_objects):
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)

            # some exporters only use the active object
            view_layer.objects.active = obj

            name = bpy.path.clean_name(obj.name)

            fn = os.path.join(basedir, format.value.lower(), name)
            ensure_dir(fn)
            match format:
                case FileFormat.GLB | FileFormat.GLTF_SEPARATE | FileFormat.GLTF_EMBEDDED:
                    bpy.ops.export_scene.gltf(filepath=fn +
                                              f".{format.value.lower()}", export_format=format.value, use_selection=True)
                case FileFormat.USDZ:
                    from io_scene_usdz import export_usdz
                    export_usdz.export_usdz(context, filepath=fn +
                                            f".{format.value.lower()}", exportMaterials=True,
                                            bakeTextures=False, bakeTextureSize=1024, bakeAO=False,
                                            bakeAOSamples=64, exportAnimations=False,
                                            globalScale=1.0, useConverter=False,
                                            )

    @staticmethod
    def batch_gltf_embedded(context: 'Context'):
        Export._batch(FileFormat.GLTF_EMBEDDED, context)

    @staticmethod
    def batch_gltf_separate(context: 'Context'):
        Export._batch(FileFormat.GLTF_SEPARATE, context)

    @staticmethod
    def batch_glb(context: 'Context'):
        Export._batch(FileFormat.GLB, context)

    @staticmethod
    def batch_usdz(context: 'Context'):
        Export._batch(FileFormat.USDZ, context)


class Io:
    imp = Import()
    exp = Export()


io = Io()
