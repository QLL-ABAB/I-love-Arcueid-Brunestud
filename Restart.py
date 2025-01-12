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
    def __init__(self, player):
        super().__init__()
        self.background = pygame.transform.scale(
            pygame.image.load(Game_Path.background_path[0]),
            (
                WindowSettings.width,
                WindowSettings.height,
            ),
        )
        self.choose_saver = False
        self.choose_saver_over = False
        self.show_choose = True
        self.player = player

        self.count_num = 40

        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """

        self.text1 = font1.render("读取存档", True, (255, 255, 255))
        self.text1_rect = self.text1.get_rect(center=(1200, 750))
        self.button_image1 = pygame.Surface((250, 125))
        self.button_image1.fill((50, 50, 50))
        self.button_rect1 = self.button_image1.get_rect()
        self.button_rect1.center = (1200, 750)

        self.text2 = font1.render("存档1", True, (255, 255, 255))
        self.text2_rect = self.text2.get_rect(center=(500, 500))
        self.button_image2 = pygame.Surface((180, 90))
        self.button_image2.fill((25, 25, 25))
        self.button_rect2 = self.button_image2.get_rect()
        self.button_rect2.center = (500, 500)

        self.text3 = font1.render("存档2", True, (255, 255, 255))
        self.text3_rect = self.text3.get_rect(center=(700, 500))
        self.button_rect3 = self.button_image2.get_rect(center=(700, 500))

        self.text4 = font1.render("存档3", True, (255, 255, 255))
        self.text4_rect = self.text4.get_rect(center=(900, 500))
        self.button_rect4 = self.button_image2.get_rect(center=(900, 500))

        self.button_image1_clicked = pygame.Surface((250, 125))
        self.button_image1_clicked.fill((100, 100, 100))

        self.button_image2_clicked = pygame.Surface((180, 90))
        self.button_image2_clicked.fill((100, 100, 100))

        self.text5 = font2.render(
            "Choose a save file to load!!!!!", True, (255, 255, 255)
        )
        self.text5_rect = self.text5.get_rect(center=(WindowSettings.width / 2, 350))

        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """
        self.judege_window_image = pygame.Surface((1200, 700))
        self.judege_window_image.fill((20, 20, 20))
        self.judege_window_image.set_alpha(220)
        self.judege_window_rect = self.judege_window_image.get_rect()
        self.judege_window_rect.center = (
            WindowSettings.width // 2,
            WindowSettings.height // 2,
        )
        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """
        self.text_surface = font2.render("Now press Q to enter", True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(
            center=(
                WindowSettings.width / 2,
                WindowSettings.height - 150,
            )
        )
        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """
        self.delete_icon = pygame.image.load(Game_Path.delete_path)

        self.delete = pygame.Surface((120, 120))
        self.delete.fill((100, 100, 100))
        self.delete_rect1 = self.delete.get_rect(center=(500, 600))
        self.delete_rect2 = self.delete.get_rect(center=(700, 600))
        self.delete_rect3 = self.delete.get_rect(center=(900, 600))

        self.delete_clicked = pygame.Surface((120, 120))
        self.delete_clicked.fill((200, 200, 200))

        self.to_delete = None
        self.whether_delete = False
        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """
        self.text6 = font3.render(
            "Is it okay to refresh the save file?", True, (255, 255, 255)
        )
        self.text6_rect = self.text6.get_rect(center=(700, 400))

        self.text7 = font1.render("Yes", True, (255, 255, 255))
        self.text7_rect = self.text7.get_rect(center=(450, 600))
        self.button_image7 = pygame.Surface((180, 90))
        self.button_image7.fill((25, 25, 25))
        self.button_rect7 = self.button_image2.get_rect()
        self.button_rect7.center = (450, 600)

        self.text8 = font1.render("No", True, (255, 255, 255))
        self.text8_rect = self.text3.get_rect(center=(950, 600))
        self.button_rect8 = self.button_image7.get_rect(center=(950, 600))

        self.button_image2_clicked = pygame.Surface((180, 90))
        self.button_image2_clicked.fill((100, 100, 100))

        self.text5 = font2.render(
            "Choose a save file to load!!!!!", True, (255, 255, 255)
        )
        self.text5_rect = self.text5.get_rect(center=(WindowSettings.width / 2, 350))
        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """

    def listen(self, event: Event):
        super().listen(event)
        if self.count_num < 40:
            self.count_num += 1

        if event.code == Event_Code.DRAW:

            mouse_get_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()

            window.blit(self.background, (0, 0))

            if self.choose_saver_over:
                window.blit(self.text_surface, self.text_rect)

            if self.show_choose:
                if self.button_rect1.collidepoint(mouse_pos):
                    window.blit(self.button_image1_clicked, self.button_rect1)
                    if mouse_get_pressed[0] and self.count_num == 40:
                        self.choose_saver = True
                        self.show_choose = False
                        self.count_num = 0
                else:
                    window.blit(self.button_image1, self.button_rect1)
                window.blit(self.text1, self.text1_rect)

            if self.choose_saver or self.whether_delete:
                window.blit(self.judege_window_image, self.judege_window_rect)

            if self.choose_saver:
                window.blit(self.text5, self.text5_rect)

                """
                >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                """
                if self.delete_rect1.collidepoint(mouse_pos):
                    window.blit(self.delete_clicked, self.delete_rect1)
                    if mouse_get_pressed[0] and self.count_num == 40:
                        self.to_delete = "./save1.json"
                        self.whether_delete = True
                        self.choose_saver = False
                        self.count_num = 0
                else:
                    window.blit(self.delete, self.delete_rect1)

                if self.delete_rect2.collidepoint(mouse_pos):
                    window.blit(self.delete_clicked, self.delete_rect2)
                    if mouse_get_pressed[0] and self.count_num == 40:
                        self.to_delete = "./save2.json"
                        self.whether_delete = True
                        self.choose_saver = False
                        self.count_num = 0
                else:
                    window.blit(self.delete, self.delete_rect2)

                if self.delete_rect3.collidepoint(mouse_pos):
                    window.blit(self.delete_clicked, self.delete_rect3)
                    if mouse_get_pressed[0] and self.count_num == 40:
                        self.to_delete = "./save3.json"
                        self.whether_delete = True
                        self.choose_saver = False
                        self.count_num = 0
                else:
                    window.blit(self.delete, self.delete_rect3)

                window.blit(self.delete_icon, self.delete_rect1)
                window.blit(self.delete_icon, self.delete_rect2)
                window.blit(self.delete_icon, self.delete_rect3)
                """
                >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                """
                if self.button_rect2.collidepoint(mouse_pos):
                    window.blit(self.button_image2_clicked, self.button_rect2)
                    if mouse_get_pressed[0] and self.count_num == 40:
                        self.choose_saver = False
                        game_state_original = load_game("./save1.json")
                        update_state(self.player, game_state_original)
                        self.player.save_name = "./save1.json"
                        self.count_num = 0
                        self.choose_saver_over = True

                else:
                    window.blit(self.button_image2, self.button_rect2)
                window.blit(self.text2, self.text2_rect)

                if self.button_rect3.collidepoint(mouse_pos):
                    window.blit(self.button_image2_clicked, self.button_rect3)
                    if mouse_get_pressed[0] and self.count_num == 40:
                        self.choose_saver = False
                        game_state_original = load_game("./save2.json")
                        update_state(self.player, game_state_original)
                        self.player.save_name = "./save2.json"
                        self.count_num = 0
                        self.choose_saver_over = True

                else:
                    window.blit(self.button_image2, self.button_rect3)
                window.blit(self.text3, self.text3_rect)

                if self.button_rect4.collidepoint(mouse_pos):
                    window.blit(self.button_image2_clicked, self.button_rect4)
                    if mouse_get_pressed[0] and self.count_num == 40:
                        self.choose_saver = False
                        game_state_original = load_game("./save3.json")
                        update_state(self.player, game_state_original)
                        self.player.save_name = "./save3.json"
                        self.count_num = 0
                        self.choose_saver_over = True
                else:
                    window.blit(self.button_image2, self.button_rect4)
                window.blit(self.text4, self.text4_rect)

                """
                >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                """
            if self.whether_delete:
                if self.button_rect7.collidepoint(mouse_pos):
                    window.blit(self.button_image2_clicked, self.button_rect7)
                    if mouse_get_pressed[0] and self.count_num == 40:
                        game_state_refresh = GameState()
                        save_game(game_state_refresh, self.to_delete)
                        self.whether_delete = False
                        self.choose_saver = True
                        self.count_num = 0
                else:
                    window.blit(self.button_image7, self.button_rect7)

                if self.button_rect8.collidepoint(mouse_pos):
                    window.blit(self.button_image2_clicked, self.button_rect8)
                    if mouse_get_pressed[0] and self.count_num == 40:
                        self.whether_delete = False
                        self.choose_saver = True
                        self.count_num = 0
                else:
                    window.blit(self.button_image7, self.button_rect8)

                window.blit(self.text6, self.text6_rect)
                window.blit(self.text7, self.text7_rect)
                window.blit(self.text8, self.text8_rect)


class Scene_Ending(Listener):
    def __init__(self, player):
        super().__init__()
        self.background = pygame.transform.scale(
            pygame.image.load(Game_Path.background_path[1]),
            (
                WindowSettings.width,
                WindowSettings.height,
            ),
        )
        self.player = player

    def listen(self, event: Event):
        super().listen(event)

        keys = pygame.key.get_pressed()

        if event.code == Event_Code.DRAW:

            game_state_refresh = GameState()
            save_game(game_state_refresh, self.player.save_name)

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
    def __init__(self, player):
        super().__init__()
        self.background = pygame.transform.scale(
            pygame.image.load(Game_Path.background_path[2]),
            (
                WindowSettings.width,
                WindowSettings.height,
            ),
        )
        self.player = player

    def listen(self, event: Event):
        super().listen(event)
        keys = pygame.key.get_pressed()
        if event.code == Event_Code.DRAW:

            game_state_refresh = GameState()
            save_game(game_state_refresh, self.player.save_name)

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
