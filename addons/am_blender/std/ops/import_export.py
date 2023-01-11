from ...std import *


class Import:
    pass


class Export:
    @staticmethod
    @log.catch
    @dec.check.saved(f"Export._save_name()")
    def _save_filename(objs: Union[Iterable['Object'], 'Object']) -> Union[str, None]:
        r"""Get context related save filename"""
        if not objs:
            log.warning(f'Export._save_name() :: No objects')
            return ""

        objs = list(as_iterable(objs))
        active = bpy.context.view_layer.objects.active
        if not active:
            log.warning(f'Export._save_name() :: No active object')
            return None

        return bpy.path.clean_name(active.name)

    @staticmethod
    @log.catch
    @dec.check.saved(f"Export.export()")
    def export(context: 'Context', format: FileFormat, dir: str = ""):
        r"""Export active objects"""
        objs = context.selected_objects
        if not objs:
            log.warning(f'Export.export() :: No objects to export')
            return

        # TODO: test this
        # some exporters only use the active object
        context.view_layer.objects.active = objs[0]

        # export to blend file location
        filename = Export._save_filename(objs)
        if not filename:
            log.warning(
                f'Export.export() :: Export._save_filename(objs) :: No filename')
            return

        fn = ""
        if dir:
            fn = os.path.join(dir, filename)
        else:
            fn = os.path.join(os.path.dirname(
                bpy.data.filepath), format.value.lower(), filename)

        ensure_dir(fn)

        match format:
            case FileFormat.GLB | FileFormat.GLTF_SEPARATE | FileFormat.GLTF_EMBEDDED:
                gltf = bpy.ops.export_scene.gltf
                gltf(filepath=fn +
                     f".{format.value.lower()}", export_format=format.value, use_selection=True)
            case FileFormat.USDZ:
                from io_scene_usdz import export_usdz
                usdz = export_usdz.export_usdz
                usdz(context, filepath=fn +
                     f".{format.value.lower()}", exportMaterials=True,
                     bakeTextures=False, bakeTextureSize=1024, bakeAO=False,
                     bakeAOSamples=64, exportAnimations=False,
                     globalScale=1.0, useConverter=False,
                     )

    @staticmethod
    @log.catch
    @dec.recall.selection
    def batch_export(context: 'Context', format: FileFormat, dir: str = ""):
        r"""Batch export selected objects to separate files"""
        objs = context.selected_objects
        bpy.ops.object.mode_set(mode='OBJECT')
        for obj in objs:
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            Export.export(context, format, dir)

    @staticmethod
    @log.catch
    @dec.recall.selection
    def to_google_model_viewer(context: 'Context', separate_models: bool = False):
        html = open(os.path.join(meta.datafile_dir,
                    'google_model_viewer.html'), 'r')

        def export():
            filename = Export._save_filename(context.selected_objects)
            if not filename:
                return

            dir = ensure_dir(os.path.join(os.path.dirname(
                bpy.data.filepath), 'google_model_viewer', filename, filename))

            log.info(f'Exporting to Google Model Viewer: {dir}')

            Export.export(context, FileFormat.GLB, dir)
            Export.export(context, FileFormat.USDZ, dir)

            index_html = os.path.join(os.path.dirname(
                bpy.data.filepath), dir, "index.html")
            with open(index_html, 'wt') as fout:
                fout.write(html.read().replace(
                    '{FILE.GLB}', f'{filename}.glb').replace('{FILE.USDZ}', f'{filename}.usdz'))

        if separate_models:
            bpy.ops.object.mode_set(mode='OBJECT')
            for obj in context.selected_objects:
                bpy.ops.object.select_all(action='DESELECT')
                obj.select_set(True)
                export()
        else:
            export()

        html.close()


class Io:
    imp = Import()
    exp = Export()


io = Io()
