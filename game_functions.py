import pygame
import sys

from bullet import Bullet
from game_over import GameOver

def check_events(settings, screen, stats, shooter, target, bullets,play_button, hud):
    # Running checks for keyboard and mouse events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, settings, shooter, target, stats, bullets, hud)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, shooter)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, stats, target, bullets, play_button, mouse_x, mouse_y, hud)


def check_play_button(settings, stats, target, bullets, play_button, mouse_x, mouse_y, hud):
    # List of events that happen when the player clicks play
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    
    if button_clicked and not stats.game_active:
        settings.initialise_dynamic_settings()
        start_game(stats, target, bullets, hud)


def start_game(stats, target, bullets, hud):
    # Function to start the game
    stats.reset_stats()
    bullets.empty()
    hud.prep_hits()
    hud.prep_misses()
    stats.stage = 1
    hud.prep_stage()
    target.initialise_target()
    stats.game_active = True

def check_keydown_events(event, screen, settings, shooter, target, stats, bullets, hud):
    #Function to check when a key is pressed

    if event.key == pygame.K_UP:
        shooter.moving_up = True
    if event.key == pygame.K_DOWN:
        shooter.moving_down = True
    if event.key == pygame.K_SPACE:
        new_bullet = Bullet(screen, settings, shooter)
        bullets.add(new_bullet)
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_p:
        if event.game_active == False:
            start_game(stats, target, bullets, hud)


def check_keyup_events(event, shooter):
    # Checks for key releases

    if event.key == pygame.K_UP:
        shooter.moving_up = False
    if event.key == pygame.K_DOWN:
        shooter.moving_down = False

def update_bullets(settings, bullets):
    for bullet in bullets.sprites():
        bullet.update_position()
        bullet.draw_bullet()
        # Reminder to write function to kill bullet after it leaves the screen


    for bullet in bullets.copy():
        if bullet.rect.left >= settings.screen_width:
            bullets. remove(bullet) # Killing bullet after it leaves the screen to optimize game


def update_target(settings, target):
    if target.check_edges():
        settings.target_direction *= -1

    target.update_target()

def check_bullet_target_collisions(settings, stats, target, bullets, bullets_target, hud):
    # What happens when bullet hits target
    if pygame.sprite.spritecollideany(target, bullets):
        for bullet in bullets.copy():
            if bullet.rect.right >= target.rect.left:
                bullets_target.append(bullet)
                bullets.remove(bullet)
                stats.total_hits += 1
                hud.prep_hits()
                hud.prep_misses()
                if len(bullets_target) == settings.target_hits:
                    level_up(bullets_target, stats, target, hud)


def level_up(bullets_target, stats, target, hud):
    bullets_target.clear()
    stats.reset_stats()
    stats.stage += 1
    hud.prep_stage()
    hud.prep_misses()
    target.reduce_target_height()


def check_bullet_screen_edge_collision(stats, screen, bullets, hud, m_line):
      screen_rect = screen.get_rect()
      for bullet in bullets.copy():
        if bullet.rect.right >= screen_rect.right:
            m_line.flag = True
            m_line.bullet_screen_time = pygame.time.get_ticks()
            bullets.remove(bullet)
            stats.bullets_left -= 1
            stats.total_misses += 1
            hud.prep_misses()

def game_over(settings, screen, stats):
    go = GameOver(settings, screen, stats)
    if stats.bullets_left == 0: 
        stats.game_active = False
        go.blitme() 


def update_screen(settings, screen, stats, shooter, bullets, target, play_button, hud, m_line, clock, current_time):
    # Function to update screen features
    screen.fill(settings.bg_colour)
    update_bullets(settings, bullets)
    update_target(settings, target)
    shooter.blitme()
    if m_line.flag == True:
        m_line.draw_miss_line()

    if current_time - m_line.bullet_screen_time > 50:
        m_line.flag = False
    target.draw_target()
    hud.show_info()
    game_over(settings, screen, stats)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
    clock.tick(60)    
