import pygame
import copy
import textwrap


from Collections import *
from Settings import *
from Wild_scene_entityLike import *
from Portals import *
from City_scene_entityLike import *
from Add_windows import *
from Openai import *

pygame.init()


class Scene_Shop(Listener):
    def __init__(self, player):
        super().__init__()
        self.background = pygame.transform.scale(
            pygame.image.load(Game_Path.background_path[3]),
            (
                WindowSettings.width,
                WindowSettings.height,
            ),
        )
        self.attribute_size = SceneSettings.attribute_size
        self.player = player
        self.blocks = []
        self.not_buy_blood = True
        self.not_buy_through = True
        self.not_buy_add_bullet_speed = True
        self.not_buy_skill = True
        self.not_buy_bottle = True

        self.add_hp = Attribute_showing(3, pygame.Rect(500, 150, 100, 100))
        self.add_hp_original_image = copy.copy(self.add_hp.image)
        self.add_hp_changed_image = change_color(self.add_hp.image, 1.5, 1.5, 1.5)

        self.add_attack = Attribute_showing(5, pygame.Rect(800, 150, 100, 100))
        self.add_attack_original_image = copy.copy(self.add_attack.image)
        self.add_attack_changed_image = change_color(
            self.add_attack.image, 1.5, 1.5, 1.5
        )

        self.eat_blood = Attribute_showing(6, pygame.Rect(1100, 150, 100, 100))
        self.eat_blood_original_image = copy.copy(self.eat_blood.image)
        self.eat_blood_changed_image = change_color(self.eat_blood.image, 1.5, 1.5, 1.5)

        self.Arucrid = Attribute_showing(7, pygame.Rect(75, 150, 350, 1228))

        self.exit = Attribute_showing(9, pygame.Rect(1000, 430, 200, 114))
        self.exit_original_image = copy.copy(self.exit.image)
        self.exit_changed_image = change_color(self.exit.image, 1.5, 1.5, 1.5)

        self.through = Attribute_showing(12, pygame.Rect(500, 280, 100, 100))
        self.through_original_image = copy.copy(self.through.image)
        self.through_changed_image = change_color(self.through.image, 1.5, 1.5, 1.5)

        self.add_bullet_speed = Attribute_showing(13, pygame.Rect(800, 280, 100, 100))
        self.add_bullet_speed_original_image = copy.copy(self.add_bullet_speed.image)
        self.add_bullet_speed_changed_image = change_color(
            self.add_bullet_speed.image, 1.5, 1.5, 1.5
        )

        self.skill = Attribute_showing(14, pygame.Rect(1100, 280, 100, 100))
        self.skill_original_image = copy.copy(self.skill.image)
        self.skill_changed_image = change_color(self.skill.image, 1.5, 1.5, 1.5)

        self.bottle = Attribute_showing(16, pygame.Rect(500, 430, 100, 100))
        self.bottle_original_image = copy.copy(self.bottle.image)
        self.bottle_changed_image = change_color(self.bottle.image, 1.5, 1.5, 1.5)

        self.num1 = 20

        self.coin_image = pygame.transform.scale(
            pygame.image.load(Game_Path.coin_path),
            (self.attribute_size * 2, self.attribute_size * 2),
        )
        self.attack_showing = Attribute_showing(
            10, pygame.Rect(10, 100, self.attribute_size * 2, self.attribute_size * 2)
        )

        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """
        self.word_window1 = pygame.Surface((1400, 350))
        self.word_window1.fill((0, 0, 0))
        self.word_window1.set_alpha(200)
        self.word_window_rect = pygame.Rect(0, 550, 1400, 400)

        self.word_window_judge = False

        self.exit_dialog = Attribute_showing(9, pygame.Rect(1300, 843, 100, 57))
        self.exit_dialog.image = pygame.transform.scale(
            pygame.image.load(Game_Path.attribute_path[9]),
            (100, 57),
        )
        self.exit_dialog_original_image = copy.copy(self.exit_dialog.image)
        self.exit_dialog_changed_image = change_color(
            self.exit_dialog.image, 1.5, 1.5, 1.5
        )
        self.word_return = ""
        self.word_print1_before = []

        self.rows_num_choice = 0
        self.rows_num = 0
        self.rows_left = 0
        self.row = [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]
        self.max_width = 80
        self.wrapped_lines = []
        self.answer_show = False
        self.words_input_show = []
        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """

    def mouse(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_get_pressed = pygame.mouse.get_pressed()

        if self.num1 <= 20:
            self.num1 += 1

        if self.add_hp.rect.collidepoint(mouse_pos):
            self.add_hp.image = self.add_hp_changed_image

            if (
                self.player.coin >= 1
                and self.player.hp < 20
                and mouse_get_pressed[0]
                and self.num1 >= 20
            ):
                self.num1 = 0
                self.player.hp += 1
                self.player.coin -= 1

        else:
            self.add_hp.image = self.add_hp_original_image

        if self.add_attack.rect.collidepoint(mouse_pos):
            self.add_attack.image = self.add_attack_changed_image
            if (
                self.player.coin >= 1
                and self.player.attack < 6
                and mouse_get_pressed[0]
                and self.num1 >= 20
            ):
                self.num1 = 0
                self.player.attack += 1
                self.player.coin -= 1
        else:
            self.add_attack.image = self.add_attack_original_image

        if self.eat_blood.rect.collidepoint(mouse_pos):
            self.eat_blood.image = self.eat_blood_changed_image

            if (
                self.player.coin >= 2
                and self.not_buy_blood == True
                and mouse_get_pressed[0]
                and self.num1 >= 20
            ):
                self.num1 = 0
                self.player.coin -= 2
                self.not_buy_blood = False
                self.player.blood_eat = True

        else:
            self.eat_blood.image = self.eat_blood_original_image

        if self.through.rect.collidepoint(mouse_pos):
            self.through.image = self.through_changed_image

            if (
                self.player.coin >= 3
                and self.not_buy_through == True
                and mouse_get_pressed[0]
                and self.num1 >= 20
            ):
                self.num1 = 0
                self.player.coin -= 3
                self.not_buy_through = False
                self.player.through = True
        else:
            self.through.image = self.through_original_image

        if self.add_bullet_speed.rect.collidepoint(mouse_pos):
            self.add_bullet_speed.image = self.add_bullet_speed_changed_image

            if (
                self.player.coin >= 4
                and self.not_buy_add_bullet_speed == True
                and mouse_get_pressed[0]
                and self.num1 >= 20
            ):
                self.num1 = 0
                self.player.coin -= 4
                self.not_buy_add_bullet_speed = False
                self.player.add_bullet_speed = True
        else:
            self.add_bullet_speed.image = self.add_bullet_speed_original_image

        if self.skill.rect.collidepoint(mouse_pos):
            self.skill.image = self.skill_changed_image

            if (
                self.player.coin >= 3
                and self.not_buy_skill == True
                and mouse_get_pressed[0]
                and self.num1 >= 20
            ):
                self.num1 = 0
                self.player.coin -= 3
                self.not_buy_skill = False
                self.player.skill = True

        else:
            self.skill.image = self.skill_original_image

        if self.bottle.rect.collidepoint(mouse_pos):
            self.bottle.image = self.bottle_changed_image

            if (
                self.player.coin >= 1
                and self.not_buy_bottle == True
                and mouse_get_pressed[0]
                and self.num1 >= 20
            ):
                self.num1 = 0
                self.player.coin -= 1
                self.not_buy_bottle = False
                self.player.bottle = True

        else:
            self.bottle.image = self.bottle_original_image

        if self.exit.rect.collidepoint(mouse_pos):
            self.exit.image = self.exit_changed_image
            if mouse_get_pressed[0]:
                self.post(Event(Scene_Code.CITY))
        else:
            self.exit.image = self.exit_original_image

        if (
            self.Arucrid.rect.collidepoint(mouse_pos)
            and mouse_get_pressed[0]
            and self.word_window_judge == False
        ):
            self.word_window_judge = True

        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """

    def word_window(self, judge, event_get):
        mouse_pos = pygame.mouse.get_pos()
        mouse_get_pressed = pygame.mouse.get_pressed()
        if judge:
            window.blit(self.word_window1, self.word_window_rect)
            window.blit(self.exit_dialog.image, self.exit_dialog.rect)

            if self.exit_dialog.rect.collidepoint(mouse_pos):
                self.exit_dialog.image = self.exit_dialog_changed_image
                if mouse_get_pressed[0]:
                    self.word_window_judge = False
            else:
                self.exit_dialog.image = self.exit_dialog_original_image

            for event in event_get:
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_BACKSPACE:
                        if self.word_print1_before:
                            self.word_print1_before.pop()
                            self.row[0] = "".join(self.word_print1_before)

                    elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:

                        self.rows_num_choice = 0

                        self.word_input = "".join(self.word_print1_before)
                        # self.row[0] = ""
                        self.word_return = AI_talk(self.word_input)
                        self.wrapped_lines = textwrap.wrap(
                            self.word_return, width=self.max_width
                        )
                        # print(self.wrapped_lines)
                        self.rows_num = len(self.wrapped_lines) // 8
                        self.rows_left = len(self.wrapped_lines) % 8
                        self.answer_show = True
                        self.word_print1_before = []
                        self.word_input = ""

                    elif event.key == pygame.K_TAB:
                        self.rows_num_choice = 0
                        self.word_print1_before = []
                        self.rows_num = 0

                        self.wrapped_lines = []
                        self.word_print1_before = []
                        self.row[0] = ""
                        self.row[1] = ""
                        self.row[2] = ""
                        self.row[3] = ""
                        self.row[4] = ""
                        self.row[5] = ""
                        self.row[6] = ""
                        self.row[7] = ""
                        self.answer_show = False

                    elif event.key == pygame.K_UP:
                        if self.rows_num_choice > 0:
                            self.rows_num_choice -= 1

                    elif event.key == pygame.K_DOWN:
                        if self.rows_num_choice < self.rows_num:
                            self.rows_num_choice += 1

                    else:
                        self.word_print1_before.append(event.unicode)
                        self.wrapped_lines = textwrap.wrap(
                            "".join(self.word_print1_before), width=self.max_width
                        )
                        self.rows_num = len(self.wrapped_lines) // 8
                        self.rows_left = len(self.wrapped_lines) % 8

            if self.rows_num_choice < self.rows_num:
                for j in range(8):
                    self.row[j] = self.wrapped_lines[self.rows_num_choice * 8 + j]

            elif self.rows_num_choice == self.rows_num:

                for j in range(len(self.wrapped_lines) % 8):
                    self.row[j] = self.wrapped_lines[self.rows_num_choice * 8 + j]
                for j in range(len(self.wrapped_lines) % 8, 8):
                    self.row[j] = ""

            window.blit(
                font1.render(self.row[0], True, (255, 255, 255)),
                (10, 560),
            )
            window.blit(
                font1.render(self.row[1], True, (255, 255, 255)),
                (10, 600),
            )
            window.blit(
                font1.render(self.row[2], True, (255, 255, 255)),
                (10, 640),
            )
            window.blit(
                font1.render(self.row[3], True, (255, 255, 255)),
                (10, 680),
            )
            window.blit(
                font1.render(self.row[4], True, (255, 255, 255)),
                (10, 720),
            )
            window.blit(
                font1.render(self.row[5], True, (255, 255, 255)),
                (10, 760),
            )
            window.blit(
                font1.render(self.row[6], True, (255, 255, 255)),
                (10, 800),
            )
            window.blit(
                font1.render(self.row[7], True, (255, 255, 255)),
                (10, 840),
            )

        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """

    def listen(self, event: Event):
        super().listen(event)

        if event.code == Event_Code.DRAW:
            window.blit(self.background, (0, 0))
            window.blit(self.add_hp.image, self.add_hp.rect)
            window.blit(self.add_attack.image, self.add_attack.rect)
            window.blit(self.eat_blood.image, self.eat_blood.rect)
            window.blit(self.Arucrid.image, self.Arucrid.rect)
            window.blit(self.exit.image, self.exit.rect)
            window.blit(self.through.image, self.through.rect)
            window.blit(self.add_bullet_speed.image, self.add_bullet_speed.rect)
            window.blit(self.skill.image, self.skill.rect)
            window.blit(self.bottle.image, self.bottle.rect)

            for i in range(self.player.hp):
                hp1 = Attribute_showing(
                    0,
                    pygame.Rect(
                        i * 25 + 10, 30, self.attribute_size, self.attribute_size
                    ),
                )
                window.blit(hp1.image, hp1.rect)

            window.blit(self.coin_image, (10, 60))
            coin_num = font1.render(str(self.player.coin), True, (0, 0, 0))
            window.blit(coin_num, (50, 60))
            window.blit(self.attack_showing.image, self.attack_showing.rect)
            attack_num = font1.render(str(self.player.attack), True, (0, 0, 0))
            window.blit(attack_num, (50, 100))

            self.mouse()
