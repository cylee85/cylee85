import test_class as test__
import types

module_name = dict(locals())
del module_name['types']
for i in module_name:
    if not i.startswith("__"):
        print(type(locals()[i]))
        if isinstance(locals()[i], types.ModuleType):
            module_name = i
classes = []
for i in dir(globals()[module_name]):
    k = eval(f'{module_name}.{i}')
    data = type(k)
    if data == type(type):
        classes.append(k)
        print(data, eval(f'{module_name}.{i}'))


class E(*classes):
    def __init__(self):
        for c in classes:
            c.__init__(self)


k = E()
