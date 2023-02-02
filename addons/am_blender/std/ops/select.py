from ...std import *


class Select:
    @staticmethod
    @log.catch
    def all(objs: Union[Iterable['Object'], 'Object']):
        for obj in as_iterable(objs):
            obj.select_set(True)


select = Select()