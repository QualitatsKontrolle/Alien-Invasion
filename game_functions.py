import sys, pygame
from bullet import Bullet

def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet & add it to the bullets group
        if len(bullets) < game_settings.bullets_allowed:
            new_bullet = Bullet(game_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(game_settings, screen, ship, bullets):
    """Respond to keypresses & mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.K_SPACE:
            fire_bullet(game_settings, screen, ship, bullets)

def fire_bullet(game_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet"""
    # Create a new bullet & add it to the bullets group
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(game_settings, screen, ship, bullets):
    """Update images on screen & flip to new screen."""
    # Redraw screen during each pass through the loop
    screen.fill(game_settings.bg_color)
    ship.blitme()
    
    # Make most recently drawn screen visible
    pygame.display.flip()
    
    # Redraw all bullets behind ship & aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def update_bullets(bullets):
    """Update position of bullets & get rid of old ones"""
    # Update bullet positions
    bullets.update()
    
    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

