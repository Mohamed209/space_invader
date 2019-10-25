import pygame
from pygame.locals import (
    KEYDOWN,
    K_ESCAPE,
    QUIT
)

from src.game_environment import GameEnvironment
from src.player import Player
from src.enemy import Enemy

if __name__ == '__main__':
    game = GameEnvironment(500, 500)
    player = Player(50, 50)
    player.set_player_env(game.SCREEN_HEIGHT, game.SCREEN_WIDTH)
    while game.game_run:
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    game.game_run = False
            # Check for QUIT event. If QUIT, then set running to false.
            elif event.type == QUIT:
                game.game_run = False

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user keypresses
        player.update(pressed_keys)
        # Fill the screen with black
        game.screen.fill((0, 0, 0))

        # Draw the player on the screen
        game.screen.blit(player.surf, player.rect)

        # Update the display
        pygame.display.flip()
