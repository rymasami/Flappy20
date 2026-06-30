import pygame

# Constantes da física do jogo
class Player:
    GRAVITY = 0.45 
    JUMP_STRENGTH = -8.5 
    MAX_FALL_SPEED = 12 

    def __init__(self, window, x, y, image_path):
        self.window = window
        self.x = x
        self.y = y
        self.velocity_y = 0
        self.rotation = 0
        self.original_surf = pygame.image.load(image_path).convert_alpha()
        self.surf = self.original_surf
        self.rect = self.surf.get_rect(center=(self.x, self.y))

    # Função de pular
    def jump(self):
        self.velocity_y = Player.JUMP_STRENGTH

    def update(self):
        self.velocity_y += Player.GRAVITY
        if self.velocity_y > Player.MAX_FALL_SPEED:
            self.velocity_y = Player.MAX_FALL_SPEED
        self.y += self.velocity_y
        self.rect.centery = self.y
        self.rotation = max(-25, min(90, -self.velocity_y * 4))
        self.surf = pygame.transform.rotate(self.original_surf, self.rotation)
        self.rect = self.surf.get_rect(center=self.rect.center)

    def draw(self):
        self.window.blit(self.surf, self.rect)

    def get_mask_rect(self):
        shrink = 6
        return self.rect.inflate(-shrink, -shrink)
