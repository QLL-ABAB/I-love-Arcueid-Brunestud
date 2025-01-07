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

        self.hp = BossSettings.boss_hp  # boss的血量
        self.width = BossSettings.boss_width  # boss的宽度
        self.height = BossSettings.boss_height  # boss的高度
        self.image = pygame.transform.scale(
            pygame.image.load(Game_Path.boss_path[0]),
            (self.width, self.height),
        )
        self.rect = pygame.rect.Rect(
            BossSettings.wlid_boss_pos0[0],
            BossSettings.wlid_boss_pos0[1],
            self.width,
            self.height,
        )
        self.attack = BossSettings.boss_attack  # boss的攻击力
        self.speed = BossSettings.boss_speed  # boss的速度
        self.move_region = ((800, 1250), (50, 850))
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
        self.move_x = 0
        self.move_y = 0

        self.fellow1s = pygame.sprite.Group()
        self.fellow2s = pygame.sprite.Group()

    def listen(self, event: Event):

        if event.code == Event_Code.BOSS_ANIMATIOM:
            self.animation()  # boss动画效果
            self.move_num += 1
            if self.move_num >= 10:
                self.move_num = 0
                self.move_x = random.uniform(-1, 1)
                self.move_y = random.uniform(-1, 1)

            if self.hp > 0:
                # if  self.rect.top >= self.move_region[1][0] + self.speed:
                if not (
                    (
                        self.rect.top <= self.move_region[1][0] + self.speed
                        and self.move_y < 0
                    )
                    or (
                        self.rect.bottom >= self.move_region[1][1] - self.speed
                        and self.move_y > 0
                    )
                    or (
                        self.rect.left <= self.move_region[0][0] + self.speed
                        and self.move_x < 0
                    )
                    or (
                        self.rect.right >= self.move_region[0][1] - self.speed
                        and self.move_x > 0
                    )
                ):
                    self.rect.top += self.move_y * self.speed
                    self.rect.left += self.move_x * self.speed

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

        if random.randint(1, 40) == 8:
            bullet1 = Boss_attack1(self.rect)
            self.boss_bullets1.add(bullet1)

    def call_the_fellows(self):
        if self.hp > 0:
            random_num = random.randint(1, 10)
            if random_num == 2:
                self.fellow1s.add(Fellows(0))
            if random_num == 4:
                self.fellow2s.add(Fellows(1))

    def draw(self):
        super().draw()
        for bullet in self.boss_bullets:
            bullet.update()
            bullet.draw()

        for bullet in self.boss_bullets1:
            bullet.update()
            bullet.draw()

        for fellow in self.fellow1s:
            fellow.auto_fire()
            fellow.draw()

        for fellow in self.fellow2s:
            fellow.auto_fire()
            fellow.draw()


class Boss_attack(Fixed_object):
    def __init__(self, rect):
        super().__init__(None, None)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(
            pygame.image.load(Game_Path.bullet_path[0]), (50, 20)
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
            pygame.image.load(Game_Path.bullet_path[1]), (60, 50)
        )
        self.bullet_speed = BossSettings.boss_bullet_speed + 10
        self.rect = pygame.Rect(rect[0] - 20, rect[1] + 80, 60, 50)

    def update(self):
        self.rect.left -= self.bullet_speed
        if self.rect.left <= -15:
            self.kill()


class Fellows(Fixed_object):
    def __init__(self, type: int):
        pygame.sprite.Sprite.__init__(self)
        self.hp = Fellow_Settings.fellow_hp
        self.width = Fellow_Settings.fellow_width
        self.height = Fellow_Settings.fellow_height
        self.type = type
        self.image = pygame.transform.scale(
            pygame.image.load(Game_Path.fellow_path[self.type]),
            (self.width, self.height),
        )
        self.rect = pygame.rect.Rect(1300, 200, self.width, self.height)
        self.fellow_bullets = pygame.sprite.Group()

    def auto_fire(self):  # 随机攻击
        if random.randint(1, 20) == 8:
            bullet = Fellow_attack(self.rect)
            self.fellow_bullets.add(bullet)

    def draw(self):
        super().draw()
        for bullet in self.fellow_bullets:
            bullet.update()
            bullet.draw()


class Fellow_attack(Fixed_object):
    def __init__(self, rect):
        super().__init__(None, None)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(
            pygame.image.load(Game_Path.bullet_path[2]), (40, 40)
        )
        self.bullet_speed = BossSettings.boss_bullet_speed
        self.rect = pygame.Rect(rect[0] - 20, rect[1] + 80, 60, 50)

    def update(self):
        self.rect.left -= self.bullet_speed
        if self.rect.left <= -10:
            self.kill()
