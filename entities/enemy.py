"""
Avião inimigo — desce pela tela e dispara ocasionalmente.
"""

import pygame
import random
from settings import (
    LARGURA, ALTURA,
    INIMIGO_VELOCIDADE_BASE, INIMIGO_COR,
    INIMIGO_LARGURA, INIMIGO_ALTURA,
    INIMIGO_CADENCIA_MIN, INIMIGO_CADENCIA_MAX,
    PONTOS_INIMIGO,
)
from entities.bullet import BalaInimigo
from assets.loader import carregar_imagem


class Inimigo(pygame.sprite.Sprite):

    def __init__(self, x, y, velocidade_extra=0):
        super().__init__()
        self.image = self._criar_sprite()
        self.rect = self.image.get_rect(center=(x, y))

        self.velocidade = INIMIGO_VELOCIDADE_BASE + velocidade_extra
        self.pontos = PONTOS_INIMIGO

        # Temporizador de tiro aleatório
        self._proximo_tiro = pygame.time.get_ticks() + random.randint(
            INIMIGO_CADENCIA_MIN, INIMIGO_CADENCIA_MAX
        )

    # ------------------------------------------------------------------
    def _criar_sprite(self):
        """Carrega sprite do inimigo ou usa forma geométrica como fallback."""
        imagem = carregar_imagem("assets/images/enemy.png", INIMIGO_LARGURA, INIMIGO_ALTURA)
        if imagem:
            # Inimigos descem pela tela — rotaciona 180° para apontar para baixo
            return pygame.transform.rotate(imagem, 180)
        # Fallback geométrico
        surf = pygame.Surface((INIMIGO_LARGURA, INIMIGO_ALTURA), pygame.SRCALPHA)
        pygame.draw.polygon(surf, INIMIGO_COR, [
            (INIMIGO_LARGURA // 2, INIMIGO_ALTURA),
            (INIMIGO_LARGURA,      0),
            (0,                    0),
        ])
        pygame.draw.circle(surf, (255, 180, 180),
                           (INIMIGO_LARGURA // 2, INIMIGO_ALTURA // 3), 5)
        return surf

    # ------------------------------------------------------------------
    def update(self, dt, grupo_balas_inimigas):
        self.rect.y += self.velocidade

        # Remove ao sair da tela pela parte inferior
        if self.rect.top > ALTURA:
            self.kill()

        # Disparo
        agora = pygame.time.get_ticks()
        if agora >= self._proximo_tiro:
            bala = BalaInimigo(self.rect.centerx, self.rect.bottom)
            grupo_balas_inimigas.add(bala)
            self._proximo_tiro = agora + random.randint(
                INIMIGO_CADENCIA_MIN, INIMIGO_CADENCIA_MAX
            )
