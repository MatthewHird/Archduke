import pygame
from states.app_states import States
from objects.button import Button


class Settings:
    fps = 30

    def __init__(self):
        self.return_value = None
        self.clock = pygame.time.Clock()

    def run(self):
        self.return_value = None

        while not self.return_value:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        return self.return_value

    def events(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass
