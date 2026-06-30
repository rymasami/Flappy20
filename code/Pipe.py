import pygame
import random


class Pipe:
    WIDTH = 70
    SPEED = 4
    MIN_GAP_Y = 150
    MAX_GAP_Y_MARGIN = 150  

    def __init__(self, window, x, window_height, gap_size=160, color=(40, 160, 70)):
        self.window = window
        self.x = x
        self.window_height = window_height
        self.gap_size = gap_size
        self.color = color
        max_gap_y = self.window_height - Pipe.MAX_GAP_Y_MARGIN
        self.gap_y = random.randint(Pipe.MIN_GAP_Y, max_gap_y)
        self.scored = False
        self._build_rects()

    def _build_rects(self):
        top_height = self.gap_y - self.gap_size // 2
        bottom_y = self.gap_y + self.gap_size // 2

        self.top_rect = pygame.Rect(self.x, 0, Pipe.WIDTH, top_height)
        self.bottom_rect = pygame.Rect(
            self.x, bottom_y, Pipe.WIDTH, self.window_height - bottom_y
        )

    # Movimento do cano para esquerda
    def update(self):
        self.x -= Pipe.SPEED
        self._build_rects()

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.top_rect)
        pygame.draw.rect(self.window, self.color, self.bottom_rect)
        border_color = (20, 110, 45)
        pygame.draw.rect(self.window, border_color, self.top_rect, width=4)
        pygame.draw.rect(self.window, border_color, self.bottom_rect, width=4)

    def is_off_screen(self):
        return self.x + Pipe.WIDTH < 0

    def collides_with(self, player_rect):
        return self.top_rect.colliderect(player_rect) or self.bottom_rect.colliderect(player_rect)

    def check_score(self, player_x):
        # Contagem pontuação
        if not self.scored and (self.x + Pipe.WIDTH) < player_x:
            self.scored = True
            return True
        return False
