import pygame


class Score:
    def __init__(self, window):
        self.window = window
        self.value = 0
        self.font = pygame.font.SysFont("arial", 36, bold=True)

    def add_point(self):
        self.value += 1

    def reset(self):
        self.value = 0

    def draw(self, x=20, y=20):
        text_surf = self.font.render(str(self.value), True, (255, 255, 255))
        shadow_surf = self.font.render(str(self.value), True, (0, 0, 0))
        self.window.blit(shadow_surf, (x + 2, y + 2))
        self.window.blit(text_surf, (x, y))
