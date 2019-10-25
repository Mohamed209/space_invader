import random

import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, surw, surh):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((surw, surh))
        self.surf.fill((255, 255, 255))
        self.envw = 0
        self.envh = 0
        self.speed = random.randint(5, 20)

    def set_enemy_env(self, envw, envh):
        self.envw = envw
        self.envh = envh
        self.rect = self.surf.get_rect(
            center=(
                random.randint(self.envw + 20, self.envw + 100),
                random.randint(0, self.envh),
            ))

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
