"""Contains unit-test for window file"""
###### Python Packages ######
import time
import pygame

###### My Packages ######
from pyengine.window import FrameRate, Resolution


def test_set_resolution():
    """Test set_resolution method in Resolution class"""
    screen_info = pygame.display.Info()
    monitor_width = screen_info.current_w
    monitor_height = screen_info.current_h

    res_obj = Resolution([500, 500], 2)
    full_res_obj = Resolution([0, 0], 2)

    assert res_obj.screen_width == 500
    assert res_obj.screen_height == 500

    assert full_res_obj.screen_width == monitor_width
    assert full_res_obj.screen_height == monitor_height


def test_set_grid():
    """Test set_grid method in Resolution class"""
    res_obj = Resolution([0, 0], 4)

    assert res_obj.x_ceil == 4 * 9
    assert res_obj.y_ceil == 4 * 16


def test_set_delta():
    """Test set_delta method in FrameRate class"""
    frame_obj = FrameRate(60)
    frame_obj.set_delta()

    previous_time = time.time()

    assert frame_obj.previous_time == previous_time
    assert frame_obj.delta_time == (time.time() - previous_time)
