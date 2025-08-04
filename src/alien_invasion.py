import sys
import pygame
from .settings import Settings


class AlienInvasion:
    """Startin point of the game"""

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = self.settings.bg_color

    # function to run the game
    def run_game(self):
        """Start the main loop for the game."""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screenn during each pass through the loop
            self.screen.fill(self.bg_color)

            pygame.display.flip()
            self.clock.tick(60)
