import pygame


from Collections import *
from Settings import *
from Player import *

pygame.init()


class Forest_Tile(EntityLike):
    def __init__(self, type: int, rect: pygame.rect.Rect):
        super().__init__(
            image=pygame.transform.scale(
                pygame.image.load(Game_Path.forest_tiles_path[type]),
                (SceneSettings.tile_size, SceneSettings.tile_size),
            ),
            rect=rect,
        )


class Fire(EntityLike):
    def __init__(self: int, rect: pygame.rect.Rect, player: Player1):
        super().__init__(
            image=pygame.transform.scale(
                pygame.image.load(Game_Path.fire_path[0]),
                (SceneSettings.tile_size, SceneSettings.tile_size),
            ),
            rect=rect,
        )
        self.player = player


class Tree(EntityLike):  # 障碍物的类
    def __init__(self, rect: pygame.rect.Rect):

        super().__init__(
            image=pygame.transform.scale(
                pygame.image.load(Game_Path.tree_path),
                (SceneSettings.tile_size, SceneSettings.tile_size * 3 / 2),
            ),
            rect=rect,
        )


class Enemy(EntityLike):
    def __init__(self, num, rect: pygame.Rect):
        pygame.sprite.Sprite.__init__(self)
        self.hp = EnemySettings.enemy_hp
        self.width = EnemySettings.enemy_width[num]
        self.height = EnemySettings.enemy_height[num]
        self.attack = EnemySettings.enemy_attack  # 玩家的攻击力
        self.image = pygame.transform.scale(
            pygame.image.load(Game_Path.enemy_path[num]), (self.width, self.height)
        )
        self.rect = rect


class Water(EntityLike):
    def __init__(self, rect: pygame.rect.Rect):
        super().__init__(
            image=pygame.transform.scale(
                pygame.image.load(Game_Path.forest_tiles_path[6]),
                (SceneSettings.tile_size, SceneSettings.tile_size),
            ),
            rect=rect,
        )
