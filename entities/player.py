"""
Avião controlado pelo jogador.
"""

import pygame
from settings import (
    LARGURA, ALTURA,
    JOGADOR_VELOCIDADE, JOGADOR_VIDAS, JOGADOR_CADENCIA,
    JOGADOR_COR, JOGADOR_LARGURA, JOGADOR_ALTURA,
)
from entities.bullet import BalaJogador


class Jogador(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = self._criar_sprite()
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA // 2
        self.rect.bottom = ALTURA - 20

        self.vidas = JOGADOR_VIDAS
        self._ultimo_tiro = 0       # timestamp do último disparo (ms)
        self.invencivel = False     # pisca após levar dano
        self._tempo_invencivel = 0
        self._duracao_invencivel = 1500  # ms

    # ------------------------------------------------------------------
    def _criar_sprite(self):
        """Desenha o avião como forma geométrica (fallback sem imagem)."""
        surf = pygame.Surface((JOGADOR_LARGURA, JOGADOR_ALTURA), pygame.SRCALPHA)
        # Corpo central
        pygame.draw.polygon(surf, JOGADOR_COR, [
            (JOGADOR_LARGURA // 2, 0),
            (JOGADOR_LARGURA,      JOGADOR_ALTURA),
            (JOGADOR_LARGURA // 2, JOGADOR_ALTURA - 10),
            (0,                    JOGADOR_ALTURA),
        ])
        # Detalhe da cabine
        pygame.draw.circle(surf, (200, 230, 255),
                           (JOGADOR_LARGURA // 2, JOGADOR_ALTURA // 3), 6)
        return surf

    # ------------------------------------------------------------------
    def update(self, dt, eventos, grupo_balas):
        teclas = pygame.key.get_pressed()
        self._mover(teclas)
        self._verificar_tiro(teclas, dt, grupo_balas)
        self._atualizar_invencibilidade(dt)

    def _mover(self, teclas):
        if teclas[pygame.K_LEFT]  and self.rect.left > 0:
            self.rect.x -= JOGADOR_VELOCIDADE
        if teclas[pygame.K_RIGHT] and self.rect.right < LARGURA:
            self.rect.x += JOGADOR_VELOCIDADE
        if teclas[pygame.K_UP]   and self.rect.top > 0:
            self.rect.y -= JOGADOR_VELOCIDADE
        if teclas[pygame.K_DOWN] and self.rect.bottom < ALTURA:
            self.rect.y += JOGADOR_VELOCIDADE

    def _verificar_tiro(self, teclas, dt, grupo_balas):
        agora = pygame.time.get_ticks()
        if teclas[pygame.K_SPACE]:
            if agora - self._ultimo_tiro >= JOGADOR_CADENCIA:
                bala = BalaJogador(self.rect.centerx, self.rect.top)
                grupo_balas.add(bala)
                self._ultimo_tiro = agora

    def _atualizar_invencibilidade(self, dt):
        if self.invencivel:
            self._tempo_invencivel += dt
            if self._tempo_invencivel >= self._duracao_invencivel:
                self.invencivel = False
                self._tempo_invencivel = 0
                self.image.set_alpha(255)
            else:
                # Efeito de piscar alternando opacidade
                alpha = 80 if (self._tempo_invencivel // 150) % 2 == 0 else 255
                self.image.set_alpha(alpha)

    # ------------------------------------------------------------------
    def levar_dano(self):
        """Reduz uma vida e ativa invencibilidade temporária."""
        if self.invencivel:
            return
        self.vidas -= 1
        self.invencivel = True
        self._tempo_invencivel = 0

    def esta_vivo(self):
        return self.vidas > 0
