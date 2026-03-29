"""
Tela de game over com pontuação final e botões de reinício e menu.
"""

import pygame
from settings import (
    LARGURA, ALTURA, PRETO, BRANCO, AMARELO, VERMELHO, CINZA_CLARO,
    CENA_JOGO, CENA_MENU,
)
from ui.button import Botao


class GameOverCena:

    def __init__(self, tela, estado):
        self.tela = tela
        self.estado = estado

        self._fonte_titulo    = pygame.font.SysFont("arial", 60, bold=True)
        self._fonte_pontuacao = pygame.font.SysFont("arial", 26)
        self._fonte_onda      = pygame.font.SysFont("arial", 20)

        cx = LARGURA // 2
        self._btn_reiniciar = Botao(cx, 340, 220, 50, "JOGAR NOVAMENTE",
                                    cor=(40, 100, 180), cor_hover=(60, 140, 220),
                                    cor_texto=BRANCO)
        self._btn_menu      = Botao(cx, 410, 220, 50, "MENU PRINCIPAL",
                                    cor=(80, 80, 80), cor_hover=(120, 120, 120),
                                    cor_texto=BRANCO)

        self._proxima_cena = None

    # ------------------------------------------------------------------
    def atualizar(self, dt, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                self._proxima_cena = CENA_MENU

        if self._btn_reiniciar.atualizar(eventos):
            self._proxima_cena = CENA_JOGO
        if self._btn_menu.atualizar(eventos):
            self._proxima_cena = CENA_MENU

        return self._proxima_cena

    def desenhar(self):
        self.tela.fill(PRETO)
        self._desenhar_titulo()
        self._desenhar_pontuacao()
        self._btn_reiniciar.desenhar(self.tela)
        self._btn_menu.desenhar(self.tela)

    # ------------------------------------------------------------------
    def _desenhar_titulo(self):
        # Sombra vermelha
        sombra = self._fonte_titulo.render("GAME OVER", True, (100, 0, 0))
        self.tela.blit(sombra, sombra.get_rect(center=(LARGURA // 2 + 3, 133)))
        titulo = self._fonte_titulo.render("GAME OVER", True, VERMELHO)
        self.tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, 130)))

    def _desenhar_pontuacao(self):
        pontuacao = self.estado.get("pontuacao", 0)
        onda      = self.estado.get("onda", 1)

        surf_pts = self._fonte_pontuacao.render(
            f"Pontuação final: {pontuacao:06d}", True, AMARELO
        )
        self.tela.blit(surf_pts, surf_pts.get_rect(center=(LARGURA // 2, 220)))

        surf_onda = self._fonte_onda.render(
            f"Chegou até a onda {onda}", True, CINZA_CLARO
        )
        self.tela.blit(surf_onda, surf_onda.get_rect(center=(LARGURA // 2, 260)))
