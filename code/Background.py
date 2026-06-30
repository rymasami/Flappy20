import pygame


class Background:
    GROUND_HEIGHT = 70
    SKY_TOP_COLOR = (78, 192, 230)
    SKY_BOTTOM_COLOR = (180, 230, 240)
    GROUND_COLOR = (210, 180, 110)

    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.ground_y = window_height - Background.GROUND_HEIGHT

        self.sky_surf = self._build_sky_gradient()

    def _build_sky_gradient(self):
        surf = pygame.Surface((self.window_width, self.ground_y))
        top = Background.SKY_TOP_COLOR
        bottom = Background.SKY_BOTTOM_COLOR
        height = self.ground_y

        for y in range(height):
            ratio = y / height
            r = top[0] + (bottom[0] - top[0]) * ratio
            g = top[1] + (bottom[1] - top[1]) * ratio
            b = top[2] + (bottom[2] - top[2]) * ratio
            pygame.draw.line(surf, (r, g, b), (0, y), (self.window_width, y))

        return surf

    def get_ground_rect(self):
        return pygame.Rect(0, self.ground_y, self.window_width, Background.GROUND_HEIGHT)

    def draw(self):
        self.window.blit(self.sky_surf, (0, 0))
        pygame.draw.rect(
            self.window, Background.GROUND_COLOR, self.get_ground_rect()
        )
