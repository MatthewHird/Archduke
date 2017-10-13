import pygame


class Boundary:
    def __init__(self, display, display_size):
        self.display = display
        self.display_size = display_size
        self.walls = self.spawn_walls()

    def spawn_walls(self):
        left = self.Wall([-1, 0, 1, self.display_size[1]], 1, 0)
        right = self.Wall([self.display_size[0], 0, 1, self.display_size[1]], -1, 0)
        top = self.Wall([0, -1, self.display_size[0], 1], 0, 1)
        bot = self.Wall([0, self.display_size[1], self.display_size[0], 1], 0, -1)
        return pygame.sprite.Group([left, right, top, bot])

    class Wall(pygame.sprite.Sprite):
        def __init__(self, rect, bump_x, bump_y):
            pygame.sprite.Sprite.__init__(self)
            self.rect = pygame.Rect(rect)
            self.bump_x = bump_x
            self.bump_y = bump_y