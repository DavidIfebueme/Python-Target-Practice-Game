import pygame

class Target():
    '''A target to aim for in Sideway Shooter'''
    def __init__(self, settings, screen, stats):
        '''Initialise target onto screen'''
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.screen_rect = screen.get_rect()
        self.width = settings.target_width
        self.height = settings.target_height
        self.colour = (255, 0, 0)

        #Create rect and set position
        self.rect = pygame.Rect(0,0 , self.width, self.height)
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

        self.centery = float(self.rect.centery)

    def update_target(self):
        self.centery -= (self.settings.target_speed*
                            self.settings.target_direction)
                            
        self.rect.centery = self.centery

    def reduce_target_height(self):
        self.rect.inflate_ip(0, -20)
        self.height -= 20
        for x in [1, 4, 7, 10, 13]:
            if x == self.stats.stage:
                self.colour = (255, 0, 0)
        for x in [2, 5, 8, 11, 14]:
            if x == self.stats.stage:
                self.colour = (0, 255, 0)
        for x in [3, 6, 9, 12, 15]:
            if x == self.stats.stage:
                self.colour = (0, 0, 255)

    def initialise_target(self):
        self.rect.inflate_ip(0, 300 - self.height)
        self.height = self.settings.target_height
        self.centery = self.screen_rect.centery
        self.colour = (255, 0, 0)

    def check_edges(self):
        if self.rect.top == self.screen_rect.top:
            return True
        if self.rect.bottom == self.screen_rect.bottom:
            return True

    def draw_target(self):
        '''Draw target to the screen'''
        pygame.draw.rect(self.screen, self.colour, self.rect)