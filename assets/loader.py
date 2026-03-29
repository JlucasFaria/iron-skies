"""
Utilitário para carregamento seguro de imagens e sons.
Retorna None silenciosamente se o arquivo não existir ou falhar ao carregar.
"""

import os
import pygame


def carregar_imagem(caminho, largura=None, altura=None):
    """
    Tenta carregar uma imagem. Retorna Surface redimensionada ou None se falhar.
    """
    if not os.path.isfile(caminho):
        return None
    try:
        imagem = pygame.image.load(caminho).convert_alpha()
        if largura and altura:
            imagem = pygame.transform.scale(imagem, (largura, altura))
        return imagem
    except pygame.error:
        return None


def carregar_som(caminho):
    """
    Tenta carregar um som. Retorna Sound ou None se falhar / mixer inativo.
    """
    if not pygame.mixer.get_init():
        return None
    if not os.path.isfile(caminho):
        return None
    try:
        return pygame.mixer.Sound(caminho)
    except pygame.error:
        return None


def carregar_musica(caminho):
    """
    Tenta carregar e tocar música de fundo em loop.
    Não faz nada se o arquivo não existir ou o mixer estiver inativo.
    """
    if not pygame.mixer.get_init():
        return
    if not os.path.isfile(caminho):
        return
    try:
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # -1 = loop infinito
    except pygame.error:
        pass
