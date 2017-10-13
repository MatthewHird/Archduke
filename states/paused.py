import pygame
from objects.button import Button


class Paused:
    pygame.font.init()
    fps = 30

    menu_font = pygame.font.SysFont('calibri', 50)
    hit_font = pygame.font.SysFont('calibri', 60)

    black = (0, 0, 0)
    white = (255, 255, 255)

    btn_names = ['Resume', 'Menu', 'Exit']

    def __init__(self, display, display_size):
        self.return_value = None
        self.display = display
        self.clock = pygame.time.Clock()
        self.display_size = display_size

        self.p_menu = pygame.Surface((round(self.display_size[0] / 2), round(self.display_size[1] / 2)))
        self.p_menu_size = self.p_menu.get_size()
        self.p_menu_xy = ((self.display_size[0] - self.p_menu_size[0]) / 2,
                          (self.display_size[1] - self.p_menu_size[1]) / 2)
        self.p_menu.fill(self.white)
        self.p_menu.set_alpha(127)

        self.buttons = []
        for index, item in enumerate(self.btn_names):
            button = Button(self.display, item, self.menu_font, self.hit_font, self.white)
            button.xy = [self.p_menu_xy[0] + (self.p_menu_size[0] - button.size[0]) / 2,
                         self.p_menu_xy[1] + self.p_menu_size[1] / 2 + button.size[1] * index
                         - (button.size[1] * len(self.btn_names) / 2)]
            button.rect = [button.xy[0], button.xy[1], button.size[0], button.size[1]]
            self.buttons.append(button)

    def run(self):
        self.return_value = None
        self.display.blit(self.p_menu, self.p_menu_xy)
        pygame.display.update()

        while not self.return_value:
            self.events()
            self.update()
            self.draw()
            self.cleanup()

        if self.return_value == 'Resume':
            return None
        else:
            return self.return_value

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.return_value = 'Exit'
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
        self.display.fill(self.black)
        self.display.blit(self.p_menu, self.p_menu_xy)
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
