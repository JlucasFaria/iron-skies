"""
Gerenciador de colisões entre os grupos de sprites do jogo.
"""

import pygame
import random
from entities.explosion import Explosao
from entities.powerup import PowerUpTiroDuplo, PowerUpRicochete, PowerUpVida
from assets.loader import carregar_som
from settings import POWERUP_CHANCE_ARMA, POWERUP_CHANCE_VIDA


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
        acertos = pygame.sprite.groupcollide(
            self.balas_jogador, self.inimigos, True, True
        )
        pontos = 0
        for bala, inimigos_atingidos in acertos.items():
            for inimigo in inimigos_atingidos:
                self.explosoes.add(Explosao(inimigo.rect.centerx, inimigo.rect.centery))
                pontos += inimigo.pontos
                if self._som_explosao:
                    self._som_explosao.set_volume(0.5)
                    self._som_explosao.play()
                self._tentar_drop_powerup(inimigo)
        return pontos

    def _tentar_drop_powerup(self, inimigo):
        x, y = inimigo.rect.centerx, inimigo.rect.centery
        # Power-up de arma (tiro duplo ou ricochete, mutuamente exclusivos)
        if random.random() < POWERUP_CHANCE_ARMA:
            cls = random.choice([PowerUpTiroDuplo, PowerUpRicochete])
            self.powerups.add(cls(x, y))
        # Power-up de vida (chance independente, só dropa se não estiver com vida cheia)
        if random.random() < POWERUP_CHANCE_VIDA:
            self.powerups.add(PowerUpVida(x, y))

    def _jogador_vs_powerups(self):
        coletados = pygame.sprite.spritecollide(self.jogador, self.powerups, True)
        for pu in coletados:
            if pu.tipo == "tiro_duplo":
                self.jogador.ativar_tiro_duplo()
            elif pu.tipo == "ricochete":
                self.jogador.ativar_ricochete()
            elif pu.tipo == "vida":
                self.jogador.ganhar_vida()

    def _balas_inimigas_vs_jogador(self):
        acertos = pygame.sprite.spritecollide(self.jogador, self.balas_inimigas, True)
        if acertos:
            self.jogador.levar_dano()

    def _inimigos_vs_jogador(self):
        acertos = pygame.sprite.spritecollide(self.jogador, self.inimigos, True)
        if acertos:
            for inimigo in acertos:
                self.explosoes.add(Explosao(inimigo.rect.centerx, inimigo.rect.centery))
            self.jogador.levar_dano()
