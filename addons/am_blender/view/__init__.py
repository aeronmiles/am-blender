from . import (pie, operators)


def register():
    operators.register()
    pie.register()


def unregister():
    operators.unregister()
    pie.unregister()
