"""Define game window that contains windows setting"""
import time
import os
import pygame

# pylint: disable=E1101
#### Pygame Init ####
pygame.init()
pygame.mixer.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"
os.environ["SDL_VIDEO_WINDOW_POS"] = "1000,500"


class Reslution:
    """Define the game reslution"""

    def __init__(self, size, grid_div):
        """init a new reslution object"""
        self.screen_width = None
        self.screen_height = None
        self.width_ratio = None
        self.height_ratio = None
        self.x_ceil = None
        self.y_ceil = None

        self.set_reslution(size)
        self.set_ratio()
        self.set_grid(grid_div)

    def set_reslution(self, size):
        """Set the game window size"""
        screen_info = pygame.display.Info()
        moniter_width = screen_info.current_w
        moniter_height = screen_info.current_h

        if size is None:
            self.screen_width = moniter_width
            self.screen_height = moniter_height
        else:
            self.screen_width = size[0]
            self.screen_height = size[1]

    def set_ratio(self):
        """Set the window ration according to 1920x1080 and the current screen size"""
        self.width_ratio = self.screen_width / 1920
        self.height_ratio = self.screen_height / 1080

    def set_grid(self, grid_div):
        """Set the game grid"""
        self.x_ceil = grid_div * 9
        self.y_ceil = grid_div * 16


class FrameRate:
    """Define the game main clock"""

    def __init__(self, fps):
        """Init a new clock object"""
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.delta_time = None
        self.previous_time = time.time()

    def set_delta(self):
        """
        Sets the game deltatime

        this function will be called every game loop to calc the deltatime value
        """
        self.delta_time = time.time() - self.previous_time
        self.previous_time = time.time()


class Window(Reslution, FrameRate):
    """Game window object that contains all the window setting"""

    def __init__(self):
        """Init a new window object"""
        Reslution.__init__(self, None, 2)
        FrameRate.__init__(self, 60)

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Engine")

        icon_path = (
            "/".join(os.path.abspath(__file__).split("\\")[:-1]) + "/Sprites/icon.png"
        )
        icon = pygame.image.load(icon_path).convert_alpha()
        pygame.display.set_icon(icon)


win_obj = Window()
