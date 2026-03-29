"""
Cena principal do jogo — integra todas as entidades e gerenciadores.
"""

import pygame
from settings import (
    LARGURA, ALTURA, AZUL_CEU, BRANCO, PRETO,
    CENA_MENU, CENA_GAME_OVER,
)
from entities.player import Jogador
from managers.collision_manager import GerenciadorColisao
from managers.wave_manager import GerenciadorOndas
from ui.hud import HUD
from assets.loader import carregar_imagem


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
        self.grupo_powerups       = pygame.sprite.Group()

        # Jogador
        self._jogador = Jogador()
        self.grupo_jogador.add(self._jogador)

        # Gerenciadores
        self._colisao = GerenciadorColisao(
            self._jogador,
            self.grupo_inimigos,
            self.grupo_balas_jogador,
            self.grupo_balas_inimigas,
            self.grupo_explosoes,
            self.grupo_powerups,
        )
        self._ondas = GerenciadorOndas(self.grupo_inimigos, self.grupo_balas_inimigas)

        self._hud = HUD()
        self._pausado = False
        self._fonte_pausa = pygame.font.SysFont("arial", 40, bold=True)

        # Fundo com scroll vertical
        fundo = carregar_imagem("assets/images/background.png", LARGURA, ALTURA)
        self._fundo = fundo
        self._fundo_y1 = 0
        self._fundo_y2 = -ALTURA
        self._fundo_velocidade = 1

    # ------------------------------------------------------------------
    def atualizar(self, dt, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                if self._pausado:
                    return CENA_MENU   # segundo ESC: volta ao menu
                else:
                    self._pausado = True  # primeiro ESC: pausa o jogo

        if self._pausado:
            return None

        self._atualizar_fundo()

        # Atualiza entidades
        self._jogador.update(dt, eventos, self.grupo_balas_jogador)
        self.grupo_inimigos.update(dt, self.grupo_balas_inimigas)
        self.grupo_balas_jogador.update()
        self.grupo_balas_inimigas.update()
        self.grupo_explosoes.update()
        self.grupo_powerups.update()

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

    def _atualizar_fundo(self):
        self._fundo_y1 += self._fundo_velocidade
        self._fundo_y2 += self._fundo_velocidade
        if self._fundo_y1 >= ALTURA:
            self._fundo_y1 = -ALTURA
        if self._fundo_y2 >= ALTURA:
            self._fundo_y2 = -ALTURA

    def desenhar(self):
        self.tela.fill(AZUL_CEU)
        self._desenhar_fundo()

        self.grupo_balas_jogador.draw(self.tela)
        self.grupo_balas_inimigas.draw(self.tela)
        self.grupo_inimigos.draw(self.tela)
        self.grupo_jogador.draw(self.tela)
        self.grupo_explosoes.draw(self.tela)
        self.grupo_powerups.draw(self.tela)

        self._hud.desenhar(
            self.tela,
            self.estado["pontuacao"],
            self._jogador.vidas,
            self.estado["onda"],
        )

        if self._pausado:
            self._desenhar_pausa()

    def _desenhar_fundo(self):
        """Desenha fundo com scroll vertical — usa imagem ou fallback de pontos."""
        if self._fundo:
            self.tela.blit(self._fundo, (0, self._fundo_y1))
            self.tela.blit(self._fundo, (0, self._fundo_y2))
        else:
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
