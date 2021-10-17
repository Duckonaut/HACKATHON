possibilities = self.getAvailable()
            if (len(possibilities) > 0):
                bot_move = choice(possibilities)
                self.grid[bot_move[0]][bot_move[1]].choice = 1
                self.update()
                if self.checkWin(1):
                    self.endGame(1)
            else:
                self.endGame(-1)