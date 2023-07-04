import enum

# Directions = enum.Enum('Directions', ['LEFT', 'RIGHT', 'UP', 'DOWN'])


class Directions(enum.Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


def move(direction: Directions) -> None:
    if not isinstance(direction, Directions):
        raise ValueError(f'Direction "{direction}" not allowed')

    print(f'Moving to {direction.name.lower()}')


move(Directions.LEFT)
move(Directions.RIGHT)
move(Directions.UP)
move(Directions.RIGHT)
