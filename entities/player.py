"""
Avião controlado pelo jogador.
"""

import pygame
from settings import (
    LARGURA, ALTURA,
    JOGADOR_VELOCIDADE, JOGADOR_VIDAS, JOGADOR_CADENCIA,
    JOGADOR_COR, JOGADOR_LARGURA, JOGADOR_ALTURA,
    POWERUP_DURACAO, BALA_RICOCHETE_VEL_X,
)
from entities.bullet import BalaJogador, BalaRicochete
from assets.loader import carregar_imagem, carregar_som

# Tipos de power-up de arma disponíveis
POWERUP_NENHUM     = None
POWERUP_TIRO_DUPLO = "tiro_duplo"
POWERUP_RICOCHETE  = "ricochete"


class Jogador(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = self._criar_sprite()
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA // 2
        self.rect.bottom = ALTURA - 20

        self.vidas = JOGADOR_VIDAS
        self._ultimo_tiro = 0
        self.invencivel = False
        self._tempo_invencivel = 0
        self._duracao_invencivel = 1500  # ms

        self._som_tiro = carregar_som("assets/sounds/shoot.ogg")

        # Power-up de arma ativo (mutuamente exclusivos)
        self.powerup_ativo = POWERUP_NENHUM
        self._powerup_fim  = 0

    # ------------------------------------------------------------------
    def _criar_sprite(self):
        """Carrega sprite do jogador ou usa forma geométrica como fallback."""
        imagem = carregar_imagem("assets/images/player.png", JOGADOR_LARGURA, JOGADOR_ALTURA)
        if imagem:
            return imagem
        surf = pygame.Surface((JOGADOR_LARGURA, JOGADOR_ALTURA), pygame.SRCALPHA)
        pygame.draw.polygon(surf, JOGADOR_COR, [
            (JOGADOR_LARGURA // 2, 0),
            (JOGADOR_LARGURA,      JOGADOR_ALTURA),
            (JOGADOR_LARGURA // 2, JOGADOR_ALTURA - 10),
            (0,                    JOGADOR_ALTURA),
        ])
        pygame.draw.circle(surf, (200, 230, 255),
                           (JOGADOR_LARGURA // 2, JOGADOR_ALTURA // 3), 6)
        return surf

    # ------------------------------------------------------------------
    def update(self, dt, eventos, grupo_balas):
        teclas = pygame.key.get_pressed()
        self._mover(teclas)
        self._verificar_tiro(teclas, grupo_balas)
        self._atualizar_invencibilidade(dt)
        self._atualizar_powerup()

    def _mover(self, teclas):
        if teclas[pygame.K_LEFT]  and self.rect.left > 0:
            self.rect.x -= JOGADOR_VELOCIDADE
        if teclas[pygame.K_RIGHT] and self.rect.right < LARGURA:
            self.rect.x += JOGADOR_VELOCIDADE
        if teclas[pygame.K_UP]   and self.rect.top > 0:
            self.rect.y -= JOGADOR_VELOCIDADE
        if teclas[pygame.K_DOWN] and self.rect.bottom < ALTURA:
            self.rect.y += JOGADOR_VELOCIDADE

    def _verificar_tiro(self, teclas, grupo_balas):
        agora = pygame.time.get_ticks()
        if teclas[pygame.K_SPACE]:
            if agora - self._ultimo_tiro >= JOGADOR_CADENCIA:
                self._disparar(grupo_balas)
                self._ultimo_tiro = agora
                if self._som_tiro:
                    self._som_tiro.set_volume(0.3)
                    self._som_tiro.play()

    def _disparar(self, grupo_balas):
        cx, topo = self.rect.centerx, self.rect.top
        if self.powerup_ativo == POWERUP_TIRO_DUPLO:
            grupo_balas.add(BalaJogador(cx - 10, topo))
            grupo_balas.add(BalaJogador(cx + 10, topo))
        elif self.powerup_ativo == POWERUP_RICOCHETE:
            grupo_balas.add(BalaRicochete(cx - 8, topo, -BALA_RICOCHETE_VEL_X))
            grupo_balas.add(BalaRicochete(cx + 8, topo, +BALA_RICOCHETE_VEL_X))
        else:
            grupo_balas.add(BalaJogador(cx, topo))

    def _atualizar_powerup(self):
        """Expira o power-up de arma ao término do tempo."""
        if self.powerup_ativo and pygame.time.get_ticks() >= self._powerup_fim:
            self.powerup_ativo = POWERUP_NENHUM

    def _atualizar_invencibilidade(self, dt):
        if self.invencivel:
            self._tempo_invencivel += dt
            if self._tempo_invencivel >= self._duracao_invencivel:
                self.invencivel = False
                self._tempo_invencivel = 0
                self.image.set_alpha(255)
            else:
                alpha = 80 if (self._tempo_invencivel // 150) % 2 == 0 else 255
                self.image.set_alpha(alpha)

    # ------------------------------------------------------------------
    def ativar_tiro_duplo(self):
        """Ativa tiro duplo, cancelando qualquer outro power-up de arma."""
        self.powerup_ativo = POWERUP_TIRO_DUPLO
        self._powerup_fim  = pygame.time.get_ticks() + POWERUP_DURACAO

    def ativar_ricochete(self):
        """Ativa ricochete, cancelando qualquer outro power-up de arma."""
        self.powerup_ativo = POWERUP_RICOCHETE
        self._powerup_fim  = pygame.time.get_ticks() + POWERUP_DURACAO

    def ganhar_vida(self, max_vidas=JOGADOR_VIDAS + 2):
        """Adiciona uma vida até o limite."""
        if self.vidas < max_vidas:
            self.vidas += 1

    def levar_dano(self):
        """Reduz uma vida e ativa invencibilidade temporária."""
        if self.invencivel:
            return
        self.vidas -= 1
        self.invencivel = True
        self._tempo_invencivel = 0

    def esta_vivo(self):
        return self.vidas > 0
