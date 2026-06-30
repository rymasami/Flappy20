import pygame

from Player import Player
from PipeFactory import PipeFactory
from Background import Background
from Score import Score


class Level:
    WIN_SCORE = 20          # pontuação necessária para vencer
    PIPE_SPAWN_INTERVAL = 90  # de quantos em quantos frames nasce um cano novo

    def __init__(self, window, window_width, window_height, player_image_path):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height

        self.background = Background(window, window_width, window_height)
        self.pipe_factory = PipeFactory(window, window_height)
        self.score = Score(window)

        self.player = Player(
            window,
            x=window_width // 4,
            y=window_height // 2,
            image_path=player_image_path,
        )

        self.pipes = []
        self.frame_count = 0

        self.game_over = False
        self.victory = False

    def _spawn_pipe_if_needed(self):
        self.frame_count += 1
        if self.frame_count % Level.PIPE_SPAWN_INTERVAL == 0:
            new_pipe = self.pipe_factory.create_pipe(x=self.window_width + 20)
            self.pipes.append(new_pipe)

    def _update_pipes(self):
        for pipe in self.pipes:
            pipe.update()

            if pipe.check_score(self.player.rect.centerx):
                self.score.add_point()
                if self.score.value >= Level.WIN_SCORE:
                    self.victory = True

        # Remove canos que já saíram da tela, por performance
        self.pipes = [p for p in self.pipes if not p.is_off_screen()]

    def _check_collisions(self):
        player_rect = self.player.get_mask_rect()

        # Colisão com o chão ou com o teto = derrota
        if player_rect.bottom >= self.background.ground_y or player_rect.top <= 0:
            self.game_over = True
            return

        # Colisão com qualquer cano = derrota
        for pipe in self.pipes:
            if pipe.collides_with(player_rect):
                self.game_over = True
                return

    def _draw_end_message(self, text, color):
        font = pygame.font.SysFont("arial", 44, bold=True)
        surf = font.render(text, True, color)
        rect = surf.get_rect(
            center=(self.window_width // 2, self.window_height // 2 - 40)
        )
        shadow = font.render(text, True, (0, 0, 0))
        self.window.blit(shadow, (rect.x + 2, rect.y + 2))
        self.window.blit(surf, rect)

        hint_font = pygame.font.SysFont("arial", 22)
        hint = hint_font.render(
            "Space - Jogar novamente   |   ESC - Sair", True, (30, 30, 30)
        )
        hint_rect = hint.get_rect(
            center=(self.window_width // 2, self.window_height // 2 + 30)
        )
        self.window.blit(hint, hint_rect)

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if not self.game_over and not self.victory:
                        if event.key == pygame.K_SPACE:
                            self.player.jump()
                    else:
                        # Level só retorna o resultado — quem age é o Game.py
                        # Isso mantém a separação de responsabilidades correta
                        if event.key == pygame.K_SPACE:
                            return "restart"
                        if event.key == pygame.K_ESCAPE:
                            return "quit"

            if not self.game_over and not self.victory:
                self.player.update()
                self._spawn_pipe_if_needed()
                self._update_pipes()
                self._check_collisions()

            self.background.draw()
            for pipe in self.pipes:
                pipe.draw()
            self.player.draw()
            self.score.draw()

            if self.game_over:
                self._draw_end_message("Você perdeu!", (200, 30, 30))
            elif self.victory:
                self._draw_end_message("Você venceu!", (20, 140, 40))

            pygame.display.update()
            clock.tick(60)
