class Color(str):
    pass


RED = Color('Red')
GREEN = Color('Green')
BLUE = Color('Blue')
YELLOW = Color('Yellow')
BLACK = Color('Black')
WHITE = Color('White')
GRAY = Color('Gray')

TRAIN_COLORS: set[Color] = {
    RED,
    GREEN,
    BLUE,
    YELLOW,
    BLACK
}

RAIL_COLORS: set[Color] = TRAIN_COLORS | {
    WHITE
}


class Rail():
    def __init__(self, city_1: str, city_2: str, lenght: int, color: Color | None = None) -> None:
        """Make a rail between 2 cities

        Args:
            city_1 (str): Start of the rail
            city_2 (str): End of the rail
            lenght (int): How many tiles there are
            color (Color | None, optional): What color is the rail, None is considered not yet built. Defaults to None.
        """
        if lenght < 1:
            raise ValueError("Length must be positive.")
        if len(city_1) < 1:
            raise ValueError("Starting city must be given.")
        if len(city_2) < 1:
            raise ValueError("Ending city must be given.")
        if city_1 == city_2:
            raise ValueError("Start and end must be different.")
        self._c1 = city_1
        self._c2 = city_2
        self._len = lenght
        self._color = color

    @property
    def len(self) -> int:
        return self._len

    @len.setter
    def len(self, len: int) -> None:
        raise PermissionError("You cannot change this")

    def __len__(self) -> int:
        return self.len

    @property
    def color(self) -> Color | None:
        return self._color

    @color.setter
    def color(self, color: Color) -> None:
        if self._color is not None:
            raise PermissionError("You cannot change this")
        if color not in RAIL_COLORS:
            raise ValueError("This is not a valid new color")
        self._color = color


__all__ = [
    'Color',
    'RED',
    'GREEN',
    'BLUE',
    'YELLOW',
    'BLACK',
    'WHITE',
    'TRAIN_COLORS',
    'RAIL_COLORS',
    'Rail'
]
