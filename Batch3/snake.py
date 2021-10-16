import pygame
from random import randint

White = (255, 255, 255)
Green = (50, 250, 30)
GRAY = (30, 30, 30)
GRAYER = (50, 50, 50)
BLACK = (0, 0, 0)

LINE_WIDTH = 1
WIDTH = HEIGHT = 640

FPS = 6

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Snake")


class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.col = None
        self.lifespan = 0


class Field:
    def __init__(self, win):
        self._win = win
        self.SQUARE_SIZE = 40
        self._snake = Snake()
        self._grid = []
        self.apple = ()
        self.points = 0

        for n in range(16):
            self._grid.append([])
            for m in range(16):
                self._grid[n].append(Square(n, m))

        self.spawnApple()

    def draw_text(self, x, y, string, col, size):
        font = pygame.font.SysFont("Impact", size)
        text = font.render(string, True, col)
        textbox = text.get_rect()
        textbox.center = (x, y)
        self._win.blit(text, textbox)

    def spawnApple(self):
        x = randint(0, 15)
        y = randint(0, 15)
        while self.getSquare(x, y).lifespan != 0:
            x = randint(0, 15)
            y = randint(0, 15)

        square = self.getSquare(x, y)
        square.lifespan = -1
        square.col = White

        self.apple = (x, y)

    def getSquare(self, x, y):
        return self._grid[x][y]

    def Snake(self):
        return self._snake

    def endGame(self):
        self._win.fill(White)
        x, y = WIDTH//2, HEIGHT//2
        self.draw_text(x+2, y-2, "Game Over (Space to restart)", BLACK, 40)
        self.draw_text(x+2, y-2, "Game Over (Space to restart)", BLACK, 40)
        self.draw_text(x-2, y+2, "Game Over (Space to restart)", BLACK, 40)
        self.draw_text(x-2, y+2, "Game Over (Space to restart)", BLACK, 40)
        self.draw_text(x, y, "Game Over (Space to restart)", Green, 40)

    def updateSnake(self):
        global FPS
        self.Snake().update()
        if self.getSquare(self.Snake().Y(), self.Snake().X()).lifespan > 0:
            self.Snake()._dead = True

        if self.Snake()._dead:
            self.endGame()
        else:
            square = self.getSquare(self.Snake().Y(), self.Snake().X())
            square.col = Green
            square.lifespan = self.Snake().segments
            if (self.Snake().Y(), self.Snake().X()) == self.apple:
                self.points += 1
                if self.points % 3 == 0:
                    FPS += 1
                self.Snake().segments += 1
                self.spawnApple()

    def update(self):
        if not self.Snake()._dead:
            self._win.fill(GRAYER)
            for row in range(0, 16):
                for col in range(row % 2, 16, 2):
                    pygame.draw.rect(self._win, GRAY, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))

            self.updateSnake()

            for row in range(0, 16):
                for col in range(0, 16):
                    square = self.getSquare(row, col)
                    if square.lifespan != 0:
                        pygame.draw.rect(self._win, square.col, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))
                        square.lifespan -= 1

            x, y = WIDTH//2, HEIGHT//2 - 100
            self.draw_text(x+2, y-2, f"{self.points}", BLACK, 40)
            self.draw_text(x+2, y-2, f"{self.points}", BLACK, 40)
            self.draw_text(x-2, y+2, f"{self.points}", BLACK, 40)
            self.draw_text(x-2, y+2, f"{self.points}", BLACK, 40)
            self.draw_text(x, y, f"{self.points}", Green, 40)


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
        elif (self._direction == 1 and self._x < 15):
            self._x += 1
        elif (self._direction == 2 and self._y < 15):
            self._y += 1
        elif (self._direction == 3 and self._x > 0):
            self._x -= 1
        else:
            self._dead = True


def main():
    global FPS
    run = True
    clock = pygame.time.Clock()
    field = Field(WIN)
    while run:
        clock.tick(FPS)
        turned = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and not turned:
                if (event.key == pygame.K_a and field.Snake()._direction != 1):
                    field.Snake().Direction(3)
                    turned = True
                elif (event.key == pygame.K_w and field.Snake()._direction != 2):
                    field.Snake().Direction(0)
                    turned = True
                elif (event.key == pygame.K_s and field.Snake()._direction != 0):
                    field.Snake().Direction(2)
                    turned = True
                elif (event.key == pygame.K_d and field.Snake()._direction != 3):
                    field.Snake().Direction(1)
                    turned = True
                elif (event.key == pygame.K_SPACE and field.Snake()._dead):
                    field = Field(WIN)
                    FPS = 6

        field.update()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
