import pygame

from display.display import Display
from states.app_states import States
from states.menu import Menu
from states.game import Game
from states.settings import Settings


class App:

    app_name = 'Archduke'
    icon = 'assets/images/icon.png'
    display_size = (800, 600)

    def __init__(self):
        self.state = States.menu
        self.settings = States.settings

    def execute(self):
        display_init = Display(self.app_name, self.icon, self.display_size[0], self.display_size[1])
        display_init.run()
        display = display_init.display
        menu = Menu(self.app_name, display, self.display_size)

        app_quit = False

        while not app_quit:
            if self.state == States.menu:
                self.state = menu.run()
            elif self.state == States.game:
                game = Game()
                self.state = game.run()
            elif self.state == States.options:
                self.state = self.settings.run()
            elif self.state == States.quit:
                app_quit = True


if __name__ == '__main__':
    app = App()
    app.execute()
