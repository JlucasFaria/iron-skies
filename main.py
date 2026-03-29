"""
IronSkies — Ponto de entrada e gerenciador de cenas.
"""

import pygame
import sys
from settings import LARGURA, ALTURA, FPS, TITULO, CENA_MENU, CENA_JOGO, CENA_GAME_OVER


def main():
    pygame.init()
    # Inicializa o mixer de som separadamente — jogo funciona sem ele
    try:
        pygame.mixer.init()
    except pygame.error:
        pass

    pygame.display.set_caption(TITULO)
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    relogio = pygame.time.Clock()

    # Importações tardias para evitar dependências circulares
    from scenes.menu import MenuCena
    from scenes.game import GameCena
    from scenes.game_over import GameOverCena

    # Estado compartilhado entre cenas
    estado = {
        "pontuacao": 0,
        "onda": 1,
    }

    cena_atual = CENA_MENU
    cenas = {
        CENA_MENU:      MenuCena(tela, estado),
        CENA_JOGO:      GameCena(tela, estado),
        CENA_GAME_OVER: GameOverCena(tela, estado),
    }

    while True:
        dt = relogio.tick(FPS)  # milissegundos desde o último frame

        # Coleta eventos e repassa para a cena ativa
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        cena = cenas[cena_atual]
        proxima_cena = cena.atualizar(dt, eventos)
        cena.desenhar()
        pygame.display.flip()

        # Troca de cena
        if proxima_cena and proxima_cena != cena_atual:
            # Reinicia a cena de destino antes de entrar nela
            if proxima_cena == CENA_JOGO:
                estado["pontuacao"] = 0
                estado["onda"] = 1
                cenas[CENA_JOGO] = GameCena(tela, estado)
            elif proxima_cena == CENA_MENU:
                cenas[CENA_MENU] = MenuCena(tela, estado)
            elif proxima_cena == CENA_GAME_OVER:
                cenas[CENA_GAME_OVER] = GameOverCena(tela, estado)
            cena_atual = proxima_cena


if __name__ == "__main__":
    main()
