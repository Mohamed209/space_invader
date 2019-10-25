import pygame


class GameEnvironment:
    """
    Game environment class simulate game objects and their interactions
    """

    SCREEN_WIDTH = 0
    SCREEN_HEIGHT = 0

    def __init__(self, screen_width, screen_height, run=True):
        pygame.init()
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.game_run = run
