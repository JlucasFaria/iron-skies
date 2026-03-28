"""
Projéteis disparados pelo jogador e pelos inimigos.
"""

import pygame
from settings import (
    BALA_JOGADOR_VELOCIDADE, BALA_JOGADOR_COR,
    BALA_JOGADOR_LARGURA, BALA_JOGADOR_ALTURA,
    BALA_INIMIGO_VELOCIDADE, BALA_INIMIGO_COR,
    BALA_INIMIGO_LARGURA, BALA_INIMIGO_ALTURA,
    ALTURA,
)


class Bala(pygame.sprite.Sprite):
    """Projétil genérico — direção -1 (para cima) ou +1 (para baixo)."""

    def __init__(self, x, y, direcao, velocidade, cor, largura, altura):
        super().__init__()
        self.image = pygame.Surface((largura, altura), pygame.SRCALPHA)
        pygame.draw.rect(self.image, cor, (0, 0, largura, altura), border_radius=3)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidade = velocidade * direcao  # negativo = sobe, positivo = desce

    def update(self):
        self.rect.y += self.velocidade
        # Remove ao sair da tela
        if self.rect.bottom < 0 or self.rect.top > ALTURA:
            self.kill()


class BalaJogador(Bala):
    """Projétil disparado pelo jogador (sobe)."""

    def __init__(self, x, y):
        super().__init__(
            x, y,
            direcao=-1,
            velocidade=BALA_JOGADOR_VELOCIDADE,
            cor=BALA_JOGADOR_COR,
            largura=BALA_JOGADOR_LARGURA,
            altura=BALA_JOGADOR_ALTURA,
        )


class BalaInimigo(Bala):
    """Projétil disparado por inimigo (desce)."""

    def __init__(self, x, y):
        super().__init__(
            x, y,
            direcao=+1,
            velocidade=BALA_INIMIGO_VELOCIDADE,
            cor=BALA_INIMIGO_COR,
            largura=BALA_INIMIGO_LARGURA,
            altura=BALA_INIMIGO_ALTURA,
        )
