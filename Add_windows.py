import pygame
from pygame.locals import *
import copy
import time
import math
import random

from Collections import *
from Settings import *
from Openai import *


pygame.init()


font1 = pygame.font.Font(Game_Path.word_path, TextSettings.font_size)
font2 = pygame.font.Font(Game_Path.word_path, TextSettings.font_size_plus)
font3 = pygame.font.Font(Game_Path.word_path, TextSettings.font_size_middle)
box_rect = pygame.Rect(
    0,
    WindowSettings.height - TextSettings.box_height,
    WindowSettings.width,
    TextSettings.box_height,
)
box_surface = pygame.Surface(box_rect.size)
box_surface.fill(TextSettings.box_color)


class Scene_Fight(Listener):
    def __init__(self, player, type):
        super().__init__()
        self.attribute_size = SceneSettings.attribute_size
        self.player_real = player
        self.enemy_attack = [2, 1]
        self.enemy_hp = [13, 8]
        self.coin_add = [5, 2]
        self.enemy_pos = (1000, 600)
        self.player_pos = (200, 600)

        self.player_right = True
        self.enemy_left = True
        self.player_act = False
        self.enemy_act = False
        self.choose = True
        self.player_defend = False
        self.player_swing = False

        self.animation_num = 0
        self.animation_speed = 1

        self.player_hp_showings = []
        self.enemy_hp_showings = []

        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """  # 按钮

        self.button_image1 = pygame.Surface((140, 70))
        self.button_image1.fill((50, 50, 50))
        self.button_rect1 = self.button_image1.get_rect(center=(200, 550))
        self.button_image1_clicked = pygame.Surface((140, 70))
        self.button_image1_clicked.fill((100, 100, 100))

        self.button_image2 = pygame.Surface((140, 70))
        self.button_image2.fill((50, 50, 50))
        self.button_rect2 = self.button_image2.get_rect(center=(350, 550))
        self.button_image2_clicked = pygame.Surface((140, 70))
        self.button_image2_clicked.fill((100, 100, 100))

        self.button_image3 = pygame.Surface((140, 70))
        self.button_image3.fill((50, 50, 50))
        self.button_rect3 = self.button_image3.get_rect(center=(1250, 150))
        self.button_image3_clicked = pygame.Surface((140, 70))
        self.button_image3_clicked.fill((100, 100, 100))

        self.button_image4 = pygame.Surface((140, 70))
        self.button_image4.fill((50, 50, 50))
        self.button_rect4 = self.button_image4.get_rect(center=(700, 200))
        # self.button_image4_clicked = pygame.Surface((140, 70))
        # self.button_image4_clicked.fill((100, 100, 100))

        self.button_text1 = font1.render("FIGHT", True, (255, 255, 255))
        self.button_text2 = font1.render("DEFEND", True, (255, 255, 255))
        self.button_text3 = font1.render("RTPS", True, (255, 255, 255))
        self.button_text4 = font1.render("代理中", True, (255, 255, 255))
        self.button_text1_rect = self.button_text1.get_rect(center=(200, 550))
        self.button_text2_rect = self.button_text2.get_rect(center=(350, 550))
        self.button_text3_rect = self.button_text3.get_rect(center=(1250, 150))
        self.button_text4_rect = self.button_text4.get_rect(center=(700, 200))

        self.daili = -1
        self.count_num = 0

        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """
        self.attack_harder = False
        self.attack_harder_image = pygame.transform.scale(
            pygame.image.load(Game_Path.attribute_path[15]),
            (SceneSettings.attribute_size * 3, SceneSettings.attribute_size * 3),
        )
        self.attack_harder_rect = self.attack_harder_image.get_rect()
        self.attack_harder_rect.center = (40, 90)

        for i in range(20):
            self.player_hp_showings.append(
                Attribute_showing(
                    0,
                    pygame.Rect(
                        i * 25 + 10, 30, self.attribute_size, self.attribute_size
                    ),
                )
            )

        for i in range(14):
            self.enemy_hp_showings.append(
                Attribute_showing(
                    11,
                    pygame.Rect(
                        1340 - i * 25,
                        30,
                        self.attribute_size,
                        self.attribute_size,
                    ),
                )
            )

        self.background = pygame.transform.scale(
            pygame.image.load(Game_Path.background_path[4]),
            (
                WindowSettings.width,
                WindowSettings.height,
            ),
        )
        self.attribute_size = SceneSettings.attribute_size

        self.player = Fixed_object(
            pygame.transform.scale(
                pygame.image.load(Game_Path.player_run_path1[0]), (200, 200)
            ),
            pygame.Rect(200, 600, 200, 200),
        )

        self.enemy1 = Fixed_object(
            pygame.transform.scale(
                pygame.image.load(Game_Path.enemy_path[3]), (200, 200)
            ),
            pygame.Rect(1000, 600, 200, 200),
        )

        self.enemy2 = Fixed_object(
            pygame.transform.scale(
                pygame.image.load(Game_Path.enemy_path[2]), (200, 200)
            ),
            pygame.Rect(1000, 600, 200, 200),
        )

        self.type = type

        self.ai_choose_num = 0

    def ai_choose(self):
        try:
            Question = "choose 1 or 2 with equal probability, respond with one number"
            Answer = int(AI_talk(Question))
            print(Answer)
            if Answer % 2 == 1:
                return 1
            else:
                return 2
        except:
            return random.randint(1, 2)

    def listen(self, event: Event):
        super().listen(event)

        if self.count_num < 40:
            self.count_num += 1

        if event.code == Event_Code.DRAW:
            """
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            """  # 判断是否可以继续

            if self.player_real.hp <= 0:
                self.post(Event(Scene_Code.GAME_OVER))

            if self.enemy_hp[self.type - 1] <= 0:
                self.player_real.coin += self.coin_add[self.type - 1]
                self.post(Event(Scene_Code.FOREST))
                self.player_real.speed = PlayerSettings.player_Speed

            """
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            """  # 背景

            window.blit(self.background, (0, 0))

            for i in range(self.player_real.hp):
                hp = self.player_hp_showings[i]
                window.blit(hp.image, hp.rect)

            for i in range(self.enemy_hp[self.type - 1]):
                hp = self.enemy_hp_showings[i]
                window.blit(hp.image, hp.rect)

            """
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            """  # 自动移动

            if self.player_right and self.player_act:
                self.player.rect = (
                    self.player_pos[0]
                    + (self.enemy_pos[0] - 100 - self.player_pos[0])
                    * self.animation_num
                    / 200,
                    self.player_pos[1]
                    + (self.enemy_pos[1] - self.player_pos[1])
                    * self.animation_num
                    / 200,
                    200,
                    200,
                )

            if (not self.player_right) and self.player_act:
                self.player.rect = (
                    self.enemy_pos[0]
                    - 100
                    - (self.enemy_pos[0] - 100 - self.player_pos[0])
                    * self.animation_num
                    / 200,
                    self.enemy_pos[1]
                    - (self.enemy_pos[1] - self.player_pos[1])
                    * self.animation_num
                    / 200,
                    200,
                    200,
                )

            if self.type == 1:
                if self.enemy_act:
                    if self.enemy_left:
                        self.enemy1.rect = (
                            self.enemy_pos[0]
                            - (self.enemy_pos[0] - 100 - self.player_pos[0])
                            * self.animation_num
                            / 200,
                            self.enemy_pos[1]
                            - (self.enemy_pos[1] - self.player_pos[1])
                            * self.animation_num
                            / 200,
                            200,
                            200,
                        )

                    if not self.enemy_left:
                        self.enemy1.rect = (
                            self.player_pos[0]
                            + 100
                            + (self.enemy_pos[0] - 100 - self.player_pos[0])
                            * self.animation_num
                            / 200,
                            self.enemy_pos[1]
                            - (self.enemy_pos[1] - self.player_pos[1])
                            * self.animation_num
                            / 200,
                            200,
                            200,
                        )

                self.enemy1.draw()

            if self.type == 2:

                if self.enemy_act:
                    if self.enemy_left:
                        self.enemy2.rect = (
                            self.enemy_pos[0]
                            - (self.enemy_pos[0] - 100 - self.player_pos[0])
                            * self.animation_num
                            / 200,
                            self.enemy_pos[1]
                            - (self.enemy_pos[1] - self.player_pos[1])
                            * self.animation_num
                            / 200,
                            200,
                            200,
                        )

                    if not self.enemy_left:
                        self.enemy2.rect = (
                            self.player_pos[0]
                            + 100
                            + (self.enemy_pos[0] - 100 - self.player_pos[0])
                            * self.animation_num
                            / 200,
                            self.player_pos[1]
                            + (self.enemy_pos[1] - self.player_pos[1])
                            * self.animation_num
                            / 200,
                            200,
                            200,
                        )

                self.enemy2.draw()

            self.player.draw()

            if self.attack_harder:
                window.blit(self.attack_harder_image, self.attack_harder_rect)

            """
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            """  # 选择

            mouse = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if self.choose:
                if self.daili != 1:
                    if self.button_rect1.collidepoint(mouse):
                        window.blit(self.button_image1_clicked, self.button_rect1)
                        if mouse_pressed[0]:
                            self.choose = False
                            self.player_swing = True
                            self.player_defend = False
                            self.player_act = True
                    else:
                        window.blit(self.button_image1, self.button_rect1)

                    if self.button_rect2.collidepoint(mouse) and self.daili != 1:
                        window.blit(self.button_image2_clicked, self.button_rect2)
                        if mouse_pressed[0]:
                            self.choose = False
                            self.player_defend = True
                            self.player_swing = False
                            self.enemy_act = True
                            self.enemy_left = True
                    else:
                        window.blit(self.button_image2, self.button_rect2)

                else:
                    self.ai_choose_num = self.ai_choose()
                    if self.ai_choose_num == 1:
                        self.choose = False
                        self.player_swing = True
                        self.player_defend = False
                        self.player_act = True

                    elif self.ai_choose_num == 2:
                        self.choose = False
                        self.player_defend = True
                        self.player_swing = False
                        self.enemy_act = True
                        self.enemy_left = True

                if self.daili != 1:
                    window.blit(self.button_text1, self.button_text1_rect)
                    window.blit(self.button_text2, self.button_text2_rect)

            if (
                self.button_rect3.collidepoint(mouse)
                and mouse_pressed[0]
                and self.count_num >= 40
            ):
                self.daili = 1
                self.count_num = 0

            if self.daili == 1:
                window.blit(self.button_image3_clicked, self.button_rect3)
            else:
                window.blit(self.button_image3, self.button_rect3)

            window.blit(self.button_text3, self.button_text3_rect)

            if self.daili == 1:
                window.blit(self.button_image4, self.button_rect4)
                window.blit(self.button_text4, self.button_text4_rect)

            """
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            """  #  角色自动化程序

            if self.player_swing:
                if (self.player_right == False and self.player_act == True) or (
                    self.enemy_left == False and self.enemy_act == True
                ):
                    self.animation_num += 6
                else:
                    self.animation_num += 4

                if self.animation_num >= 200:
                    self.animation_num = 0
                    if self.player_act:
                        if self.player_right:
                            self.player_right = False
                            if self.attack_harder:
                                self.enemy_hp[self.type - 1] -= math.floor(
                                    self.player_real.attack * 1.5
                                )
                                self.attack_harder = False
                            else:
                                self.enemy_hp[self.type - 1] -= self.player_real.attack

                        elif not self.player_right:
                            self.player_act = False
                            self.enemy_act = True
                            self.player_right = True

                    elif self.enemy_act:
                        if self.enemy_left:
                            self.enemy_left = False
                            self.player_real.hp -= self.enemy_attack[self.type - 1]

                        elif not self.enemy_left:
                            self.enemy_act = False
                            self.enemy_left = True
                            self.choose = True
                            self.player_swing = False

                    time.sleep(1)

            if self.player_defend:
                if self.enemy_left == False and self.enemy_act == True:
                    self.animation_num += 6
                else:
                    self.animation_num += 4

                if self.animation_num >= 200:

                    self.animation_num = 0
                    self.attack_harder = True

                    if self.enemy_act:
                        if self.enemy_left:
                            self.enemy_left = False
                            self.player_real.hp -= self.enemy_attack[self.type - 1] - 1

                        elif not self.enemy_left:
                            self.enemy_act = False
                            self.enemy_left = True
                            self.choose = True
                            self.player_defend = False

                    time.sleep(1)
