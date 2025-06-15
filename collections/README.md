# Collections

temat `namedtuple` pochodzi faktycznie z `collections` ale lepiej ten kontener implementować w oparciu o klase `NamedTuple` from `typing`

DO NOT use `namedtuple` from `collections` use `NamedTuple` from `typing`

- subclassing NamedTuple and adding methods
- convert method into property BC it is computed value and you only read (never set) AND `distance_to_origin` do not take vars -> it is "computed value"
- overriding magic methods, e.g. add vectors `004`
- adding properties `005`
- `MyPoint = namedtuple("Point", ["x", "y"])` lewa strona to zminna w której trzymana jest classa, która inicjuje typ "Point" `006`
