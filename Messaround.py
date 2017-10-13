import pygame


class Button:
    def __init__(self, display, text, menu_font, hit_font, color):
        self.display = display
        self.text = text
        self.menu_surf = menu_font.render(text, 1, color)
        self.hit_surf = hit_font.render(text, 1, color)
        self.size = (self.hit_surf.get_width(), self.hit_surf.get_height())
        self.xy = [0, 0]
        self.offset_xy = ((self.hit_surf.get_width() - self.menu_surf.get_width()) / 2,
                          (self.hit_surf.get_height() - self.menu_surf.get_height()) / 4)

    def hit(self):
        pos_x, pos_y = pygame.mouse.get_pos()
        if self.xy[0] <= pos_x <= self.xy[0] + self.size[0] and self.xy[1] <= pos_y <= self.xy[1] + self.size[1]:
            return self.text
        else:
            return False

    def draw(self):
        pos_x, pos_y = pygame.mouse.get_pos()
        if self.xy[0] <= pos_x <= self.xy[0] + self.size[0] and self.xy[1] <= pos_y <= self.xy[1] + self.size[1]:
            self.display.blit(self.hit_surf, self.xy)
        else:
            self.display.blit(self.menu_surf, [self.xy[0] + self.offset_xy[0], self.xy[1] + self.offset_xy[1]])
