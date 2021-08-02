from random import randrange
from typing import TypeVar, Sequence

T = TypeVar('T')


def randomItem(items: Sequence[T]) -> T:
    index = randrange(len(items))
    return items[index]
