from ..colors import Color
from .. import colors


class Train():
    def __init__(self, color: Color) -> None:
        self._color = color

    @property
    def color(self) -> Color:
        return self._color

    @color.setter
    def color(self, color: Color) -> None:
        raise PermissionError("You cannot change this")


BLACK = Train(colors.BLACK)
BLUE = Train(colors.BLUE)
GREEN = Train(colors.GREEN)
YELLOW = Train(colors.YELLOW)
RED = Train(colors.RED)

CIRCUS_TRAINS: list[Train] = [
    BLACK,
    # TODO: complete
]

__all__ = [
    "CIRCUS_TRAINS"
]
