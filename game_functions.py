import sys

import pygame
from bullet import Bullet
from alien import Alien


def check_keyup_events(event, ship):
    """Respnd to ke releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respnd to keepasses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K.q:
        sys.exit()


def fire_bullets(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Creat a new bullet and add it to the bullets group.
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mous events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and alien.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Draw the ship.
    ship.blitme()
    # Draw the alien.
    aliens.draw(screen)
    # Make the most recently drawn screen visible, Update screen events.
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update Bullet position.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
    """Respond to bullet-alien collsision."""
    # Remove any bulelt and alien that have collideed.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Destroy exisisting bullet and make a new fleet.
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def check_fleet_edges(ai_settings, aliens):
    """Test if any alien in the group have reached the edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    """Update the position of all aliens in a fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def get_number_row(ai_settings, ship_hieght, alien_hieght):
    """Determine the number of rows ofaliens that fit the on the screen."""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_hieght) -
                         ship_hieght)
    number_row = int(available_space_y / (2 * alien_hieght))
    return number_row


def get_number_alien_x(ai_settings, alien_width):
    """Determine the number of alien that fit in a raw (or x)."""
    available_space_x = ai_settings.scrren_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_nb, row_nb):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_nb)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_nb
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is equalto one alien width.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_row = get_number_row(ai_settings, ship.rect.height,
                                alien.rect.height)
    # Create the first row of aliens.
    for row_nb in range(number_row):
        for alien_nb in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_nb, row_nb)
