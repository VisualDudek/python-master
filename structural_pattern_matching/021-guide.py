# you can impose additional restriction on the sequence type using class pattern


from typing import Union, List, Tuple


def flip(pair: Union[List[int], Tuple[int, ...]]) -> Union[list[int], tuple[int, ...]]:
    match pair:
        case list([x, y]):
            return [y, x]
        case tuple([x, y]):
            return y, x
        case _:
            raise TypeError("Unsupported type")
