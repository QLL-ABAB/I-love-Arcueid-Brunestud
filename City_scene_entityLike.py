import pygame


from Collections import *
from Settings import *
from Player import *

pygame.init()


class City_Tile(EntityLike):
    def __init__(self, type: int, rect: pygame.rect.Rect):
        super().__init__(
            image=pygame.transform.scale(
                pygame.image.load(Game_Path.city_tiles_path[type]),
                (SceneSettings.tile_size, SceneSettings.tile_size),
            ),
            rect=rect,
        )


class Game_machine(EntityLike):
    def __init__(self, rect: pygame.rect.Rect):
        super().__init__(
            image=pygame.transform.scale(
                pygame.image.load(Game_Path.game_machine_path),
                (SceneSettings.tile_size * 2, SceneSettings.tile_size * 4),
            ),
            rect=rect,
        )


class Shop_icon(EntityLike):
    def __init__(self, rect: pygame.rect.Rect):
        super().__init__(
            image=pygame.transform.scale(
                pygame.image.load(Game_Path.shop_path),
                (SceneSettings.tile_size * 4, SceneSettings.tile_size * 4),
            ),
            rect=rect,
        )


class Hotel_icon(EntityLike):
    def __init__(self, rect: pygame.rect.Rect):
        super().__init__(
            image=pygame.transform.scale(
                pygame.image.load(Game_Path.hotel_path),
                (SceneSettings.tile_size * 4, SceneSettings.tile_size * 4),
            ),
            rect=rect,
        )
