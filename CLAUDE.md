# IronSkies - Trabalho de Linguagem de Programação Aplicada (UNINTER)

## Contexto do Projeto

Jogo 2D desenvolvido em Python com Pygame para a disciplina **Linguagem de Programação Aplicada** da UNINTER.
Estilo shoot 'em up top-down (visão de cima) com aviões caça.

## Requisitos da Disciplina

- Jogo 2D jogável (não pode ser via console/cmd)
- Deve ter menu principal com controles exibidos na tela
- Assets (imagens/sons) podem ser adquiridos da internet
- O código deve ser original (não pode ser cópia de outro projeto)
- Entrega: arquivo ZIP com projeto compilado para Windows (.exe + assets)
- Compilação: usar PyInstaller ou método do PyCharm/VSCode

## Estrutura de Pastas

```
iron_skies/
├── main.py                      # Ponto de entrada e gerenciador de cenas
├── settings.py                  # Todas as constantes do jogo
├── build.bat                    # Script de compilação para Windows (.exe)
├── README.md                    # Documentação pública do projeto
├── scenes/
│   ├── __init__.py
│   ├── menu.py                  # Tela de menu principal com controles
│   ├── game.py                  # Cena principal do jogo
│   └── game_over.py             # Tela de game over
├── entities/
│   ├── __init__.py
│   ├── player.py                # Avião do jogador (movimento, tiro, power-ups)
│   ├── enemy.py                 # Aviões inimigos (zigzag + tiro aleatório)
│   ├── bullet.py                # Projéteis: BalaJogador, BalaInimigo, BalaRicochete
│   ├── explosion.py             # Animação de explosão (20 frames PNG + fallback)
│   └── powerup.py               # Power-ups: TiroDuplo, Ricochete, Vida
├── managers/
│   ├── __init__.py
│   ├── collision_manager.py     # Colisões + drops de power-up
│   └── wave_manager.py          # Ondas de inimigos com dificuldade crescente
├── ui/
│   ├── __init__.py
│   ├── hud.py                   # HUD: pontos, vidas, onda, power-up ativo
│   └── button.py                # Botão reutilizável com hover/clique
└── assets/
    ├── loader.py                # Carregamento seguro (compatível com PyInstaller)
    ├── images/                  # Sprites PNG (fallback geométrico se ausente)
    │   ├── player.png
    │   ├── enemy.png
    │   ├── background.png
    │   ├── bullet_player.png
    │   ├── bullet_enemy.png
    │   └── explosion_00..19.png
    ├── sounds/                  # Sons OGG (jogo funciona sem eles)
    │   ├── shoot.ogg
    │   ├── explosion.ogg
    │   └── game_over.ogg
    └── fonts/
        └── kenvector_future.ttf
```

## Especificações Técnicas

- **Resolução:** 800x600
- **FPS:** 60
- **Python:** 3.10+
- **Pygame:** 2.x
- **Linguagem dos comentários:** Português
- **Assets:** Kenney Space Shooter Remastered (CC0)

## Controles

| Tecla | Ação |
|-------|------|
| ← → ↑ ↓ | Mover avião |
| Espaço | Atirar |
| ESC | Pausar (segundo ESC volta ao menu) |

## Power-ups

| Tipo | Cor | Efeito | Duração |
|------|-----|--------|---------|
| Tiro Duplo | Verde-água | Dois projéteis lado a lado | 8s |
| Ricochete | Laranja | Balas ricocheteiam nas bordas (3x) | 8s |
| Vida | Rosa | +1 vida (máx. 5) | Permanente |

- Tiro Duplo e Ricochete são **mutuamente exclusivos** — coletar um cancela o outro
- Chance de drop: 25% arma (aleatório entre os dois) + 10% vida por inimigo morto

## Sistema de Power-ups no Código

O jogador possui `powerup_ativo` (string ou None): `"tiro_duplo"`, `"ricochete"` ou `None`.
Métodos: `ativar_tiro_duplo()`, `ativar_ricochete()`, `ganhar_vida()`.
O HUD recebe `powerup_ativo` e exibe o indicador correto.

## Compilação para .exe

```bash
build.bat
```

Ou manualmente:
```bash
py -m pip install pyinstaller
py -m PyInstaller --onefile --windowed --add-data "assets;assets" --name "IronSkies" main.py
```

O executável gerado estará em `dist/IronSkies.exe`.
Copiar a pasta `assets/` junto ao `.exe` mantendo a hierarquia de pastas.

## Como Rodar em Desenvolvimento

```bash
py -m pip install pygame
py main.py
```

## Fluxo de Cenas

```
main.py → Menu → Game → Game Over → Menu
```

## Notas Importantes

- O jogo funciona **sem** arquivos de assets — usa formas geométricas coloridas como fallback
- Sons são completamente opcionais e não travam o jogo se ausentes
- Todas as constantes (cores, velocidades, dimensões) estão centralizadas em `settings.py`
- `assets/loader.py` resolve caminhos tanto em desenvolvimento quanto no `.exe` compilado

## Fluxo de Trabalho com Git

- Para cada grupo do `TASKS.md`, criar uma branch separada antes de começar (ex: `grupo-1-estrutura-base`)
- Para cada task concluída dentro do grupo, fazer um commit individual
- **Nunca incluir co-autor nos commits** (sem linha `Co-Authored-By`)
- **Push, merge no GitHub, pull e delete da branch são responsabilidade do usuário**
- Antes de iniciar um novo grupo, verificar se o fluxo do grupo anterior foi concluído (main atualizado, branch deletada)
- `CLAUDE.md` e `TASKS.md` estão no `.gitignore` e nunca serão commitados
