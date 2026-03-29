"""
Componente de botão reutilizável com efeito de hover e clique.
"""

import pygame
from settings import BRANCO, CINZA, CINZA_CLARO, PRETO


class Botao:

    def __init__(self, x, y, largura, altura, texto,
                 cor=CINZA, cor_hover=CINZA_CLARO, cor_texto=PRETO, fonte=None):
        self.rect = pygame.Rect(0, 0, largura, altura)
        self.rect.center = (x, y)
        self.texto = texto
        self.cor = cor
        self.cor_hover = cor_hover
        self.cor_texto = cor_texto
        self.fonte = fonte or pygame.font.SysFont("arial", 22, bold=True)
        self._hover = False
        self._clicado = False

    # ------------------------------------------------------------------
    def atualizar(self, eventos):
        """Atualiza estado de hover e detecta clique. Retorna True se clicado."""
        mouse_pos = pygame.mouse.get_pos()
        self._hover = self.rect.collidepoint(mouse_pos)
        self._clicado = False

        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if self._hover:
                    self._clicado = True

        return self._clicado

    def desenhar(self, tela):
        cor_atual = self.cor_hover if self._hover else self.cor
        pygame.draw.rect(tela, cor_atual, self.rect, border_radius=8)
        pygame.draw.rect(tela, BRANCO, self.rect, width=2, border_radius=8)

        superficie_texto = self.fonte.render(self.texto, True, self.cor_texto)
        tela.blit(superficie_texto, superficie_texto.get_rect(center=self.rect.center))
