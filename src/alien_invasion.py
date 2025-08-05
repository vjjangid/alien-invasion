import sys
import pygame
from .settings import Settings
from .ships import Ship


class AlienInvasion:
    """Startin point of the game"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.moving_right = False
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = self.settings.bg_color

    # function to run the game
    def run_game(self):
        """Start the main loop for the game."""

        while True:
            self._check_events()
            self._update_screen()

            self.clock.tick(60)

    def _check_events(self):
        """REspond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                    self.moving_right = True
                    # move the ship to right
                    self.ship.rect.x += 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                    self.moving_right = False

    def _update_screen(self):
        # Redraw the screenn during each pass through the loop
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        pygame.display.flip()

    def update(self):
        """Update the ship position based on the movement flag."""

        if self.moving_right:
            self.rect.x += 1
