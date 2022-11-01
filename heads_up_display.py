import pygame.font

class HUD():
    '''A class that shows game information'''
    def __init__(self, screen, settings, stats, bullets_target):
        '''Initialise HUD information'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        self.bullets_target = bullets_target

        #Font settings
        self.text_colour = (100, 0, 0)
        self.font = pygame.font.SysFont('arialblack', 20)

        self.prep_stage()
        self.prep_hits()
        self.prep_misses()

    def prep_stage(self):
        '''Prepare image for stage in game'''
        stage_str = 'Stage: ' + str(self.stats.stage)
        self.stage_image = self.font.render(stage_str, True, self.text_colour,
            self.settings.bg_colour)
        
        #Display image
        self.stage_rect = self.stage_image.get_rect()
        self.stage_rect.left = self.screen_rect.left + 5
        self.stage_rect.top = self.screen_rect.top + 5

    def prep_hits(self):
        '''Prepare image for hits in game'''
        hits_str = 'Hits: ' + str(len(self.bullets_target)) + '/' + str(self.settings.target_hits)
        self.hits_image = self.font.render(hits_str, True, self.text_colour, 
            self.settings.bg_colour)

        #Display image
        self.hits_rect = self.hits_image.get_rect()
        self.hits_rect.left = self.stage_rect.right + 50
        self.hits_rect.top = self.screen_rect.top + 5

    def prep_misses(self):
        '''Prepare image for misses in game'''
        misses_str = 'Misses: ' + str(self.stats.bullets_left)
        self.misses_image = self.font.render(misses_str, True, self.text_colour,
            self.settings.bg_colour)

        #Display image
        self.misses_rect = self.misses_image.get_rect()
        self.misses_rect.left = self.hits_rect.right + 50
        self.misses_rect.top = self.screen_rect.top + 5

    def show_info(self):
        '''Draw info to screen'''
        self.screen.blit(self.hits_image, self.hits_rect)
        self.screen.blit(self.misses_image, self.misses_rect)
        self.screen.blit(self.stage_image, self.stage_rect)