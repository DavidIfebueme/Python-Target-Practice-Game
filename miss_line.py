import pygame

class MissLine():
    '''A visual aid to display when bullet misses target'''
    def __init__(self, settings, screen):
        '''Initialise miss line'''
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()
        self.width = settings.miss_line_width
        self.height = settings.miss_line_height
        self.colour = (230, 0, 0)
        self.bullet_screen_time = 0
        self.flag = False

        #Create rect and set position
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

    def draw_miss_line(self):
        '''Draw miss line to screen'''
        pygame.draw.rect(self.screen, self.colour, self.rect)