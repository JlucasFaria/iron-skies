# IronSkies — Tarefas do Projeto

## Grupo 1: Estrutura Base

- [ ] Criar estrutura de pastas (`scenes/`, `entities/`, `managers/`, `ui/`, `assets/images/`, `assets/sounds/`)
- [ ] Criar `settings.py` com todas as constantes (cores, dimensões, velocidades, FPS)
- [ ] Criar `main.py` com loop principal e gerenciador de cenas
- [ ] Criar arquivos `__init__.py` em todos os pacotes

## Grupo 2: Entidades Principais

- [ ] `entities/bullet.py` — projétil com movimento, classe base simples
- [ ] `entities/player.py` — avião do jogador (movimento 4 direções, tiro, vidas)
- [ ] `entities/enemy.py` — avião inimigo (movimento descendente, tiro ocasional)
- [ ] `entities/explosion.py` — animação de explosão (frames geométricos ou sprite)

## Grupo 3: Gerenciadores

- [ ] `managers/collision_manager.py` — detecção de colisão entre grupos de sprites
- [ ] `managers/wave_manager.py` — spawn de ondas de inimigos com dificuldade crescente

## Grupo 4: Interface (UI)

- [ ] `ui/button.py` — componente de botão reutilizável (hover, clique)
- [ ] `ui/hud.py` — HUD durante o jogo (pontuação, vidas, número da onda)

## Grupo 5: Cenas

- [ ] `scenes/menu.py` — tela de menu principal com controles exibidos na tela
- [ ] `scenes/game.py` — cena principal integrando todas as entidades e gerenciadores
- [ ] `scenes/game_over.py` — tela de game over com pontuação final e botão de reinício

## Grupo 6: Assets e Fallbacks

- [ ] Garantir que o jogo rode sem arquivos de imagem (fallback com formas geométricas)
- [ ] Garantir que o jogo rode sem arquivos de som (sons opcionais, sem travar)
- [ ] Adicionar assets de imagem (sprites de avião, inimigo, fundo) — opcional
- [ ] Adicionar assets de som (tiro, explosão, música de fundo) — opcional

## Grupo 7: Polimento e Equilíbrio

- [ ] Ajustar velocidades, cadência de tiro e quantidade de inimigos por onda
- [ ] Testar fluxo completo: Menu → Jogo → Game Over → Menu
- [ ] Verificar que ESC pausa / volta ao menu corretamente
- [ ] Corrigir bugs encontrados durante os testes

## Grupo 8: Compilação e Entrega

- [ ] Testar execução limpa com `python main.py`
- [ ] Compilar para `.exe` com PyInstaller (`--onefile --windowed --add-data "assets;assets"`)
- [ ] Testar o `.exe` gerado em `dist/` com a pasta `assets/` ao lado
- [ ] Empacotar projeto em arquivo ZIP para entrega (`.exe` + `assets/` + código-fonte)
