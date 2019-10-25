import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)


class Player(pygame.sprite.Sprite):
    """
    class to simulate player sprites and actions
    """

    def __init__(self, surw, surh):
        super(Player, self).__init__()
        self.surf = pygame.Surface((surw, surh))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.envw = 0
        self.envh = 0

    def set_player_env(self, w, h):
        self.envw = w
        self.envh = h

    # Move the sprite based on user key presses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            if self.rect.top <= 0:
                self.rect.top = 0
            else:
                self.rect.move_ip(0, -1)
        elif pressed_keys[K_DOWN]:
            if self.rect.bottom >= self.envh:
                self.rect.bottom = self.envh
            else:
                self.rect.move_ip(0, 1)
        elif pressed_keys[K_LEFT]:
            if self.rect.left <= 0:
                self.rect.left = 0
            else:
                self.rect.move_ip(-1, 0)
        elif pressed_keys[K_RIGHT]:
            if self.rect.right >= self.envw:
                self.rect.right = self.envw
            else:
                self.rect.move_ip(1, 0)
        else:
            pass
