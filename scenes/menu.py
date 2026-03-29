"""
Cena do menu principal com controles exibidos na tela.
"""

import pygame
from settings import (
    LARGURA, ALTURA, AZUL_CEU, BRANCO, AMARELO, CINZA_CLARO,
    CENA_JOGO, JOGADOR_COR,
)
from ui.button import Botao


class MenuCena:

    def __init__(self, tela, estado):
        self.tela = tela
        self.estado = estado

        self._fonte_titulo = pygame.font.SysFont("arial", 56, bold=True)
        self._fonte_subtitulo = pygame.font.SysFont("arial", 18)
        self._fonte_controles = pygame.font.SysFont("arial", 17)

        cx = LARGURA // 2
        self._btn_jogar = Botao(cx, 300, 200, 50, "JOGAR",
                                cor=(40, 100, 180), cor_hover=(60, 140, 220),
                                cor_texto=BRANCO)
        self._btn_sair  = Botao(cx, 370, 200, 50, "SAIR",
                                cor=(120, 30, 30), cor_hover=(180, 50, 50),
                                cor_texto=BRANCO)

        self._proxima_cena = None

    # ------------------------------------------------------------------
    def atualizar(self, dt, eventos):
        if self._btn_jogar.atualizar(eventos):
            self._proxima_cena = CENA_JOGO
        if self._btn_sair.atualizar(eventos):
            pygame.quit()
            import sys; sys.exit()
        return self._proxima_cena

    def desenhar(self):
        self.tela.fill(AZUL_CEU)
        self._desenhar_estrelas()
        self._desenhar_titulo()
        self._desenhar_controles()
        self._btn_jogar.desenhar(self.tela)
        self._btn_sair.desenhar(self.tela)

    # ------------------------------------------------------------------
    def _desenhar_estrelas(self):
        """Fundo decorativo com estrelas estáticas."""
        import random
        rng = random.Random(42)  # semente fixa para estrelas sempre iguais
        for _ in range(60):
            x = rng.randint(0, LARGURA)
            y = rng.randint(0, ALTURA)
            r = rng.randint(1, 2)
            pygame.draw.circle(self.tela, BRANCO, (x, y), r)

    def _desenhar_titulo(self):
        # Sombra
        sombra = self._fonte_titulo.render("IRON SKIES", True, (0, 0, 0))
        self.tela.blit(sombra, sombra.get_rect(center=(LARGURA // 2 + 3, 103)))
        # Título
        titulo = self._fonte_titulo.render("IRON SKIES", True, AMARELO)
        self.tela.blit(titulo, titulo.get_rect(center=(LARGURA // 2, 100)))

        sub = self._fonte_subtitulo.render("Shoot 'em up", True, CINZA_CLARO)
        self.tela.blit(sub, sub.get_rect(center=(LARGURA // 2, 155)))

    def _desenhar_controles(self):
        controles = [
            ("CONTROLES", AMARELO),
            ("← → ↑ ↓   Mover avião", BRANCO),
            ("Espaço       Atirar",    BRANCO),
            ("ESC          Pausar / Menu", BRANCO),
        ]
        y = 450
        for texto, cor in controles:
            surf = self._fonte_controles.render(texto, True, cor)
            self.tela.blit(surf, surf.get_rect(center=(LARGURA // 2, y)))
            y += 26
