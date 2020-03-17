import pygame
from Snake import Snake
from Food import Food


def draw_snake(snake: Snake) -> None:
    for piece in snake.body:
        snake_rect = pygame.Rect((piece.x, piece.y), (snake_size, snake_size))
        pygame.draw.rect(surface, RED, snake_rect)


def draw_food(food: Food) -> None:
    food_rect = pygame.Rect((food.x, food.y), (snake_size, snake_size))
    pygame.draw.rect(surface, BLUE, food_rect)


def show_score(score: int) -> None:
    text = score_font.render("Score: " + str(score), True, WHITE)
    surface.blit(text, (0, 0))


def show_you_lost_screen() -> None:
    text = you_lost_screen_text.render("You lost press C to continue or Q to quit", True, WHITE)
    surface.blit(text, (WIDTH/9, HEIGHT/2.5))


def game_loop() -> None:

    game_over = False
    game_close = False

    while not game_close:

        while game_over and not game_close:
            surface.fill(BLACK)
            show_you_lost_screen()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = True
                    if event.key == pygame.K_c:
                        game_over = False

        snake = Snake(WIDTH, HEIGHT, snake_size)
        food = Food(WIDTH, HEIGHT, snake_size)
        score = 0
        while not game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = True
                if event.type == pygame.KEYDOWN:
                    snake.head_direction = event.key

            if snake.eat(food):
                food.generate(WIDTH, HEIGHT, snake_size)
                score += 1

            snake.move()

            if snake.died(WIDTH, HEIGHT):
                game_over = True

            surface.fill(BLACK)
            draw_snake(snake)
            draw_food(food)
            show_score(score)

            pygame.display.update()
            clock.tick(snake_speed)


if __name__ == '__main__':
    WIDTH, HEIGHT = 800, 600
    snake_size = 20
    snake_speed = 15

    BLACK = pygame.Color(0, 0, 0)
    BLUE = pygame.Color(20, 20, 150)
    RED = pygame.Color(150, 20, 20)
    WHITE = pygame.Color(255, 255, 255)

    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()
    score_font = pygame.font.SysFont('arial', 20)
    you_lost_screen_text = pygame.font.SysFont('comicsansms', 35)
    game_loop()
