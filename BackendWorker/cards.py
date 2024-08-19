import copy
import random
from typing import Callable, Generic, SupportsIndex, TypeVar


T = TypeVar('T', Callable[..., None], None)


class Card(Generic[T]):
    def __call__(self, *arg: object) -> None:  # type: ignore
        if self.effect is None:
            return
        self.effect(*arg)

    def __init__(self, content: str, effect: T = None) -> None:
        self.content = content
        self.effect = effect
        if effect is None:
            self.__call__: Callable[[], None] = self.__call__  # type: ignore
        else:
            self.__call__: T = self.__call__


class CardStack(Generic[T]):
    def __init__(self, card_list: list[Card[T]], shuffle_on_empty: bool = True) -> None:
        self.stack: list[Card[T]] = copy.deepcopy(card_list)
        self.trash: list[Card[T]] = []
        self.shuffle_on_empty = shuffle_on_empty

    def shuffle(self, with_trash: bool = False) -> None:
        if with_trash:
            self.stack.extend(self.trash)
            self.trash = []
        random.shuffle(self.stack)

    def __call__(self) -> Card[T]:
        if self.shuffle_on_empty and len(self.stack) < 1:
            self.shuffle(True)
        card = self.stack.pop(0)
        self.trash.append(card)
        return card

    def look_trash(self, pos: SupportsIndex = -1) -> Card[T]:
        return self.trash[pos]


__all__ = ['Card', 'CardStack']
