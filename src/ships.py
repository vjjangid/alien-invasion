import pygame


class Ship:
    """code related to ship"""

    def __init__(self, alien_game):
        """Initialize the ship and set its starting position"""
        self.screen = alien_game.screen
        self.screen_rect = alien_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load("content/images/ship.bmp")
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw sthe ship at its curren location"""
        self.screen.blit(self.image, self.rect)
