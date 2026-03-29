"""
Gerenciador de colisões entre os grupos de sprites do jogo.
"""

import pygame
import random
from entities.explosion import Explosao
from entities.powerup import PowerUpTiroDuplo
from assets.loader import carregar_som
from settings import POWERUP_CHANCE


class GerenciadorColisao:

    def __init__(self, jogador, inimigos, balas_jogador, balas_inimigas, explosoes, powerups):
        self.jogador = jogador
        self.inimigos = inimigos
        self.balas_jogador = balas_jogador
        self.balas_inimigas = balas_inimigas
        self.explosoes = explosoes
        self.powerups = powerups
        self._som_explosao = carregar_som("assets/sounds/explosion.ogg")

    # ------------------------------------------------------------------
    def processar(self):
        """Verifica todas as colisões e retorna os pontos ganhos no frame."""
        pontos = 0
        pontos += self._balas_jogador_vs_inimigos()
        self._balas_inimigas_vs_jogador()
        self._inimigos_vs_jogador()
        self._jogador_vs_powerups()
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
                if self._som_explosao:
                    self._som_explosao.set_volume(0.5)
                    self._som_explosao.play()
                # Chance de dropar power-up
                if random.random() < POWERUP_CHANCE:
                    pu = PowerUpTiroDuplo(inimigo.rect.centerx, inimigo.rect.centery)
                    self.powerups.add(pu)
        return pontos

    def _jogador_vs_powerups(self):
        """Jogador coleta power-up ao tocar nele."""
        coletados = pygame.sprite.spritecollide(self.jogador, self.powerups, True)
        for _ in coletados:
            self.jogador.ativar_tiro_duplo()

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
