"""
Animação de explosão — usa frames PNG reais ou fallback geométrico.
"""

import pygame
from settings import EXPLOSAO_DURACAO, EXPLOSAO_FRAMES, LARANJA, AMARELO, VERMELHO
from assets.loader import carregar_imagem

# Tamanho de exibição da explosão na tela
_TAMANHO = 64


def _carregar_frames_reais():
    """Tenta carregar os 20 frames PNG da explosão."""
    frames = []
    for i in range(20):
        nome = f"assets/images/explosion_{i:02d}.png"
        img = carregar_imagem(nome, _TAMANHO, _TAMANHO)
        if img is None:
            return []  # se qualquer frame falhar, usa fallback completo
        frames.append(img)
    return frames


def _gerar_frames_geometricos():
    """Gera frames de círculos que expandem e ficam mais transparentes."""
    frames = []
    raio_max = _TAMANHO // 2
    for i in range(EXPLOSAO_FRAMES):
        progresso = (i + 1) / EXPLOSAO_FRAMES
        raio = int(raio_max * progresso)
        alpha = int(255 * (1 - progresso))

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
        if raio > 8:
            pygame.draw.circle(surf, (*AMARELO, alpha // 2),
                               (centro, centro), raio // 2)
        frames.append(surf)
    return frames


class Explosao(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        frames_reais = _carregar_frames_reais()
        self._frames = frames_reais if frames_reais else _gerar_frames_geometricos()
        self._indice = 0
        self._duracao_frame = EXPLOSAO_DURACAO // len(self._frames)
        self._ultimo_frame = pygame.time.get_ticks()

        self.image = self._frames[0]
        self.rect = self.image.get_rect(center=(x, y))

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
