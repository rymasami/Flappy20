import pygame
import sys

# Menu inicial exibindo controles
class Menu:
    def __init__(self, window, window_width, window_height, background):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.background = background

        self.title_font = pygame.font.SysFont("arial", 48, bold=True)
        self.text_font = pygame.font.SysFont("arial", 26)
        self.small_font = pygame.font.SysFont("arial", 20)

    def _draw_centered_text(self, font, text, y, color=(20, 20, 20)):
        surf = font.render(text, True, color)
        rect = surf.get_rect(center=(self.window_width // 2, y))
        self.window.blit(surf, rect)

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return

            self.background.draw()

            self._draw_centered_text(
                self.title_font, "Flappy Demo", self.window_height // 4
            )
            self._draw_centered_text(
                self.text_font,
                "Desvie dos canos e alcance 20 pontos!",
                self.window_height // 4 + 60,
            )
            self._draw_centered_text(
                self.text_font,
                "Space - Saltar",
                self.window_height // 2 + 20,
            )
            self._draw_centered_text(
                self.small_font,
                "Pressione Space para começar",
                self.window_height - 100,
                color=(60, 60, 60),
            )
            pygame.display.update()
            clock.tick(60)
