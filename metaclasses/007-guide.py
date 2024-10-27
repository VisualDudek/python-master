# SUPER Deep dive into Enum class
# open enum module and using VSCode Ctrl+Shift+O find following signatnatures
# TAKEAWAY how dunder __prepare__ is used in EnumType metaclass

from enum import Enum


# class Enum(metaclass=EnumType): ...
# class EnumType(type):


# class EnumType(type):
#     """
#     Metaclass for Enum
#     """


#     @classmethod
#     def __prepare__(metacls, cls, bases, **kwds):
#         # check that previous enum members do not exist
#         metacls._check_for_existing_members_(cls, bases)
#         # create the namespace dict
#         enum_dict = _EnumDict()
#         enum_dict._cls_name = cls
#         # inherit previous flags and _generate_next_value_ function
#         member_type, first_enum = metacls._get_mixins_(cls, bases)
#         if first_enum is not None:
#             enum_dict['_generate_next_value_'] = getattr(
#                     first_enum, '_generate_next_value_', None,
#                     )
#         return enum_dict
#     def __new__(metacls, cls, bases, classdict, *, boundary=None, _simple=False, **kwds):
#         # an Enum class is final once enumeration items have been defined; it
#         # cannot be mixed with other types (int, float, etc.) if it has an
#         # inherited __new__ unless a new __new__ is defined (or the resulting
#         # class will fail).
#         #
#         if _simple:
#             return super().__new__(metacls, cls, bases, classdict, **kwds)
#         #
#         # remove any keys listed in _ignore_
#         classdict.setdefault('_ignore_', []).append('_ignore_')
#         ignore = classdict['_ignore_']
#         for key in ignore:
#             classdict.pop(key, None)
#         #
#         # grab member names
#         member_names = classdict._member_names
#         #
#         # check for illegal enum names (any others?)
#         invalid_names = set(member_names) & {'mro', ''}  <----------
#         if invalid_names:                                           \
#             raise ValueError('invalid enum member name(s) %s'  % (  |
#                     ','.join(repr(n) for n in invalid_names)        |
#                     ))                                              |
#         #                                                           |
#         # adjust the sunders                                        |
# ...                                                                 |
#                                                                     |
#                                                                     |
# vvvvvvvvvvvvvvvvvv test against illegal enum names  ----------------/
class Invalid(Enum):
    mro = 1
