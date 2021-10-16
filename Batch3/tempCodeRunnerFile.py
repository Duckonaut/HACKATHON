for x in range(17):
            pygame.draw.rect(self._win, White, (0, self._n * x, WIDTH, LINE_WIDTH))
            pygame.draw.rect(self._win, White, (self._n * x, 0, LINE_WIDTH, HEIGHT))