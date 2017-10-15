import pygame
from objects.vehicle import Vehicle
from objects.boundary import Boundary
from states.paused import Paused


class Game:
    fps = 60
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    bg_color = black

    def __init__(self, app_name, display, display_size):
        self.return_value = None
        self.display = display
        self.clock = pygame.time.Clock()
        self.display_size = display_size
        self.app_name = app_name
        self.vehicle = Vehicle(self.display)
        self.boundary_init = Boundary(self.display, self.display_size)
        self.boundary = self.boundary_init.walls
        self.p_menu = Paused(self.display, self.display_size, self.bg_color)
        self.paused = None

    def run(self):
        self.return_value = None

        while not self.return_value:
            if self.paused:
                self.return_value = self.p_menu.events()
                self.p_menu.update()
                if self.return_value == 'Resume':
                    self.return_value = None
            else:
                self.events()
                self.update()

            self.draw()
            if self.paused:
                self.p_menu.draw()

            if self.paused:
                self.p_menu.cleanup()
            else:
                self.cleanup()

        return self.return_value

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.return_value = 'Exit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.vehicle.left = -1
                elif event.key == pygame.K_d:
                    self.vehicle.right = 1
                elif event.key == pygame.K_w:
                    self.vehicle.gas = 1
                elif event.key == pygame.K_s:
                    self.vehicle.brake = 1
                elif event.key == pygame.K_RSHIFT:
                    self.vehicle.turn_mod = 2

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.vehicle.left = 0
                elif event.key == pygame.K_d:
                    self.vehicle.right = 0
                elif event.key == pygame.K_w:
                    self.vehicle.gas = 0
                elif event.key == pygame.K_s:
                    self.vehicle.brake = 0
                elif event.key == pygame.K_RSHIFT:
                    self.vehicle.turn_mod = 1
                elif event.key == pygame.K_p:
                    self.paused = True
                    self.p_menu.run()

    def update(self):
        self.vehicle.update(self.boundary)

    def draw(self):
        self.display.fill(self.bg_color)
        self.vehicle.draw()
        if not self.paused:
            pygame.display.update()

    def cleanup(self):
        self.clock.tick(self.fps)
        pygame.display.set_caption("fps: " + str(round(self.clock.get_fps(), 1)))
