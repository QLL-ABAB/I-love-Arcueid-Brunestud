import copy
import pygame
import random
import json
import os

from Collections import *
from Settings import *
from Wild_scene_entityLike import *
from Portals import *
from City_scene_entityLike import *
from Add_windows import *


class Scene_Beginning(Listener):
    def __init__(self):
        super().__init__()
        self.background = pygame.transform.scale(
            pygame.image.load(Game_Path.background_path[0]),
            (
                WindowSettings.width,
                WindowSettings.height,
            ),
        )
        self.choose_saver = False
        self.show_choose = True

    def listen(self, event: Event):
        super().listen(event)

        if event.code == Event_Code.DRAW:

            mouse_get_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()

            window.blit(self.background, (0, 0))

            text_surface = font2.render(
                "Press Q to enter", True, TextSettings.text_color
            )
            text_rect = text_surface.get_rect(
                center=(300, WindowSettings.height - TextSettings.box_height)
            )
            window.blit(text_surface, text_rect)

            self.text1 = font1.render("读取存档", True, (255, 255, 255))
            self.text1_rect = self.text1.get_rect(center=(1200, 750))
            self.button_image1 = pygame.Surface((250, 125))
            self.button_image1.fill((50, 50, 50))
            self.button_rect1 = self.button_image1.get_rect()
            self.button_rect1.center = (1200, 750)

            self.text2 = font1.render("存档1", True, (255, 255, 255))
            self.text2_rect = self.text1.get_rect(center=(1200, 650))
            self.button_image2 = pygame.Surface((180, 90))
            self.button_image2.fill((50, 50, 50))
            self.button_rect2 = self.button_image2.get_rect()
            self.button_rect2.center = (1200, 650)

            self.text3 = font1.render("存档2", True, (255, 255, 255))
            self.text3_rect = self.text3.get_rect(center=(1200, 750))
            self.button_rect3 = self.button_image2.get_rect(center=(1200, 750))

            self.text4 = font1.render("存档3", True, (255, 255, 255))
            self.text4_rect = self.text4.get_rect(center=(1200, 850))
            self.button_rect4 = self.button_image2.get_rect(center=(1200, 850))

            self.button_image1_clicked = pygame.Surface((250, 125))
            self.button_image1_clicked.fill((100, 100, 100))

            self.button_image2_clicked = pygame.Surface((250, 125))
            self.button_image2_clicked.fill((100, 100, 100))

            window.blit(self.button_image1, self.button_rect1)

            if self.show_choose:
                if self.button_rect1.collidepoint(mouse_pos):
                    window.blit(self.button_image1_clicked, self.button_rect1)
                    if mouse_get_pressed[0]:
                        self.choose_saver = True
                        self.show_choose = False
                else:
                    window.blit(self.button_image1, self.button_rect1)
                window.blit(self.text1, self.text1_rect)

            if self.choose_saver:
                if self.button_rect2.collidepoint(mouse_pos):
                    window.blit(self.button_image2_clicked, self.button_rect2)
                    if mouse_get_pressed[0]:
                        self.choose_saver = False

                else:
                    window.blit(self.button_image2, self.button_rect2)
                window.blit(self.text2, self.text2_rect)

                if self.button_rect3.collidepoint(mouse_pos):
                    window.blit(self.button_image2_clicked, self.button_rect3)
                    if mouse_get_pressed[0]:
                        self.choose_saver = False
                else:
                    window.blit(self.button_image2, self.button_rect3)
                window.blit(self.text3, self.text3_rect)

                if self.button_rect4.collidepoint(mouse_pos):
                    window.blit(self.button_image2_clicked, self.button_rect4)
                    if mouse_get_pressed[0]:
                        self.choose_saver = False
                else:
                    window.blit(self.button_image2, self.button_rect4)
                window.blit(self.text4, self.text4_rect)


class Scene_Ending(Listener):
    def __init__(self):
        super().__init__()
        self.background = pygame.transform.scale(
            pygame.image.load(Game_Path.background_path[1]),
            (
                WindowSettings.width,
                WindowSettings.height,
            ),
        )

    def listen(self, event: Event):
        super().listen(event)

        keys = pygame.key.get_pressed()

        if event.code == Event_Code.DRAW:
            window.blit(self.background, (0, 0))

            text_surface2 = font2.render("菜", True, (255, 0, 0))
            text_rect = text_surface2.get_rect(center=(1100, 450))
            window.blit(text_surface2, text_rect)

            text_surface1 = font2.render("Press R to restart", True, (0, 0, 0))
            text_rect1 = text_surface1.get_rect(center=(1000, 600))
            window.blit(text_surface1, text_rect1)

            if keys[pygame.K_r]:
                self.post(Event(Scene_Code.GAME_BEGIN))


class Scene_Winning(Listener):
    def __init__(self):
        super().__init__()
        self.background = pygame.transform.scale(
            pygame.image.load(Game_Path.background_path[2]),
            (
                WindowSettings.width,
                WindowSettings.height,
            ),
        )

    def listen(self, event: Event):
        super().listen(event)
        keys = pygame.key.get_pressed()
        if event.code == Event_Code.DRAW:
            window.blit(self.background, (0, 0))

            text_surface3 = font2.render("YOU WIN!!!!!", True, (0, 0, 0))
            text_rect = text_surface3.get_rect(
                center=(WindowSettings.width / 2, (WindowSettings.height / 2) + 200)
            )
            window.blit(text_surface3, text_rect)

            text_surface4 = font1.render("(Press R to restart)", True, (0, 0, 0))
            text_rect1 = text_surface4.get_rect(
                center=(WindowSettings.width / 2, (WindowSettings.height / 2) + 300)
            )
            window.blit(text_surface4, text_rect1)

            if keys[pygame.K_r]:
                self.post(Event(Scene_Code.GAME_BEGIN))
