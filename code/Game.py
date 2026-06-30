import pygame
import sys

from Menu import Menu
from Level import Level
from Background import Background
from Utils import resource_path  # centralizado em Utils.py — use em todo asset

class Game:

    WINDOW_WIDTH = 480
    WINDOW_HEIGHT = 640

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(
            (Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT)
        )
        pygame.display.set_caption("Flappy Demo")
        self.player_image_path = resource_path("asset/player.png")

    def run(self):
        while True:
            # Menu é recriado a cada loop para garantir estado limpo no restart.
            # Antes estava fora do while, o que causaria problemas se o menu
            # tivesse música ou estado interno (ex: opção selecionada).
            menu_background = Background(
                self.window, Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT
            )
            menu = Menu(self.window, Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT, menu_background)
            menu.run()

            level = Level(
                self.window,
                Game.WINDOW_WIDTH,
                Game.WINDOW_HEIGHT,
                self.player_image_path,
            )
            result = level.run()

            if result == "quit":
                pygame.quit()
                sys.exit()
            # se for "restart", o while True recria o menu e começa nova partida
