# Constantes globais do jogo IronSkies

# --- Tela ---
LARGURA = 800
ALTURA = 600
FPS = 60
TITULO = "IronSkies"

# --- Cores ---
PRETO       = (0,   0,   0)
BRANCO      = (255, 255, 255)
CINZA       = (100, 100, 100)
CINZA_CLARO = (180, 180, 180)
AZUL_CEU    = (30,  60,  120)
VERMELHO    = (220, 40,  40)
VERDE       = (40,  200, 80)
AMARELO     = (255, 220, 0)
LARANJA     = (255, 140, 0)

# --- Jogador ---
JOGADOR_VELOCIDADE    = 5
JOGADOR_VIDAS         = 3
JOGADOR_CADENCIA      = 300   # milissegundos entre tiros
JOGADOR_COR           = (80,  160, 255)
JOGADOR_LARGURA       = 40
JOGADOR_ALTURA        = 50

# --- Inimigo ---
INIMIGO_VELOCIDADE_BASE = 2
INIMIGO_COR             = (220, 60,  60)
INIMIGO_LARGURA         = 36
INIMIGO_ALTURA          = 44
INIMIGO_CADENCIA_MIN    = 1500  # ms
INIMIGO_CADENCIA_MAX    = 3500  # ms

# --- Projéteis ---
BALA_JOGADOR_VELOCIDADE = 10
BALA_JOGADOR_COR        = (180, 220, 255)
BALA_JOGADOR_LARGURA    = 6
BALA_JOGADOR_ALTURA     = 14

BALA_INIMIGO_VELOCIDADE = 6
BALA_INIMIGO_COR        = (255, 100, 80)
BALA_INIMIGO_LARGURA    = 6
BALA_INIMIGO_ALTURA     = 14

# --- Explosão ---
EXPLOSAO_DURACAO     = 400   # ms
EXPLOSAO_FRAMES      = 6

# --- Pontuação ---
PONTOS_INIMIGO = 100

# --- Ondas ---
INIMIGOS_POR_ONDA_BASE   = 5
INIMIGOS_POR_ONDA_EXTRA  = 2   # acrescenta por onda
INTERVALO_SPAWN          = 1200 # ms entre spawns dentro da onda

# --- Cenas ---
CENA_MENU      = "menu"
CENA_JOGO      = "jogo"
CENA_GAME_OVER = "game_over"
