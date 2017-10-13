import pygame
from states.app_states import States
from objects.button import Button


class Menu:
    pygame.font.init()
    fps = 30

    title_font = pygame.font.SysFont('calibri', 100)
    menu_font = pygame.font.SysFont('calibri', 50)
    hit_font = pygame.font.SysFont('calibri', 60)

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    bg_color = black

    btn_names = ['Start', 'Settings', 'Exit']

    def __init__(self, app_name, display, display_size):
        self.return_value = None
        self.display = display
        self.clock = pygame.time.Clock()
        self.display_size = display_size

        self.title_font = self.title_font.render(app_name, 1, self.white)
        self.title_size = (self.title_font.get_width(), self.title_font.get_height())
        self.title_xy = (display_size[0] / 2 - self.title_font.get_width() / 2,
                         display_size[1] / 4 - self.title_font.get_height() / 2)
        self.title_surf = pygame.Surface(self.title_size, flags=pygame.SRCALPHA)
        self.title_surf.fill((0, 0, 0, 0))
        self.title_surf.blit(self.title_font, (0, 0))

        self.buttons = []
        for index, item in enumerate(self.btn_names):
            button = Button(self.display, item, self.menu_font, self.hit_font, self.white)
            button.xy = [(display_size[0] - button.size[0]) / 2,
                         display_size[1] * 3 / 4 + button.size[1] * index - (button.size[1] * len(self.btn_names) / 2)]
            button.rect = [button.xy[0], button.xy[1], button.size[0], button.size[1]]
            self.buttons.append(button)

    def run(self):
        self.return_value = None
        self.display.fill(self.bg_color)
        self.display.blit(self.title_surf, self.title_xy)
        pygame.display.update()

        while not self.return_value:
            self.events()
            self.update()
            self.draw()
            self.cleanup()

        return self.return_value

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.return_value = States.app_exit
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in self.buttons:
                    hit = button.hit()
                    if hit:
                        self.return_value = button.text

    def update(self):
        for button in self.buttons:
            button.update()

    def draw(self):
        update_list = []
        self.display.fill(self.bg_color)
        self.display.blit(self.title_surf, self.title_xy)
        for button in self.buttons:
            if button.frame_update:
                button.draw()
                update_list.append(button.rect)

        pygame.display.update(update_list)

    def cleanup(self):
        for button in self.buttons:
            button.cleanup()
        self.clock.tick(self.fps)
        pygame.display.set_caption("fps: " + str(round(self.clock.get_fps(), 1)))
