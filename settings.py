class Settings():
    '''Sideway Shooter settings'''
    def __init__(self):
        '''Initialise static game settings'''
        #Screen settings
        self.screen_width = 600
        self.screen_depth = 600
        self.bg_colour = (230, 230, 230)
        
        #Ship settings
        self.shooter_speed = 12

        #Bullet settings
        self.bullet_speed = 18
        self.target_misses_allowed = 5
        
        #Target settings
        self.target_hits = 10
        self.target_width = 10
        self.target_direction = 1
        self.target_speed = 5

        #Miss line settings
        self.miss_line_width = 5
        self.miss_line_height = self.screen_depth

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        '''Initialise dynamic game settings'''
        #Target settings
        self.target_height = 300