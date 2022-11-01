import pygame
from pygame.sprite import Group

from shooter import Shooter
from target import Target
from settings import Settings
import game_functions as gf
from game_stats import GameStats
from button import Button
from heads_up_display import HUD
from miss_line import MissLine

def run_game(): 
    '''Initialise game and create screen'''
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_depth))
    pygame.display.set_caption('Target Practice')
    clock = pygame.time.Clock()
    
    bullets_target = []
    shooter = Shooter(screen, settings)
    bullets = Group()
    stats = GameStats(settings, bullets_target)
    target = Target(settings, screen, stats)
    play_button = Button(screen, 'Play')
    hud = HUD(screen, settings, stats, bullets_target)
    m_line = MissLine(settings, screen)

    current_time = 0

    while True:
        current_time = pygame.time.get_ticks()

        total_hits = 0

        gf.check_events(settings, screen, stats, shooter, target, bullets, play_button, hud)
        if stats.game_active:       
            shooter.update_shooter_pos()
            gf.check_bullet_target_collisions(settings, stats, target, bullets, bullets_target, hud)
            gf.check_bullet_screen_edge_collision(stats, screen, bullets, hud, m_line)
        gf.update_screen(settings, screen, stats, shooter, bullets, target, play_button, hud, m_line, clock, current_time)


run_game()