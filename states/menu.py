import pygame
from objects.button import Button
from states.app_states import States


class Menu:
    pygame.font.init()
    fps = 30

    title_font = pygame.font.SysFont('calibri', 100)
    menu_font = pygame.font.SysFont('calibri', 50)
    hit_font = pygame.font.SysFont('calibri', 60)

    black = (0, 0, 0)
    white = (255, 255, 255)

    states = [States.game, States.settings, States.quit]

    def __init__(self, app_name, display, display_size):
        self.return_value = None
        self.display = display
        self.clock = pygame.time.Clock()

        self.display_size = display_size

        self.title_surf = self.title_font.render(app_name, 1, self.white)
        self.title_xy = (display_size[0] / 2 - self.title_surf.get_width() / 2,
                         display_size[1] / 4 - self.title_surf.get_height() / 2)

        self.buttons = []
        for index, item in enumerate(self.states):
            button = Button(display, item.value, self.menu_font, self.hit_font, self.white)
            button.xy = [(display_size[0] - button.size[0]) / 2,
                         display_size[1] * 3 / 4 + button.size[1] * index - (button.size[1] * len(self.states) / 2)]
            self.buttons.append(button)

    def run(self):
        self.return_value = None

        while not self.return_value:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        return self.return_value

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.return_value = States.quit
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in self.buttons:
                    self.return_value = button.hit()

    def update(self):
        pass

    def draw(self):
        self.display.fill(self.black)
        self.display.blit(self.title_surf, self.title_xy)
        for button in self.buttons:
            button.draw()
        pygame.display.update()
