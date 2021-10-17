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
        self.imagex = pygame.transform.scale(pygame.image.load(r'x.png'), (200, 200))
        self.imageo = pygame.transform.scale(pygame.image.load(r'o.png'), (200, 200))
        self._win = win
        self.end = False
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
                        self._win.blit(self.imagex, (col * 200, row * 200))
                    else:
                        self._win.blit(self.imageo, (col * 200, row * 200))

    def getAvailable(self):
        available = []
        for row in range(0, 3):
            for col in range(0, 3):
                if self.grid[row][col].choice == -1:
                    available.append((row, col))
        return available

    def draw_text(self, x, y, string, col, size):
        font = pygame.font.SysFont("Impact", size)
        text = font.render(string, True, col)
        textbox = text.get_rect()
        textbox.center = (x, y)
        self._win.blit(text, textbox)

    def update(self):
        self.draw()

    def detectTile(self, x, y):
        row = y // 200
        col = x // 200
        return self.grid[row][col]

    def endGame(self, result):
        self.update()
        self.end = True
        text = "REMIS"
        if result == 0:
            text = "WYGRYWA KRZYŻYK"
        if result == 1:
            text = "WYGRYWA KÓŁKO"

        x, y = 300, 300
        self.draw_text(x+2, y-2, text, (255, 255, 255), 40)
        self.draw_text(x+2, y-2, text, (255, 255, 255), 40)
        self.draw_text(x-2, y+2, text, (255, 255, 255), 40)
        self.draw_text(x-2, y+2, text, (255, 255, 255), 40)
        self.draw_text(x, y, text, (0, 0, 0), 40)

        x, y = 300, 350
        text = "Spacja, aby zagrać ponownie"
        self.draw_text(x+2, y-2, text, (255, 255, 255), 20)
        self.draw_text(x+2, y-2, text, (255, 255, 255), 20)
        self.draw_text(x-2, y+2, text, (255, 255, 255), 20)
        self.draw_text(x-2, y+2, text, (255, 255, 255), 20)
        self.draw_text(x, y, text, (0, 0, 0), 20)
        pygame.display.update()

    def checkWinHorizontal(self, choice):
        winHorizontal = True
        for row in range(0, 3):
            winHorizontal = True
            for col in range(0, 3):
                if self.grid[row][col].choice != choice:
                    winHorizontal = False
            if winHorizontal:
                return True
        return False

    def checkWinVertical(self, choice):
        winVertical = True
        for col in range(0, 3):
            winVertical = True
            for row in range(0, 3):
                if self.grid[row][col].choice != choice:
                    winVertical = False
            if winVertical:
                return True
        return False

    def checkWinDiagonal(self, choice):
        winDiagonal1 = True
        winDiagonal2 = True
        for i in range(0, 3):
            if self.grid[i][2-i].choice != choice:
                winDiagonal1 = False
        for i in range(0, 3):
            if self.grid[i][i].choice != choice:
                winDiagonal2 = False
        return winDiagonal1 or winDiagonal2

    def checkWin(self, choice):
        winH = self.checkWinHorizontal(choice)
        winV = self.checkWinVertical(choice)
        winD = self.checkWinDiagonal(choice)
        return winH or winV or winD

    def move(self, x, y):
        tile = self.detectTile(x, y)
        if tile.choice == -1:
            tile.choice = 0

            if self.checkWin(0):
                self.endGame(0)
                return

            possibilities = self.getAvailable()
            if (len(possibilities) > 0):
                bot_move = choice(possibilities)
                self.grid[bot_move[0]][bot_move[1]].choice = 1
                self.update()
                if self.checkWin(1):
                    self.endGame(1)
                    return
            else:
                self.endGame(-1)
                return


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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and field.end:
                    field = Field(WIN)
            if event.type == pygame.MOUSEBUTTONDOWN and not field.end:
                x, y = pygame.mouse.get_pos()
                field.move(x, y)
        if not field.end:
            field.update()
            pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()