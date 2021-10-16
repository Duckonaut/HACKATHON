import pygame
White = (255, 255, 255)
Green = (50, 250, 30)

LINE_WIDTH = 1
WIDTH = HEIGHT = 642

FPS = 10

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Snake")


class Field:
    def __init__(self, win):
        self._win = win
        self._n = 40
        self._grid = []
        for n in range(16):
            self._grid.append([])
            for _ in range(16):
                self._grid[n].append([])

    def update(self, snake):
        self._snake.update()
        self._win.fill((0, 0, 0))
        for x in range(17):
            pygame.draw.rect(self._win, White, (0, self._n * x, WIDTH, LINE_WIDTH))
            pygame.draw.rect(self._win, White, (self._n * x, 0, LINE_WIDTH, HEIGHT))

        pygame.draw.rect(self._win, Green, (LINE_WIDTH + self._snake.X() * self._n, LINE_WIDTH + self._snake.Y() * self._n, self._n - LINE_WIDTH, self._n - LINE_WIDTH))


class Snake:
    def __init__(self):
        self._x = 7
        self._y = 7
        self._direction = 1
        self._dead = False
        self.segments = 1

    def Direction(self, dir):
        self._direction = dir

    def Dead(self):
        return self._dead

    def X(self):
        return self._x

    def Y(self):
        return self._y

    def update(self):
        if (self._direction == 0 and self._y > 0):
            self._y -= 1
        elif (self._direction == 1 and self._x < 17):
            self._x += 1
        elif (self._direction == 2 and self._y < 17):
            self._y += 1
        elif (self._direction == 3 and self._x > 0):
            self._x -= 1


def main():
    run = True
    clock = pygame.time.Clock()
    field = Field(WIN)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_a):
                    field.Snake().Direction(3)
                elif (event.key == pygame.K_w):
                    field.Snake().Direction(0)
                elif (event.key == pygame.K_s):
                    field.Snake().Direction(2)
                elif (event.key == pygame.K_d):
                    field.Snake().Direction(1)

        field.update()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
