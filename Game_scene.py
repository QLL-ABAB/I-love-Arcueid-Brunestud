import pygame
import random
import time

from Collections import *
from Settings import *
from Wild_scene_entityLike import *
from Portals import *
from City_scene_entityLike import *
from Add_windows import *

pygame.init()


class Greedy_snake(Listener):
    def __init__(self, player):
        self.player = player
        self.snake_block_size = Snake_Settings.snake_block_size
        self.snake_speed = Snake_Settings.snake_speed
        self.snake_list = []
        self.snake_length = 1
        self.snake_x = 700
        self.snake_y = 360
        # self.run_num = 0

        self.food_x = (
            round(
                random.randrange(0, WindowSettings.width - self.snake_block_size * 2)
                / 20
            )
            * 20
        )

        self.food_y = (
            round(
                random.randrange(0, WindowSettings.height - self.snake_block_size * 2)
                / 20
            )
            * 20
        )

        self.x_change = 0
        self.y_change = 0

        self.whether_begin_game = True
        self.game_close = False

    def listen(self, event):
        key_game = pygame.key.get_pressed()

        if self.game_close == True:
            self.snake_list = []
            self.snake_length = 1
            self.snake_x = 700
            self.snake_y = 360
            self.food_x = (
                round(
                    random.randrange(
                        0, WindowSettings.width - self.snake_block_size * 2
                    )
                    / 20
                )
                * 20
            )
            self.food_y = (
                round(
                    random.randrange(
                        0, WindowSettings.height - self.snake_block_size * 2
                    )
                    / 20
                )
                * 20
            )
            self.x_change = 0
            self.y_change = 0
            self.whether_begin_game = True
            self.game_close = False
            self.post(Event(Scene_Code.GAME1_OVER))

        if event.code == Event_Code.DRAW:

            if self.whether_begin_game == True:
                text_surface = font2.render("Press Space to Start", True, (0, 0, 0))

                window.fill((255, 255, 255))
                window.blit(text_surface, (400, WindowSettings.height / 2))
                coin_num = font1.render(
                    "Coins: " + str(self.player.coin), True, (0, 0, 0)
                )
                window.blit(coin_num, (20, 20))

        if self.whether_begin_game == True and key_game[pygame.K_SPACE]:
            self.whether_begin_game = False

        if self.whether_begin_game == False:

            window.fill((255, 255, 255))
            coin_num = font1.render("Coins: " + str(self.player.coin), True, (0, 0, 0))
            window.blit(coin_num, (20, 20))
            # self.run_num += 1

            # if self.run_num >= 20:
            #     self.run_num = 0
            self.snake_x += self.x_change
            self.snake_y += self.y_change

            if (
                self.snake_x >= WindowSettings.width
                or self.snake_x < 0
                or self.snake_y >= WindowSettings.height
                or self.snake_y < 0
            ):
                self.game_close = True

            pygame.draw.rect(
                window,
                (255, 0, 0),
                [
                    self.food_x,
                    self.food_y,
                    self.snake_block_size,
                    self.snake_block_size,
                ],
            )

            snake_head = []
            snake_head.append(self.snake_x)
            snake_head.append(self.snake_y)
            self.snake_list.append(snake_head)
            if len(self.snake_list) > self.snake_length:

                del self.snake_list[0]

            for x in self.snake_list[:-1]:
                if x == snake_head:
                    self.game_close = True

            for x in self.snake_list:
                pygame.draw.rect(
                    window,
                    (0, 255, 0),
                    [x[0], x[1], self.snake_block_size, self.snake_block_size],
                )

            pygame.display.update()

            if self.snake_x == self.food_x and self.snake_y == self.food_y:
                self.food_x = (
                    round(
                        random.randrange(
                            0, WindowSettings.width - self.snake_block_size * 2
                        )
                        / 20
                    )
                    * 20
                )
                self.food_y = (
                    round(
                        random.randrange(
                            0, WindowSettings.height - self.snake_block_size * 2
                        )
                        / 20
                    )
                    * 20
                )
                self.snake_length += 1
                print(self.snake_length)
                self.player.coin += 1

                pygame.time.Clock().tick(self.snake_speed)


class Game1_Over(Listener):
    def __init__(self, player):
        self.player = player

    def listen(self, event):
        text_surface0 = font2.render("PRESS ESC TO OUT", True, (0, 0, 0))
        text_surface1 = font2.render("STILL WANT TO PLAY?", True, (0, 0, 0))
        text_surface2 = font2.render("Press Space to Restart", True, (0, 0, 0))
        coin_num = font1.render("Coins: " + str(self.player.coin), True, (0, 0, 0))
        window.fill((255, 255, 255))
        window.blit(text_surface0, (400, WindowSettings.height / 2 - 150))
        window.blit(text_surface1, (400, WindowSettings.height / 2))
        window.blit(text_surface2, (400, WindowSettings.height / 2 + 150))
        window.blit(coin_num, (20, 20))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.post(Event(Scene_Code.CITY))
        elif keys[pygame.K_SPACE]:
            self.post(Event(Scene_Code.GAME_GREEDY_SNAKE))
