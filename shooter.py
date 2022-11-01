import pygame


class Shooter:
    # creating the shooter/player object
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings


        self.image = pygame.image.load('Images/spacecraft.jpg') #to access the shooter image in folder
        # Next two lines to get rect of image and screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        self.center = float(self.rect.centery) #storing value for shooters center as a float

        # Movement of the shooter
        self.moving_down = False
        self.moving_up = False

    def update_shooter_pos(self):
        # To update the position of the shooter/player
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.settings.shooter_speed

        if self.moving_up and self.rect.top > 0:
            self.center -= self.settings.shooter_speed 

        self.rect.centery = self.center

    def blitme(self):
        # To draw the shooter at the present locations
        self.screen.blit(self.image, self.rect)           
            




