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
├── main.py               # Ponto de entrada, gerenciador de cenas
├── settings.py           # Todas as constantes do jogo
├── scenes/
│   ├── __init__.py
│   ├── menu.py           # Tela de menu principal
│   ├── game.py           # Cena principal do jogo
│   └── game_over.py      # Tela de game over
├── entities/
│   ├── __init__.py
│   ├── player.py         # Avião do jogador
│   ├── enemy.py          # Aviões inimigos
│   ├── bullet.py         # Projéteis
│   └── explosion.py      # Animação de explosão
├── managers/
│   ├── __init__.py
│   ├── collision_manager.py  # Detecção de colisões
│   └── wave_manager.py       # Gerenciamento de ondas de inimigos
├── ui/
│   ├── __init__.py
│   ├── hud.py            # Interface durante o jogo (pontos, vidas, onda)
│   └── button.py         # Componente de botão reutilizável
└── assets/
    ├── images/           # Sprites (opcional - usa formas geométricas se ausente)
    └── sounds/           # Sons (opcional - jogo funciona sem eles)
```

## Especificações Técnicas

- **Resolução:** 800x600
- **FPS:** 60
- **Python:** 3.10+
- **Pygame:** 2.x
- **Linguagem dos comentários:** Português

## Controles

| Tecla | Ação |
|-------|------|
| ← → ↑ ↓ | Mover avião |
| Espaço | Atirar |
| ESC | Pausar / Voltar ao menu |

## Compilação para .exe

```bash
pip install pyinstaller
cd iron_skies
pyinstaller --onefile --windowed --add-data "assets;assets" main.py
```

O executável gerado estará em `dist/main.exe`.
Copiar a pasta `assets/` junto ao `.exe` mantendo a hierarquia de pastas.

## Como Rodar em Desenvolvimento

```bash
pip install pygame
cd iron_skies
python main.py
```

## Fluxo de Cenas

```
main.py → Menu → Game → Game Over → Menu
```

## Notas Importantes

- O jogo funciona **sem** arquivos de assets — usa formas geométricas coloridas como fallback
- Sons são completamente opcionais e não travam o jogo se ausentes
- Todas as constantes (cores, velocidades, dimensões) estão centralizadas em `settings.py`

## Fluxo de Trabalho com Git

- Para cada grupo do `TASKS.md`, criar uma branch separada antes de começar (ex: `grupo-1-estrutura-base`)
- Para cada task concluída dentro do grupo, fazer um commit individual
- **Nunca incluir co-autor nos commits** (sem linha `Co-Authored-By`)
- **Push, merge no GitHub, pull e delete da branch são responsabilidade do usuário**
- Antes de iniciar um novo grupo, verificar se o fluxo do grupo anterior foi concluído (main atualizado, branch deletada)
