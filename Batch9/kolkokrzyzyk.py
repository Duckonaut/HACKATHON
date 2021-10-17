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
        self.choice = -1


class Field:
    def __init__(self, win) -> None:
        self.imagex = pygame.image.load(r'x.jpg')
        self.imageo = pygame.image.load(r'o.jpg')
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
                if tile.choice != -1:
                    if tile.choice == 0:
                        self._win.blit(self.imagex, (0, 0))
                    else:
                        self._win.blit(self.imageo, (0, 0))

    def getAvailable(self):
        available = []
        for row in range(0, 3):
            for col in range(0, 3):
                if self.grid[row][col].choice == -1:
                    available.append((row, col))
        return available

    def update(self):
        self.draw()

    def detectTile(self, x, y):
        row = y // 200
        col = x // 200
        return self.grid[row][col]

    def endGame(self):
        pass

    def move(self, x, y):
        tile = self.detectTile(x, y)
        if tile.choice == -1:
            tile.choice = 0
            possibilities = self.getAvailable()
            if (len(possibilities) > 0):
                bot_move = choice(possibilities)
                self.grid[bot_move[0]][bot_move[1]].choice = 1
                self.update()
            else:
                self.endGame()


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