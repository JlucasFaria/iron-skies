"""
Animação de explosão geométrica — expande e desaparece gradualmente.
"""

import pygame
from settings import EXPLOSAO_DURACAO, EXPLOSAO_FRAMES, LARANJA, AMARELO, VERMELHO


class Explosao(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self._frames = self._gerar_frames()
        self._indice = 0
        self._duracao_frame = EXPLOSAO_DURACAO // EXPLOSAO_FRAMES
        self._ultimo_frame = pygame.time.get_ticks()

        self.image = self._frames[0]
        self.rect = self.image.get_rect(center=(x, y))

    # ------------------------------------------------------------------
    def _gerar_frames(self):
        """Gera frames de círculos que expandem e ficam mais transparentes."""
        frames = []
        raio_max = 36
        for i in range(EXPLOSAO_FRAMES):
            progresso = (i + 1) / EXPLOSAO_FRAMES          # 0.0 → 1.0
            raio = int(raio_max * progresso)
            alpha = int(255 * (1 - progresso))

            # Escolhe cor pelo progresso: amarelo → laranja → vermelho
            if progresso < 0.4:
                cor = AMARELO
            elif progresso < 0.7:
                cor = LARANJA
            else:
                cor = VERMELHO

            tamanho = raio_max * 2 + 4
            surf = pygame.Surface((tamanho, tamanho), pygame.SRCALPHA)
            centro = tamanho // 2
            pygame.draw.circle(surf, (*cor, alpha), (centro, centro), raio)
            # Anel interno mais brilhante
            if raio > 8:
                pygame.draw.circle(surf, (*AMARELO, alpha // 2),
                                   (centro, centro), raio // 2)
            frames.append(surf)
        return frames

    # ------------------------------------------------------------------
    def update(self):
        agora = pygame.time.get_ticks()
        if agora - self._ultimo_frame >= self._duracao_frame:
            self._indice += 1
            self._ultimo_frame = agora
            if self._indice >= len(self._frames):
                self.kill()
                return
            centro = self.rect.center
            self.image = self._frames[self._indice]
            self.rect = self.image.get_rect(center=centro)
