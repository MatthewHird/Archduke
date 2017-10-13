import pygame
import math


class VehicleC:

    DEG = math.pi / 180
    RAD = 180 / math.pi
    black = (0, 0, 0)
    white = (255, 255, 255)

    class Block(pygame.sprite.Sprite):

        def __init__(self, color, width, height):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([width, height])
            self.image.fill(color)
            self.rect = self.image.get_rect()

    def __init__(self):  # , position_x_init, position_y_init, psi_init, engine_power, coefficient_brake, constant_brake,
    #              rho_drag, area_drag, constant_drag, mass_vehicle, axel_front_to_cm, axel_rear_to_cm, delta_steering,
    #              constant_stiffness, inertia_moment_square):

        self.left = 0
        self.right = 0
        self.accel = 0
        self.brake = 0
        self.turn_mod = 1

        self.body = self.Block(self.white, 30, 50)

    def update(self):

        pass

        # self.velocity_0 = self.velocity_1
        # if self.velocity_0 >= 0:
        #     self.velocity_direction = 1
        # elif self.velocity_0 < 0:
        #     self.velocity_direction = -1

        # self.force_engine = self.engine_power * self.accel
        # self.force_brake = self.coefficient_brake * self.constant_brake * self.brake
        # self.force_drag = 0.5 * self.rho_drag * self.area_drag * self.constant_drag * self.velocity_0 ^ 2
        # self.force_road_friction = 30 * self.force_drag / self.velocity_0
        # self.force_long = self.force_engine - (self.force_brake + self.force_drag + self.force_road_friction
        #                                        ) * self.velocity_direction

    def draw(self):
        pass
