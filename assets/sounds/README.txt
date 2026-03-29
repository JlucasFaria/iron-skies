Sons opcionais do jogo IronSkies.
Se ausentes, o jogo roda normalmente sem áudio.

Arquivos esperados (WAV ou OGG):
  shoot.wav      — som do tiro do jogador
  explosion.wav  — som de explosão
  music.ogg      — música de fundo (loop)

Use assets/loader.py para carregar:
  carregar_som(caminho)      → pygame.mixer.Sound ou None
  carregar_musica(caminho)   → toca em loop ou não faz nada
