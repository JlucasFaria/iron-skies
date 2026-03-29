# IronSkies

Jogo 2D shoot 'em up top-down desenvolvido em Python com Pygame para a disciplina **Linguagem de Programação Aplicada** da UNINTER.

## Demonstração

Pilote seu avião de combate, destrua ondas de inimigos, colete power-ups e sobreviva o máximo possível!

## Controles

| Tecla | Ação |
|-------|------|
| ← → ↑ ↓ | Mover avião |
| Espaço | Atirar |
| ESC | Pausar (segundo ESC volta ao menu) |

## Power-ups

| Ícone | Power-up | Efeito | Duração |
|-------|----------|--------|---------|
| 🟢 `2x` | Tiro Duplo | Dispara dois projéteis lado a lado | 8 segundos |
| 🟠 `~` | Ricochete | Dispara balas que ricocheteiam nas bordas | 8 segundos |
| 🔴 `♥` | Vida | Recupera uma vida (máx. 5) | Permanente |

> Tiro Duplo e Ricochete são **mutuamente exclusivos** — coletar um cancela o outro.

## Como Executar

**Requisitos:**
- Python 3.10+
- Pygame 2.x

**Instalação e execução:**
```bash
pip install pygame
python main.py
```

> No Windows use `py` no lugar de `python` se necessário:
> ```bash
> py -m pip install pygame
> py main.py
> ```

## Compilar para .exe

```bash
build.bat
```

O executável será gerado em `dist/IronSkies.exe`. Copie a pasta `assets/` para junto do `.exe` antes de distribuir.

## Estrutura do Projeto

```
iron_skies/
├── main.py                      # Ponto de entrada e gerenciador de cenas
├── settings.py                  # Todas as constantes do jogo
├── build.bat                    # Script de compilação para Windows
├── scenes/
│   ├── menu.py                  # Tela de menu principal
│   ├── game.py                  # Cena principal do jogo
│   └── game_over.py             # Tela de game over
├── entities/
│   ├── player.py                # Avião do jogador
│   ├── enemy.py                 # Aviões inimigos com zigzag
│   ├── bullet.py                # Projéteis (normal, ricochete, inimigo)
│   ├── explosion.py             # Animação de explosão
│   └── powerup.py               # Power-ups (tiro duplo, ricochete, vida)
├── managers/
│   ├── collision_manager.py     # Detecção de colisões e drops
│   └── wave_manager.py          # Gerenciamento de ondas com dificuldade crescente
├── ui/
│   ├── hud.py                   # Interface durante o jogo
│   └── button.py                # Componente de botão reutilizável
└── assets/
    ├── images/                  # Sprites (jogo funciona sem eles via fallback)
    ├── sounds/                  # Sons (jogo funciona sem eles)
    ├── fonts/                   # Fontes
    └── loader.py                # Carregamento seguro de assets
```

## Funcionalidades

- Ondas de inimigos com dificuldade crescente
- Inimigos com movimento em zigzag
- Sistema de power-ups com drops aleatórios
- Animações de explosão com 20 frames
- Fundo com scroll vertical contínuo
- Sistema de pausa
- Fallback geométrico completo (funciona sem assets)
- Compatível com PyInstaller

## Assets

Assets visuais e sonoros do pack **Kenney Space Shooter Remastered** (CC0 — domínio público).
