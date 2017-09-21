import math
import pygame
import time
import random

from display.display import Display
from states.app_states import AppStates


class App:

    app_name = 'Archduke'
    icon = 'assets/images/icon.png'
    display_width = 800
    display_height = 600

    def __init__(self):
        pass

    def execute(self):
        display = Display(self.app_name, self.icon, self.display_width, self.display_height)


if __name__ == '__main__':
    app = App()
    app.execute()
