from typing import Any, Protocol
from . import s_1861
from . import e_1861


class StoryModule(Protocol):
    def run(self, *params: Any) -> None:
        ...


class Story():
    story: list[StoryModule] = [
        s_1861,
        e_1861,
        # TODO: complete
    ]

    def __init__(self) -> None:
        self.at = 0

    def __call__(self, *params: Any) -> None:
        self.story[self.at].run(params)
        self.at += 1


__all__ = [
    "Story"
]
