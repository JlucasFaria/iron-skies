"""
Cena principal do jogo — integra todas as entidades e gerenciadores.
"""

import pygame
from settings import (
    LARGURA, ALTURA, AZUL_CEU, BRANCO, PRETO,
    CENA_MENU, CENA_GAME_OVER,
)
from entities.player import Jogador
from entities.explosion import Explosao
from managers.collision_manager import GerenciadorColisao
from managers.wave_manager import GerenciadorOndas
from ui.hud import HUD


class GameCena:

    def __init__(self, tela, estado):
        self.tela = tela
        self.estado = estado

        # Grupos de sprites
        self.grupo_jogador        = pygame.sprite.GroupSingle()
        self.grupo_inimigos       = pygame.sprite.Group()
        self.grupo_balas_jogador  = pygame.sprite.Group()
        self.grupo_balas_inimigas = pygame.sprite.Group()
        self.grupo_explosoes      = pygame.sprite.Group()
        self.todos_sprites        = pygame.sprite.Group()

        # Jogador
        self._jogador = Jogador()
        self.grupo_jogador.add(self._jogador)
        self.todos_sprites.add(self._jogador)

        # Gerenciadores
        self._colisao = GerenciadorColisao(
            self._jogador,
            self.grupo_inimigos,
            self.grupo_balas_jogador,
            self.grupo_balas_inimigas,
            self.grupo_explosoes,
        )
        self._ondas = GerenciadorOndas(self.grupo_inimigos, self.grupo_balas_inimigas)

        self._hud = HUD()
        self._pausado = False
        self._fonte_pausa = pygame.font.SysFont("arial", 40, bold=True)

    # ------------------------------------------------------------------
    def atualizar(self, dt, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                if self._pausado:
                    self._pausado = False
                else:
                    return CENA_MENU

        if self._pausado:
            return None

        # Atualiza entidades
        self._jogador.update(dt, eventos, self.grupo_balas_jogador)
        self.grupo_inimigos.update(dt, self.grupo_balas_inimigas)
        self.grupo_balas_jogador.update()
        self.grupo_balas_inimigas.update()
        self.grupo_explosoes.update()

        # Sincroniza sprites novos com o grupo geral
        self._sincronizar_todos_sprites()

        # Gerenciadores
        self._ondas.atualizar(dt)
        pontos_ganhos = self._colisao.processar()

        # Atualiza estado compartilhado
        self.estado["pontuacao"] += pontos_ganhos
        self.estado["onda"] = self._ondas.onda_atual

        # Verifica game over
        if not self._jogador.esta_vivo():
            return CENA_GAME_OVER

        return None

    def desenhar(self):
        self.tela.fill(AZUL_CEU)
        self._desenhar_fundo()

        self.grupo_balas_jogador.draw(self.tela)
        self.grupo_balas_inimigas.draw(self.tela)
        self.grupo_inimigos.draw(self.tela)
        self.grupo_jogador.draw(self.tela)
        self.grupo_explosoes.draw(self.tela)

        self._hud.desenhar(
            self.tela,
            self.estado["pontuacao"],
            self._jogador.vidas,
            self.estado["onda"],
        )

        if self._pausado:
            self._desenhar_pausa()

    # ------------------------------------------------------------------
    def _sincronizar_todos_sprites(self):
        """Garante que balas e explosões novas apareçam no grupo geral."""
        self.todos_sprites.add(
            *self.grupo_balas_jogador,
            *self.grupo_balas_inimigas,
            *self.grupo_inimigos,
            *self.grupo_explosoes,
        )

    def _desenhar_fundo(self):
        """Linhas verticais simulando movimento do céu."""
        import random
        rng = random.Random(42)
        for _ in range(40):
            x = rng.randint(0, LARGURA)
            y = rng.randint(0, ALTURA)
            pygame.draw.circle(self.tela, (60, 90, 150), (x, y), 1)

    def _desenhar_pausa(self):
        overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 120))
        self.tela.blit(overlay, (0, 0))
        texto = self._fonte_pausa.render("PAUSADO", True, BRANCO)
        self.tela.blit(texto, texto.get_rect(center=(LARGURA // 2, ALTURA // 2)))
