import pygame
import os
import math


class Vehicle(pygame.sprite.Sprite):

    DEG = math.pi / 180
    white = (255, 255, 255)
    black = (0, 0, 0)

    image = pygame.image.load('assets/images/car.png')

    def __init__(self, display):
        pygame.sprite.Sprite.__init__(self)

        self.display = display
        self.play_width = display.get_width()
        self.play_height = display.get_height()

        self.rect = None
        self.theta = 0
        self.x_0 = self.play_width / 2
        self.y_0 = self.play_height / 2
        self.x_1 = self.x_0
        self.y_1 = self.y_0
        self.width = self.image.get_width
        self.height = self.image.get_height
        self.offset_x = 0
        self.offset_y = 0
        self.image_trans = None
        self.accel = 0
        self.gas = 0
        self.brake = 0
        self.left = 0
        self.right = 0
        self.turn_mod = 1
        self.speed = 0
        self.direction = 0
        self.drag = 0

    def update(self, boundary):
        self.x_0 = self.x_1
        self.y_0 = self.y_1

        self.theta = ((self.theta + self.turn_mod * (self.left + self.right)) + 360) % 360
        self.direction = self.theta
        self.image_trans = pygame.transform.rotate(self.image, -1 * self.theta)
        self.offset_x = 15 * abs(math.cos(self.theta * self.DEG)) \
                        + 25 * abs(math.sin(self.theta * self.DEG))
        self.offset_y = 25 * abs(math.cos(self.theta * self.DEG)) \
                        + 15 * abs(math.sin(self.theta * self.DEG))

        self.accel = self.gas - self.brake

        if self.speed == 0:
            self.drag = 0
        elif self.speed > 0:
            self.drag = 0.02
        elif self.speed < 0:
            self.drag = -0.02

        self.speed = self.speed + self.accel - self.drag

        if -0.5 < self.speed < 0.5:
            self.speed = 0
        elif self.speed > 6:
            self.speed = 6
        elif self.speed < -2:
            self.speed = -2

        self.x_1 = self.x_0 + self.speed * math.sin(self.theta * self.DEG)
        self.y_1 = self.y_0 - self.speed * math.cos(self.theta * self.DEG)
        self.rect = pygame.Rect([self.x_1 - self.offset_x, self.y_1 - self.offset_y,
                                 self.image_trans.get_width(), self.image_trans.get_height()])

        self.hit_boundary(boundary)

    def draw(self):
        self.display.blit(self.image_trans, (self.x_1 - self.offset_x, self.y_1 - self.offset_y))

    def hit_boundary(self, boundary):
        def callback(rect):
            def collide(one, two):
                return rect.colliderect(two.rect)
            return collide

        collisions = pygame.sprite.spritecollide(self, boundary, False, callback(self.rect))
        for wall in collisions:
            self.x_1 = self.x_0 + wall.bump_x
            self.y_1 = self.y_0 + wall.bump_y
            self.speed = 0