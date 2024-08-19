from . import game, cards


def shuffle_events(game: 'game.Game'):
    game.event_list.shuffle(True)
    game.event()


EVENT_CARDS_START: list[cards.Card[game.EventEffect]] = [
    cards.Card[game.EventEffect]('Mix the event cards', shuffle_events)
]

del shuffle_events

__all__ = ['EVENT_CARDS_START']
