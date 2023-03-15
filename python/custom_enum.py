def is_callable(fn):
    return callable(fn) or isinstance(fn, classmethod) or isinstance(fn, staticmethod)

class EnumMeta(type):
    def __new__(metacls, cls, bases, classdict, **kwds):
        # print(classdict)
        enum_class = super().__new__(metacls, cls, bases, classdict, **kwds)
        # enum_class._member_map_ = {k: v for k, v in cls._member_map_ if not is_callable(v) and not k.startswith("__")}
        enum_class._member_map_ = classdict.items()
        # print(enum_class._member_map_)
        # enum_class.__iter__ = lambda cls: cls._member_map_.items()
        return enum_class
    def __iter__(cls):
        return ((k, v) for k, v in cls._member_map_ if not is_callable(v) and not k.startswith("__"))

class E(metaclass=EnumMeta):
# class E():
    # def __new__(cls, *args, **kwargs):
    #     print("args: %s, kwargs: %s" % (args, kwargs))
    #     # args: (), kwargs: {}
    #     return super(E, cls).__new__(cls, *args, **kwargs)

    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"

    ### a = "A"
    ### b = "B"

    ### def num(self):
    ###     pass

    ### @classmethod
    ### def num2(cls):
    ###     pass

    ### @staticmethod
    ### def num2(cls):
    ###     pass

    # @classmethod
    # def __iter__(cls):
    #     while vars(self)
    #     not callable(getattr(example, attr)) and not attr.startswith("__")


# print(E())
# print(dir(E))
# print(E)

print("Accessing Attributes")
# print(E.a)
# print(E.b)
print(E.RED)
print(E.BLUE)
print()

print("Iterating Attributes")
for (k, v) in E:
    print("Key: %s, Value: %s" % (k, v))


from enum import Enum
class Color(Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"

class FastColor:
    RED = Color.RED
    BLUE = Color.BLUE
    GREEN = Color.GREEN

def f():
    for _ in range(1000):
        Color.RED
        Color.BLUE
        Color.GREEN

import timeit
print(timeit.timeit('f()', number=10000, globals=globals()))

Color = FastColor
print(timeit.timeit('f()', number=10000, globals=globals()))

Color = E
print(timeit.timeit('f()', number=10000, globals=globals()))
