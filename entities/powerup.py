"""
Power-ups que caem ao derrotar inimigos e são coletados pelo jogador.
  - PowerUpTiroDuplo  : tiro duplo temporário (verde-água)
  - PowerUpRicochete  : tiro ricocheteante temporário (laranja)
  - PowerUpVida       : recupera uma vida (rosa)
"""

import pygame
from settings import (
    ALTURA, POWERUP_VELOCIDADE,
    POWERUP_COR_TIRO_DUPLO, POWERUP_COR_RICOCHETE, POWERUP_COR_VIDA,
)


class _PowerUpBase(pygame.sprite.Sprite):
    """Classe base para todos os power-ups."""

    tipo = None  # sobrescrito pelas subclasses

    def __init__(self, x, y, cor, simbolo):
        super().__init__()
        self.image = self._criar_sprite(cor, simbolo)
        self.rect = self.image.get_rect(center=(x, y))

    def _criar_sprite(self, cor, simbolo):
        tamanho = 24
        surf = pygame.Surface((tamanho, tamanho), pygame.SRCALPHA)
        cx, cy = tamanho // 2, tamanho // 2
        # Hexágono simples como base visual
        pontos = [
            (cx,      cy - 11),
            (cx + 10, cy - 5),
            (cx + 10, cy + 5),
            (cx,      cy + 11),
            (cx - 10, cy + 5),
            (cx - 10, cy - 5),
        ]
        pygame.draw.polygon(surf, cor, pontos)
        pygame.draw.polygon(surf, (255, 255, 255), pontos, 1)
        # Símbolo central
        fonte = pygame.font.SysFont("arial", 13, bold=True)
        txt = fonte.render(simbolo, True, (255, 255, 255))
        surf.blit(txt, txt.get_rect(center=(cx, cy)))
        return surf

    def update(self):
        self.rect.y += POWERUP_VELOCIDADE
        if self.rect.top > ALTURA:
            self.kill()


class PowerUpTiroDuplo(_PowerUpBase):
    tipo = "tiro_duplo"

    def __init__(self, x, y):
        super().__init__(x, y, POWERUP_COR_TIRO_DUPLO, "2x")


class PowerUpRicochete(_PowerUpBase):
    tipo = "ricochete"

    def __init__(self, x, y):
        super().__init__(x, y, POWERUP_COR_RICOCHETE, "~")


class PowerUpVida(_PowerUpBase):
    tipo = "vida"

    def __init__(self, x, y):
        super().__init__(x, y, POWERUP_COR_VIDA, "♥")
