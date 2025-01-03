import pygame

from Collections import *
from Settings import *
from Player import *

pygame.init()


class Boss_Tile(Fixed_object):
    def __init__(self, type: int, rect: pygame.rect.Rect):
        super().__init__(
            image=pygame.transform.scale(
                pygame.image.load(Game_Path.boss_tiles_path[type]),
                (SceneSettings.tile_size, SceneSettings.tile_size),
            ),
            rect=rect,
        )


class Shelt(Fixed_object):  # 掩体的类
    def __init__(self, rect: pygame.rect.Rect):
        super().__init__(
            image=pygame.transform.scale(
                pygame.image.load(Game_Path.wall_path),
                (SceneSettings.tile_size, SceneSettings.tile_size),
            ),
            rect=rect,
        )
