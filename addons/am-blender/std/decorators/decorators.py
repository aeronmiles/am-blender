from ...std import *


class Recall:
    def selection(self, func: Callable):
        def inner(*args, **kwargs):
            view_layer = bpy.context.view_layer
            obj_active = view_layer.objects.active
            sel = bpy.context.selected_objects

            func(*args, **kwargs)

            view_layer.objects.active = obj_active
            for obj in sel:
                obj.select_set(True)

        return inner


recall = Recall()


class Check:
    def saved(self, caller: str):
        def _saved(func: Callable):
            def inner(*args, **kwargs):
                if bpy.data.filepath:
                    func(*args, **kwargs)
                else:
                    log.warning(
                        f"Aborting :: {caller} :: Blend file is not saved.")

            return inner

        return _saved


check = Check()
