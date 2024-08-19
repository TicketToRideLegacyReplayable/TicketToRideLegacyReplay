from typing import Callable
from . import cards


EventEffect = Callable[['Game'], None]


class Game():
    def __init__(self) -> None:
        from . import secret_data
        from . import starting_data
        self._story = secret_data.story.Story()
        self.event_list = cards.CardStack[EventEffect](starting_data.EVENT_CARDS_START, False)
        self.event_list.shuffle()

    def event(self) -> None:
        card = self.event_list()
        card(self)


__all__ = ['Game', "EventEffect"]
