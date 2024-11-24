# when you use an empty dict literal `{}` then pattern will match just about any mapping

from collections import ChainMap, Counter, OrderedDict, UserDict, defaultdict

mappings = (
    d := dict(pi=3.14, e=2.72),
    ChainMap(d),
    Counter(d),
    OrderedDict(d),
    UserDict(d),
    defaultdict(float, d),
)
for subject in mappings:
    match subject:
        case {}:
            print("Matched:", type(subject))
        case _:
            pass
