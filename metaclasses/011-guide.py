# another example of simple usage of metaclass
# TAKEAWAY: metaclasses are inherited
# - if you are NOT doing something that's supposed to apply to a whole hierarchy of classes
# there is a good chance that it could just be done using class decorators

import time


class LoadTimeMeta(type):
    base_time = time.perf_counter()

    def __new__(mcs, name, bases, namespace):
        print(f"{mcs=}, {name=}, {bases=}, {namespace=}")
        # adding class attrib. to created class
        namespace["__class_load_time__"] = time.perf_counter() - LoadTimeMeta.base_time
        return super().__new__(mcs, name, bases, namespace)


class A(metaclass=LoadTimeMeta):
    pass


class B(A):
    pass


print(f"{A.__class_load_time__=}")
print(f"{B.__class_load_time__=}")
print(f"{type(B)}")
