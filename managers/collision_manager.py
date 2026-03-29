"""
Gerenciador de colisões entre os grupos de sprites do jogo.
"""

import pygame
from entities.explosion import Explosao


class GerenciadorColisao:

    def __init__(self, jogador, inimigos, balas_jogador, balas_inimigas, explosoes):
        self.jogador = jogador
        self.inimigos = inimigos
        self.balas_jogador = balas_jogador
        self.balas_inimigas = balas_inimigas
        self.explosoes = explosoes

    # ------------------------------------------------------------------
    def processar(self):
        """Verifica todas as colisões e retorna os pontos ganhos no frame."""
        pontos = 0
        pontos += self._balas_jogador_vs_inimigos()
        self._balas_inimigas_vs_jogador()
        self._inimigos_vs_jogador()
        return pontos

    # ------------------------------------------------------------------
    def _balas_jogador_vs_inimigos(self):
        """Bala do jogador acerta inimigo — remove ambos e gera explosão."""
        acertos = pygame.sprite.groupcollide(
            self.balas_jogador, self.inimigos, True, True
        )
        pontos = 0
        for bala, inimigos_atingidos in acertos.items():
            for inimigo in inimigos_atingidos:
                explosao = Explosao(inimigo.rect.centerx, inimigo.rect.centery)
                self.explosoes.add(explosao)
                pontos += inimigo.pontos
        return pontos

    def _balas_inimigas_vs_jogador(self):
        """Bala inimiga acerta o jogador — remove a bala e aplica dano."""
        acertos = pygame.sprite.spritecollide(
            self.jogador, self.balas_inimigas, True
        )
        if acertos:
            self.jogador.levar_dano()

    def _inimigos_vs_jogador(self):
        """Inimigo colide diretamente com o jogador — remove inimigo e aplica dano."""
        acertos = pygame.sprite.spritecollide(
            self.jogador, self.inimigos, True
        )
        if acertos:
            for inimigo in acertos:
                explosao = Explosao(inimigo.rect.centerx, inimigo.rect.centery)
                self.explosoes.add(explosao)
            self.jogador.levar_dano()
