from ...std import *


class Select:
    @staticmethod
    @log.catch
    def all(objs: Union[Iterable['Object'], 'Object'], select: bool = True):
        for obj in as_iterable(objs):
            obj.select_set(select)

select = Select()