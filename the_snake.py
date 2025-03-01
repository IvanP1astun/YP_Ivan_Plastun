from random import choice, randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (0, 255, 255)

# Цвет яблока
APPLE_COLOR = (120, 252, 0)

# Цвет змейки
SNAKE_COLOR = (255, 215, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()
"""Базовый класс для всех объектов игры."""


# Тут опишите все классы игры.
class GameObject:
    """Базовый класс для всех объектов игры."""

    def __init__(self):
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = BOARD_BACKGROUND_COLOR

    def draw(self):
        """Метод для отрисовки объекта (может быть переопределен)."""


class Apple(GameObject):
    """Класс, представляющий яблоко."""

    def __init__(self, snake_positions=None):  # Исправил
        """Инициализация яблока."""
        super().__init__()
        self.body_color = APPLE_COLOR
        self.randomize_position(snake_positions or [])

    def randomize_position(self, snake_positions):
        """Случайно устанавливает позицию яблока на поле."""
        position = (randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                    randint(0, GRID_HEIGHT - 1) * GRID_SIZE)
        if position in snake_positions:
            self.randomize_position(snake_positions)
        else:
            self.position = position

    def draw(self):
        """Отрисовывает яблоко на экране."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс, представляющий змейку."""

    def __init__(self):
        """Инициализация змеи."""
        super().__init__()
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = SNAKE_COLOR
        self.last = None

    def get_head_position(self):
        """Возвращает позицию головы змеи."""
        return self.positions[0]

    def update_direction(self):
        """Обновляет направление движения змеи, если оно изменилось."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Перемещает змею в текущем направлении."""
        head_x, head_y = self.get_head_position()
        # Нужно провести распаковку позиций головы/направления
        # по x и y - не уверен, что правильно.
        dir_x, dir_y = self.direction
        new_position = (
            (head_x + dir_x * GRID_SIZE) % SCREEN_WIDTH,
            (head_y + dir_y * GRID_SIZE) % SCREEN_HEIGHT)

        # Обновление позиции головы.
        (self.positions).insert(0, new_position)
        if len(self.positions) > self.length:
            self.last = (self.positions).pop()

    def draw(self):
        """Отрисовывает змею на экране."""
        for position in self.positions[:-1]:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(self.get_head_position(),
                                (GRID_SIZE, GRID_SIZE))

        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def reset(self):
        """Сбрасывает состояние змеи по умолчанию."""
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = choice([RIGHT, UP, DOWN, LEFT])


def handle_keys(game_object):
    """обрабатывает нажатия клавиш, чтобы изменить направление движения
    змейки
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT
                # Непонимаю как сделать словарь.


def main():
    """Функиция точка входа"""
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    main_snake = Snake()  # Создание змеи
    main_apple = Apple(main_snake.positions)  # Передаем позицию змеи

    while True:
        handle_keys(main_snake)
        main_snake.update_direction()
        main_snake.move()

        if main_snake.get_head_position() == main_apple.position:
            main_snake.length += 1
            main_apple.randomize_position(main_snake.positions)
            main_apple_position = main_apple.position
            while main_apple_position in main_snake.positions:
                main_apple_position = main_apple.position

        screen.fill(BOARD_BACKGROUND_COLOR)
        main_snake.draw()
        main_apple.draw()

        pygame.display.update()
        clock.tick(SPEED)


if __name__ == '__main__':
    main()
