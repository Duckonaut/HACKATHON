import pygame
from random import choice

Yellow = (252, 207, 83)
Yellower = (122, 98, 33)

WIDTH = HEIGHT = 600

FPS = 60

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("TicTacToe")


class Tile:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.choice = None


class Field:
    def __init__(self, win) -> None:
        self._win = win
        self.SQUARE_SIZE = 200
        self.grid = []
        self.turn = 0
        self.available = []
        for row in range(0, 3):
            self.grid.append([])
            for col in range(0, 3):
                self.available.append((row, col))
                self.grid[row].append(Tile(col, row))

    def draw(self):
        self._win.fill(Yellow)
        for row in range(0, 3):
            for col in range(row % 2, 3, 2):
                pygame.draw.rect(self._win, Yellower, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))

        for row in range(0, 3):
            for col in range(0, 3):
                tile = self.grid[row][col]
                if tile.choice is not None:
                    if tile.choice == 0:
                        pygame.draw.rect(self._win, (0, 0, 0), (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))
                    else:
                        pygame.draw.rect(self._win, (255, 255, 255), (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))

    def update(self):
        self.draw()

    def detectTile(self, x, y):
        row = y // 200
        col = x // 200
        return self.grid[row][col]

    def move(self, x, y):
        tile = self.detectTile(x, y)
        tile.choice = 0
        bot_move = choice(self.available) #tu
        self.detectTile(bot_row, bot_col).choice = 1
        self.update()


def main():
    global FPS, WIN
    run = True
    clock = pygame.time.Clock()
    field = Field(WIN)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                field.move(x, y)
        field.update()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()