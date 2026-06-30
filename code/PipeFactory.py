from Pipe import Pipe


class PipeFactory:
    def __init__(self, window, window_height):
        self.window = window
        self.window_height = window_height

    def create_pipe(self, x):
        return Pipe(self.window, x, self.window_height)
