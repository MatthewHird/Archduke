import pygame

from display.display import Display
from states.app_states import AppStates
from states.menu import Menu
from states.game import Game
from states.settings import Settings


class App:

    app_name = 'Archduke'
    icon = 'assets/images/icon.png'
    display_width = 800
    display_height = 600

    def __init__(self):
        pass

    def execute(self):
        display = Display(self.app_name, self.icon, self.display_width, self.display_height)
        menu = Menu()

        app_quit = False

        while not app_quit:
            state = menu.run()
            if state == AppStates.game:
                game = Game()
                game_state = game.run()

            elif state == AppStates.quit:
                pygame.quit()


if __name__ == '__main__':
    app = App()
    app.execute()
