import pygame
import time
import copy
import random

from Collections import *
from Settings import *
from Bgm_player import *
from Collections import *
from Game_manager import *
from Player import *
from Scenes import *
from Settings import *
from Boss_scene import *
from Boss_scene_entityLike import *

pygame.init()


class Boss1(Fixed_object):
    boss_bullets = pygame.sprite.Group()

    def __init__(self, image: pygame.Surface, rect: pygame.Rect):
        super().__init__(image, rect)
        pygame.sprite.Sprite.__init__(self)
        self.images = [
            pygame.image.load("./assets/boss_room/robot/walk_" + str(n) + ".png")
            for n in range(0, 16)
        ]
        self.hp = BossSettings.boss_hp  # boss的血量
        self.width = BossSettings.boss_width  # boss的宽度
        self.height = BossSettings.boss_height  # boss的高度
        self.image = pygame.transform.scale(
            pygame.image.load("./assets/boss_room/robot/walk_0.png"),
            (self.width, self.height),
        )
        self.rect = pygame.rect.Rect(
            BossSettings.wlid_boss_pos0[0],
            BossSettings.wlid_boss_pos0[1],
            self.width,
            self.height,
        )
        self.attack = BossSettings.boss_attack  # boss的攻击力
        self.speed = BossSettings.boss_Speed  # boss的速度
        self.move_region = ((900, 1300), (200, 700))
        self.swift = BossSettings.boss_animation_speed  # boss动画效果
        self.num = 0  # boss的动画效果
        self.move_num = 0  # boss的移动效果
        self.picture_num = 0  # boss的图片
        self.derection = 0
        self.hero_bullets = pygame.sprite.Group()
        self.boss_live = True
        self.boss_bullets = pygame.sprite.Group()
        self.boss_bullets1 = pygame.sprite.Group()

        self.boss_die_num = 0
        self.num = 0
        self.boss_animaton = True

    def listen(self, event: Event):

        if event.code == Event_Code.BOSS_ANIMATIOM:
            self.animation()  # boss动画效果
            self.move_num += 1
            if self.move_num >= 10:
                self.move_num = 0
                self.derection = random.randint(1, 5)

            if (
                self.derection == 1
                and self.rect.top >= self.move_region[1][0] + self.speed
                and self.hp > 0
            ):
                self.rect.top -= self.speed
            elif (
                self.derection == 2
                and self.rect.bottom <= self.move_region[1][1] - self.speed
                and self.hp > 0
            ):
                self.rect.bottom += self.speed
            elif (
                self.derection == 3
                and self.rect.left >= self.move_region[0][0] + self.speed
                and self.hp > 0
            ):
                self.rect.left -= self.speed
            elif (
                self.derection == 4
                and self.rect.right <= self.move_region[0][1] - self.speed
                and self.hp > 0
            ):
                self.rect.right += self.speed
            else:
                self.rect.right += 0

            if self.hp > 0:
                self.auto_fire()

        elif event.code == Event_Code.BOSS_DIE and self.boss_animaton:
            self.boss_die_num += 1
            if self.boss_die_num >= 100:
                self.boss_die_num = 0
                self.num += 1

            self.image = pygame.transform.scale(
                pygame.image.load(Game_Path.baozha_path[self.num]),
                (self.width, self.height),
            )  # boss死亡动画效果

            self.speed = 0
            if self.num >= 8:
                self.post(Event(Scene_Code.WIN))
                self.boss_animaton = False

        super().listen(event)  # 继承原有的响应事件内容，如对DRAW的响应

    def animation(self):
        self.num += self.swift
        if self.num >= 10:
            self.num = 0
            self.picture_num += 1

        self.image = pygame.transform.scale(
            pygame.image.load(Game_Path.boss_path[int((self.picture_num) % 6)]),
            (self.width, self.height),
        )  # 切换图片

    def auto_fire(self):  # 随机攻击
        if random.randint(1, 10) == 8:
            bullet = Boss_attack(self.rect)
            self.boss_bullets.add(bullet)

        if random.randint(1, 30) == 8:
            bullet1 = Boss_attack1(self.rect)
            self.boss_bullets1.add(bullet1)

    def draw(self):
        super().draw()
        for bullet in self.boss_bullets:
            bullet.update()
            bullet.draw()

        for bullet in self.boss_bullets1:
            bullet.update()
            bullet.draw()


class Boss_attack(Fixed_object):
    def __init__(self, rect):
        super().__init__(None, None)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(
            pygame.image.load(r".\assets\boss_room\zhidan\boss_bullet\1.png"), (50, 20)
        )
        self.bullet_speed = 30
        self.rect = pygame.Rect(rect[0] - 20, rect[1] + 80, 20, 20)

    def update(self):
        self.rect.left -= self.bullet_speed
        if self.rect.left <= -15:
            self.kill()


class Boss_attack1(Fixed_object):
    def __init__(self, rect):
        super().__init__(None, None)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(
            pygame.image.load(r".\assets\boss_room\zhidan\boss_bullet\2.png"), (60, 50)
        )
        self.bullet_speed = 30
        self.rect = pygame.Rect(rect[0] - 20, rect[1] + 80, 60, 50)

    def update(self):
        self.rect.left -= self.bullet_speed
        if self.rect.left <= -15:
            self.kill()


class Fellows:
    pass
