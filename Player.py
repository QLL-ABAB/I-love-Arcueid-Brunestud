import pygame
import time
import copy
import random

from Collections import *
from Settings import *


pygame.init()


class Player1(EntityLike):  # 玩家类

    def __init__(self, image: pygame.Surface, rect: pygame.Rect):
        super().__init__(image, rect)
        pygame.sprite.Sprite.__init__(self)
        self.game_state = GameState()
        self.hp = self.game_state.player_hp  # 玩家的血量
        self.speed = PlayerSettings.player_Speed  # 玩家的速度
        self.width = PlayerSettings.player_width  # 玩家的宽度
        self.height = PlayerSettings.player_height  # 玩家的高度
        self.picture_num = 0  # 玩家的图片
        self.swift = PlayerSettings.player_animation_speed  # 玩家动画效果
        self.right = True  # 玩家是否向右移动
        self.burn = 0  # 燃烧爆条效果
        self.attack = self.game_state.player_attack  # 玩家的攻击力
        self.coin = self.game_state.coin  # 玩家的金币数量

        self.blood_eat = self.game_state.blood_eat
        self.through = self.game_state.through
        self.add_bullet_speed = self.game_state.add_bullet_speed
        self.skill = self.game_state.skill

        self.bottle = False

        self.player_bullets = pygame.sprite.Group()
        self.add_bullet_num = 0
        self.boss = False

    def listen(self, event: Event):  # 玩家类所响应的事件

        if event.code == pygame.KEYDOWN:  # 键盘按下事件
            self.keydown()

        elif event.code == Event_Code.CAN_MOVE:  # 响应场景发出的允许移动事件
            self.rect.x = event.body["POS"][0]
            self.rect.y = event.body["POS"][1]

        elif event.code == Event_Code.MOVE_ANIMATIOM:
            self.animation()  # 玩家动画效果

        elif event.code == Event_Code.STAND_STILL and self.hp > 0:  # 玩家静止状态

            if self.right == True or self.boss == True:
                self.image = pygame.transform.scale(
                    pygame.image.load(Game_Path.player_run_path1[0]),
                    (self.width, self.height),
                )

            elif self.right == False:
                self.image = pygame.transform.scale(
                    pygame.image.load(Game_Path.player_run_path2[0]),
                    (self.width, self.height),
                )

        elif event.code == Event_Code.DIE:
            self.image = pygame.transform.scale(
                pygame.image.load(Game_Path.player_die_path),
                (self.width, self.height),
            )  # 玩家死亡动画效果

            self.speed = 0

        elif event.code == Event_Code.BURN:
            self.burn += self.game_state.burn_speed  # 玩家燃烧效果
            if self.burn >= 30:
                self.hp -= 1  # 玩家受到伤害
                self.burn -= 30  # 重置燃烧效果
                if self.hp > 0:
                    copy_player = copy.copy(self.image)
                    copy_player = change_color(copy_player, 255, 0, 0)
                    self.image = copy_player  # 玩家燃烧效果
                else:
                    self.post(Event(Event_Code.DIE))
                    self.post(Event(Event_Code.DRAW))

        elif event.code == Scene_Code.CITY:
            self.burn = 0  # 重置燃烧效果

        elif event.code == Event_Code.HURT:
            if self.hp > 0:
                copy_player = copy.copy(self.image)
                copy_player = change_color(copy_player, 255, 0, 0)
                self.image = copy_player

            else:
                self.post(Event(Event_Code.DIE))
                self.post(Event(Event_Code.DRAW))

        super().listen(event)  # 继承原有的响应事件内容，如对DRAW的响应

    def keydown(self):

        keys = pygame.key.get_pressed()

        # 使用nx和ny计算将要移动到的位置
        nx = self.rect.x
        ny = self.rect.y

        if keys[pygame.K_w] and self.rect.y > 0 and self.hp > 0:  # W键被按下
            ny -= self.speed
            self.post(Event(Event_Code.MOVE_ANIMATIOM))

        if keys[pygame.K_a] and self.rect.x > 0 and self.hp > 0:
            nx -= self.speed
            self.post(Event(Event_Code.MOVE_ANIMATIOM))
            self.right = False

        if (
            keys[pygame.K_s]
            and self.rect.y < WindowSettings.height + self.height
            and self.hp > 0
        ):
            ny += self.speed
            self.post(Event(Event_Code.MOVE_ANIMATIOM))

        if (
            keys[pygame.K_d]
            and self.rect.x < WindowSettings.width + self.width
            and self.hp > 0
        ):
            nx += self.speed
            self.post(Event((Event_Code.MOVE_ANIMATIOM)))
            self.right = True

        if (
            not (
                keys[pygame.K_w]
                or keys[pygame.K_a]
                or keys[pygame.K_s]
                or keys[pygame.K_d]
            )
        ) or (
            keys[pygame.K_a]
            and keys[pygame.K_d]
            and not (keys[pygame.K_w] or keys[pygame.K_s])
        ):  # 没有按下任何键
            self.post(Event(Event_Code.STAND_STILL))

        self.post(Event(Event_Code.REQUEST_MOVE, {"POS": (nx, ny)}))  # 发出请求移动事件

        ############

    def animation(self):
        self.picture_num += self.swift  # 图片切换速度

        if self.right == True or self.boss == True:
            self.image = pygame.transform.scale(
                pygame.image.load(
                    Game_Path.player_run_path1[int((self.picture_num) % 7)]
                ),
                (self.width, self.height),
            )  # 切换图片

        elif self.right == False:
            self.image = pygame.transform.scale(
                pygame.image.load(
                    Game_Path.player_run_path2[int((self.picture_num) % 7)]
                ),
                (self.width, self.height),
            )  #


class Player_bullet(Fixed_object):
    def __init__(self, rect):
        super().__init__(None, None)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(
            pygame.image.load(Game_Path.bullet_path[3]),
            (50, 20),
        )
        self.bullet_speed = 20
        self.rect = pygame.Rect(rect[0] + 10, rect[1] + 30, 20, 20)

    def update(self):
        self.rect.right += self.bullet_speed
        if self.rect.right >= 1450:
            self.kill()


class Sword_light(Fixed_object):
    def __init__(self, rect, hold_time: int):
        super().__init__(None, None)
        pygame.sprite.Sprite.__init__(self)
        self.hold_time = hold_time
        self.image = pygame.transform.scale(
            pygame.image.load(Game_Path.player_sword_light_path),
            (30 + self.hold_time * 4, 90 + self.hold_time * 12),
        )
        self.bullet_speed = 25
        self.rect = self.image.get_rect(center=(rect[0] + 10, rect[1] + 20))

    def update(self):
        self.rect.right += self.bullet_speed
        if self.rect.right >= 1450:
            self.kill()
