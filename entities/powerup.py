"""
Power-up de tiro duplo — cai ao derrotar inimigos e é coletado pelo jogador.
"""

import pygame
from settings import ALTURA, POWERUP_COR, POWERUP_VELOCIDADE


class PowerUpTiroDuplo(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = self._criar_sprite()
        self.rect = self.image.get_rect(center=(x, y))

    def _criar_sprite(self):
        tamanho = 22
        surf = pygame.Surface((tamanho, tamanho), pygame.SRCALPHA)
        cx, cy = tamanho // 2, tamanho // 2
        # Estrela de 4 pontas
        pontos = [
            (cx,         cy - 10),
            (cx + 4,     cy - 4),
            (cx + 10,    cy),
            (cx + 4,     cy + 4),
            (cx,         cy + 10),
            (cx - 4,     cy + 4),
            (cx - 10,    cy),
            (cx - 4,     cy - 4),
        ]
        pygame.draw.polygon(surf, POWERUP_COR, pontos)
        pygame.draw.polygon(surf, (255, 255, 255), pontos, 1)
        return surf

    def update(self):
        self.rect.y += POWERUP_VELOCIDADE
        if self.rect.top > ALTURA:
            self.kill()
