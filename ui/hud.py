"""
HUD exibido durante o jogo: pontuação, vidas e número da onda.
"""

import pygame
from settings import (BRANCO, AMARELO, LARGURA, JOGADOR_COR,
                      POWERUP_COR_TIRO_DUPLO, POWERUP_COR_RICOCHETE)


class HUD:

    def __init__(self):
        self._fonte_normal = pygame.font.SysFont("arial", 20, bold=True)
        self._fonte_onda   = pygame.font.SysFont("arial", 18)

    # ------------------------------------------------------------------
    def desenhar(self, tela, pontuacao, vidas, onda, powerup_ativo=None):
        self._desenhar_pontuacao(tela, pontuacao)
        self._desenhar_vidas(tela, vidas)
        self._desenhar_onda(tela, onda)
        if powerup_ativo == "tiro_duplo":
            self._desenhar_powerup(tela, "★ TIRO DUPLO", POWERUP_COR_TIRO_DUPLO)
        elif powerup_ativo == "ricochete":
            self._desenhar_powerup(tela, "~ RICOCHETE", POWERUP_COR_RICOCHETE)

    # ------------------------------------------------------------------
    def _desenhar_pontuacao(self, tela, pontuacao):
        texto = self._fonte_normal.render(f"PONTOS: {pontuacao:06d}", True, AMARELO)
        tela.blit(texto, (10, 10))

    def _desenhar_vidas(self, tela, vidas):
        texto = self._fonte_normal.render("VIDAS:", True, BRANCO)
        tela.blit(texto, (10, 36))
        # Desenha ícones de avião representando cada vida
        for i in range(vidas):
            x = 80 + i * 28
            y = 44
            pontos = [
                (x + 7,  y),
                (x + 14, y + 14),
                (x + 7,  y + 10),
                (x,      y + 14),
            ]
            pygame.draw.polygon(tela, JOGADOR_COR, pontos)

    def _desenhar_onda(self, tela, onda):
        texto = self._fonte_onda.render(f"ONDA: {onda}", True, BRANCO)
        tela.blit(texto, (LARGURA - texto.get_width() - 10, 10))

    def _desenhar_powerup(self, tela, label, cor):
        texto = self._fonte_onda.render(label, True, cor)
        tela.blit(texto, (LARGURA - texto.get_width() - 10, 32))
