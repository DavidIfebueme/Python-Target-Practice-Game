import pygame

class GameOver():
    '''Game over image'''
    def __init__(self, settings, screen, stats):
        self.settings = settings
        self.screen = screen
        self.stats = stats


        #Load image and get rect
        self.image = pygame.image.load('images/game_over.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Position image
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery - 50

        #Font settings
        self.text_colour = (0, 0, 0)
        self.font = pygame.font.SysFont('arialblack', 20)

        self.prep_stage()
        self.prep_total_hits()
        self.prep_total_misses()

    def prep_stage(self):
        '''Prepare stage image for game over'''
        stage_str = 'Stage: ' + str(self.stats.stage)
        self.stage_image = self.font.render(stage_str, True, self.text_colour,
            self.settings.bg_colour)
    
        #Display image
        self.stage_rect = self.stage_image.get_rect()
        self.stage_rect.top = self.rect.bottom + 5
        self.stage_rect.left = self.screen_rect.left + 100

    def prep_total_hits(self):
        '''Prepare total hits image for game over'''
        total_hits_str = 'Total hits: ' + str(self.stats.total_hits)
        self.total_hits_image = self.font.render(total_hits_str, True, self.text_colour,
            self.settings.bg_colour)

        #Display image
        self.total_hits_rect = self.total_hits_image.get_rect()
        self.total_hits_rect.top = self.rect.bottom + 5
        self.total_hits_rect.left = self.rect.left

    def prep_total_misses(self):
        '''Prepare total misses image for game over'''
        total_misses_str = 'Total misses: ' + str(self.stats.total_misses)
        self.total_misses_image = self.font.render(total_misses_str, True, self.text_colour,
            self.settings.bg_colour)

        #Display image
        self.total_misses_rect = self.total_hits_image.get_rect()
        self.total_misses_rect.top = self.rect.bottom + 5
        self.total_misses_rect.left = self.rect.centerx + 5

    def blitme(self):
        '''Draw game over onto screen'''
        self.screen.blit(self.image, self.rect)
        #self.screen.blit(self.stage_image, self.stage_rect)
        self.screen.blit(self.total_hits_image, self.total_hits_rect)
        self.screen.blit(self.total_misses_image, self.total_misses_rect)