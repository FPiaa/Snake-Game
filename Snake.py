import pygame
from Food import Food


class Snake(object):

    __move_map = {
        pygame.K_RIGHT: 'right',
        pygame.K_LEFT: 'left',
        pygame.K_UP: 'up',
        pygame.K_DOWN: 'down'
    }

    __opposite_directions = {
        'right': 'left',
        'left': 'right',
        'up': 'down',
        'down': 'up'
    }

    __movements = None

    def __init__(self, width, height, sub_division):

        # initiating the head
        self.body = [Body(width//2, height//2)]

        Snake.__movements = {
            'up': (0, -sub_division),
            'down': (0, sub_division),
            'left': (-sub_division, 0),
            'right': (sub_division, 0)
        }

        self.__head_direction = 'right'

    @property
    def head_direction(self) -> str:
        return self.__head_direction

    @head_direction.setter
    def head_direction(self, key_event: int) -> None:
        if key_event in Snake.__move_map.keys():
            new_direction = Snake.__move_map[key_event]

            # checks if the snake wont change to an invalid direction
            # e.g. you cant change your moving direction from left to right

            if new_direction != Snake.__opposite_directions[self.__head_direction]:
                self.__head_direction = Snake.__move_map[key_event]

    def move(self) -> None:
        for index in range(len(self.body)-1, 0, -1):
            self.body[index].x = self.body[index-1].x
            self.body[index].y = self.body[index - 1].y

        self.body[0].x += Snake.__movements[self.__head_direction][0]
        self.body[0].y += Snake.__movements[self.__head_direction][1]

    def _out_of_bounds(self, width, height) -> bool:
        head = self.body[0]
        if not (0 <= head.x <= width):
            return True
        if not (0 <= head.y <= height):
            return True
        return False

    def died(self, width, height) -> bool:
        head = self.body[0]

        # checking if the snake ate itself
        for body_piece in self.body[1:]:
            if body_piece.x == head.x and body_piece.y == head.y:
                return True
        is_out_of_bounds = self._out_of_bounds(width, height)
        return is_out_of_bounds

    def eat(self, food: Food) -> bool:
        head = self.body[0]

        if head.x == food.x and head.y == food.y:
            last = self.body[-1]
            self.body.append(Body(last.x, last.y))
            return True
        else:
            return False


class Body(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

