"""
Utilitário para carregamento seguro de imagens e sons.
Retorna None silenciosamente se o arquivo não existir ou falhar ao carregar.
Compatível com PyInstaller (resolve caminho via sys._MEIPASS).
"""

import os
import sys
import pygame


def _base():
    """Retorna o diretório base correto em desenvolvimento e no .exe compilado."""
    if getattr(sys, "frozen", False):
        return sys._MEIPASS
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def caminho_asset(relativo):
    """Monta o caminho absoluto de um asset a partir da raiz do projeto."""
    return os.path.join(_base(), relativo)


def carregar_imagem(relativo, largura=None, altura=None):
    """
    Tenta carregar uma imagem pelo caminho relativo à raiz do projeto.
    Retorna Surface redimensionada ou None se falhar.
    """
    caminho = caminho_asset(relativo)
    if not os.path.isfile(caminho):
        return None
    try:
        imagem = pygame.image.load(caminho).convert_alpha()
        if largura and altura:
            imagem = pygame.transform.scale(imagem, (largura, altura))
        return imagem
    except pygame.error:
        return None


def carregar_som(relativo):
    """
    Tenta carregar um som pelo caminho relativo à raiz do projeto.
    Retorna Sound ou None se falhar / mixer inativo.
    """
    if not pygame.mixer.get_init():
        return None
    caminho = caminho_asset(relativo)
    if not os.path.isfile(caminho):
        return None
    try:
        return pygame.mixer.Sound(caminho)
    except pygame.error:
        return None


def carregar_musica(relativo):
    """
    Tenta carregar e tocar música de fundo em loop.
    Não faz nada se o arquivo não existir ou o mixer estiver inativo.
    """
    if not pygame.mixer.get_init():
        return
    caminho = caminho_asset(relativo)
    if not os.path.isfile(caminho):
        return
    try:
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
    except pygame.error:
        pass
