import pygame


class Button:
    def __init__(self, display, text, menu_font, hit_font, color):
        self.display = display
        self.text = text
        self.menu_font = menu_font.render(text, 1, color)
        self.hit_font = hit_font.render(text, 1, color)
        self.size = (self.hit_font.get_width(), self.hit_font.get_height())
        self.offset_x = ((self.hit_font.get_width() - self.menu_font.get_width()) / 2)
        self.offset_y = ((self.hit_font.get_height() - self.menu_font.get_height()) / 4)
        self.menu_surf = pygame.Surface(self.size, flags=pygame.SRCALPHA)
        self.menu_surf.fill((0, 0, 0, 0))
        self.hit_surf = pygame.Surface(self.size, flags=pygame.SRCALPHA)
        self.hit_surf.fill((0, 0, 0, 0))
        self.menu_surf.blit(self.menu_font, [self.offset_x, self.offset_y])
        self.hit_surf.blit(self.hit_font, [0, 0])
        self.xy = [0, 0]
        self.rect = None
        
        self.frame_last = 0
        self.frame_next = 1
        self.frame_update = False

    def hit(self):
        pos_x, pos_y = pygame.mouse.get_pos()
        if self.xy[0] <= pos_x <= self.xy[0] + self.size[0] and self.xy[1] <= pos_y <= self.xy[1] + self.size[1]:
            return True
        else:
            return False

    def update(self):
        if self.hit():
            self.frame_next = 2
        else:
            self.frame_next = 1
        if self.frame_next != self.frame_last:
            self.frame_update = True

    def draw(self):
        if self.frame_update:
            if self.frame_next == 1:
                self.display.blit(self.menu_surf, self.xy)
            elif self.frame_next == 2:
                self.display.blit(self.hit_surf, self.xy)

    def cleanup(self):
        self.frame_last = self.frame_next
        self.frame_update = False
