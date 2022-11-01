class GameStats():
    '''Track stats for Target Practice'''
    def __init__(self, settings, bullets_target):
        self.settings = settings
        #self.target = target
        self.bullets_target = bullets_target
        self.reset_stats()
        self.game_active = False
        self.stage = 1
        self.total_hits = 0
        self.total_misses = 0

    def reset_stats(self):
        '''Rest game stats'''
        self.bullets_left = self.settings.target_misses_allowed
        self.bullets_target.clear()