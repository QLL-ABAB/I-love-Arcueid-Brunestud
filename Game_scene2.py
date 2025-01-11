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

class Mine_sweeping(Listener):
    def __init__(self, player):
        self.player = player
        self.mine_size = 100
        self.tile_size = 100
        self.length = 14  # 10x10的网格
        self.height = 9
        self.mine_number = 13  # 雷的数量
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.gray = (192, 192, 192)
        self.red = (255, 0, 0)
        self.revealed = [[False for _ in range(self.length)] for _ in range(self.height)]
        self.dict = {}
        for y in range(self.height):
            for x in range(self.length):
                self.dict[(x, y)] = 0
        self.board = create_board(self.length, self.height,  self.mine_number)
        self.game_close = False
        self.whether_begin_game = True
    def listen(self, event):
        key_game = pygame.key.get_pressed()
        #mouse_game = pygame.mouse.get_pressed()
        if self.game_close == True:
            self.mine_size = 100
            self.tile_size = 100
            self.length = 14  # 10x10的网格
            self.height = 9
            self.mine_number = 13  # 雷的数量
            self.black = (0, 0, 0)
            self.white = (255, 255, 255)
            self.gray = (192, 192, 192)
            self.red = (255, 0, 0)
            self.revealed = [[False for _ in range(self.length)] for _ in range(self.height)]
            self.dict = {}
            for y in range(self.height):
                for x in range(self.length):
                    self.dict[(x, y)] = 0
            self.board = create_board(self.length, self.height, self.mine_number)
            self.game_close = False
            self.whether_begin_game = True
            self.post(Event(Scene_Code.GAME2_OVER))
        if event.code == Event_Code.DRAW:

            if self.whether_begin_game == True:
                text_surface = font2.render("Press Space to Start", True, (0, 0, 0))
                #print(1)
                window.fill((255, 255, 255))
                window.blit(text_surface, (400, WindowSettings.height / 2))
                coin_num = font1.render(
                    "Coins: " + str(self.player.coin), True, (0, 0, 0)
                )
                window.blit(coin_num, (20, 20))
                pygame.display.flip()

        if self.whether_begin_game == True and key_game[pygame.K_SPACE]:
            self.whether_begin_game = False

        if  key_game[pygame.K_ESCAPE]:
            self.post(Event(Scene_Code.CITY))
            pygame.display.flip()
                
        if self.whether_begin_game == False:
            #print(2)
            window.fill((255, 255, 255))
            coin_num = font1.render("Coins: " + str(self.player.coin), True, (0, 0, 0))
            window.blit(coin_num, (20, 20))
            draw_board(self.board, self.revealed, self.dict)
            pt = 0
            for y in range(self.height):
                for x in range(self.length):
                    if self.board[y][x] == -1:
                        if self.revealed[y][x] and self.dict[(x, y)] == 2:
                            pt += 1
                    if self.board[y][x] != -1:
                        if self.revealed[y][x] and self.dict[(x, y)] == 1:
                            pt += 1
            if pt == 14*9:
                print("win")
                self.game_close = True
                self.player.coin += 30
            pygame.display.flip()
                


class Game2_Over(Listener):
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
            pygame.display.flip()
        elif keys[pygame.K_SPACE]:
            self.post(Event(Scene_Code.GAME_MINE_SWEEPING))
            pygame.display.flip()


def create_board(h1,h2, MINE_COUNT):
    board = [[0 for _ in range(h1)] for _ in range(h2)]
    mines = set()
    while len(mines) < MINE_COUNT:
        x, y = random.randint(0, h1 - 1), random.randint(0, h2 - 1)
        if (x, y) not in mines:
            mines.add((x, y))
            board[y][x] = -1
    for x, y in mines:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < h1 and 0 <= ny < h2 and board[ny][nx] != -1:
                    board[ny][nx] += 1
    return board


# 渲染函数
def draw_board(board, revealed, dict,h1 =14, h2 = 9, TILE_SIZE = 100, screen = window,RED= (255,0,0),GRAY = (192,192,192),WHITE = (255,255,255),BLACK = (0,0,0)):
    for y in range(h2):
        for x in range(h1):
            cell = board[y][x]
            if revealed[y][x]:
                if cell == -1 or dict[(x, y)] == 2:
                    pygame.draw.rect(
                        screen,
                        RED,
                        (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                    )
                else:
                    pygame.draw.rect(
                        screen,
                        GRAY,
                        (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                    )
                    if cell > 0:
                        font = pygame.font.Font(None, 36)
                        text = font.render(str(cell), True, BLACK)
                        screen.blit(text, (x * TILE_SIZE + 10, y * TILE_SIZE + 10))
            else:
                pygame.draw.rect(
                    screen, WHITE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                )
            pygame.draw.rect(
                screen, BLACK, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1
            )