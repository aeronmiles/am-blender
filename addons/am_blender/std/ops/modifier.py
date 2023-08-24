from ...std import *


class Modifier:
    @staticmethod
    @log.catch
    def show_render(objs: Union['Object', Iterable['Object']], enabled: bool):
        _objs = as_iterable(objs)
        for obj in _objs:
            if not obj.modifiers:
                continue

            for mod in obj.modifiers:
                mod.show_render = enabled
    
    @staticmethod
    @log.catch
    def show_viewport(objs: Union['Object', Iterable['Object']], enabled: bool):
        _objs = as_iterable(objs)
        for obj in _objs:
            if not obj.modifiers:
                continue

            for mod in obj.modifiers:
                mod.show_viewport = enabled

modifier = Modifier()