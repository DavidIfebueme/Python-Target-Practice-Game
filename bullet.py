import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A model of a bullet for Sideway Shooter'''
    def __init__(self, screen, settings, shooter):
        '''Create a bullet as shooter's current position'''
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = 60, 60, 60

        #Create bullet rect
        self.rect = pygame.Rect(0,0 , self.bullet_width, self.bullet_height)
        self.rect.centery = shooter.rect.centery
        self.rect.right = shooter.rect.right

        self.center = float(self.rect.centerx)

    def update_position(self):
        '''Move bullet across screen'''
        self.rect.x += 1
        self.center += self.settings.bullet_speed

        self.rect.centerx = self.center

    def draw_bullet(self):
        '''Draw bullet to the screen'''
        pygame.draw.rect(self.screen, self.bullet_colour, self.rect)