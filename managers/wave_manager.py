"""
Gerenciador de ondas de inimigos com dificuldade crescente.
"""

import pygame
import random
from settings import (
    LARGURA,
    INIMIGOS_POR_ONDA_BASE, INIMIGOS_POR_ONDA_EXTRA,
    INTERVALO_SPAWN,
    INIMIGO_LARGURA,
)
from entities.enemy import Inimigo


class GerenciadorOndas:

    def __init__(self, grupo_inimigos, grupo_balas_inimigas):
        self.grupo_inimigos = grupo_inimigos
        self.grupo_balas_inimigas = grupo_balas_inimigas

        self.onda_atual = 1
        self._inimigos_restantes = self._total_da_onda()
        self._ultimo_spawn = pygame.time.get_ticks()
        self._aguardando_limpeza = False  # espera tela limpar antes da próxima onda

    # ------------------------------------------------------------------
    def _total_da_onda(self):
        return INIMIGOS_POR_ONDA_BASE + (self.onda_atual - 1) * INIMIGOS_POR_ONDA_EXTRA

    def _velocidade_extra(self):
        """Aumenta levemente a velocidade a cada onda."""
        return (self.onda_atual - 1) * 0.4

    # ------------------------------------------------------------------
    def atualizar(self, dt):
        """Faz spawn dos inimigos e avança de onda quando necessário."""
        agora = pygame.time.get_ticks()

        # Aguarda a tela ficar limpa de inimigos para iniciar nova onda
        if self._aguardando_limpeza:
            if len(self.grupo_inimigos) == 0:
                self.onda_atual += 1
                self._inimigos_restantes = self._total_da_onda()
                self._aguardando_limpeza = False
                self._ultimo_spawn = agora
            return

        # Faz spawn de um inimigo por intervalo enquanto há restantes
        if self._inimigos_restantes > 0:
            if agora - self._ultimo_spawn >= INTERVALO_SPAWN:
                self._spawnar_inimigo()
                self._inimigos_restantes -= 1
                self._ultimo_spawn = agora
        else:
            # Todos os inimigos da onda foram spawnados — aguarda limpeza
            self._aguardando_limpeza = True

    def _spawnar_inimigo(self):
        margem = INIMIGO_LARGURA
        x = random.randint(margem, LARGURA - margem)
        y = random.randint(-80, -20)
        inimigo = Inimigo(x, y, velocidade_extra=self._velocidade_extra())
        self.grupo_inimigos.add(inimigo)
