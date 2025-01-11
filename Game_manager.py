import pygame
import time
from Collections import *
from Settings import *
from Bgm_player import *
from Add_windows import *
from Shop import *
from Game_scene import *
from Player import *
from Scenes import *
from Boss_scene import Boss_Scene1
from Game_scene2 import * 


pygame.init()


class GameManager(Listener):
    def __init__(self):
        super().__init__()
        self.bgm_player = BgmPlayer()  # 第一次死亡标志

        self.mob = Player1(
            image=pygame.transform.scale(
                pygame.image.load(Game_Path.player_run_path1[0]),
                (PlayerSettings.player_width, PlayerSettings.player_height),
            ),
            rect=pygame.Rect(
                SceneSettings.wlid_player_pos0[0],
                SceneSettings.wlid_player_pos0[1],
                PlayerSettings.player_width,
                PlayerSettings.player_height,
            ),
        )

        self.scene_forest = Scene_Forest(self.mob)
        self.scene_beginning = Scene_Beginning()
        self.scene_city = Scene_City(self.mob)
        self.scene_ending = Scene_Ending()
        self.scene_boss = Boss_Scene1(self.mob)
        self.scene_win = Scene_Winning()
        self.scene_shop = Scene_Shop(self.mob)
        self.scene_greedy_snake = Greedy_snake(self.mob)
        self.scene_game1_over = Game1_Over(self.mob)
        self.scene_fight1 = Scene_Fight(self.mob, 1)
        self.scene_fight2 = Scene_Fight(self.mob, 2)
        self.judge_first_time = True
        self.scene_mine_sweeping = Mine_sweeping(self.mob)
        self.scene_game2_over = Game2_Over(self.mob)

        self.scenes = [
            self.scene_beginning,
            self.scene_forest,
            self.scene_city,
            self.scene_ending,
            self.scene_boss,
            self.scene_win,
            self.scene_shop,
            self.scene_greedy_snake,
            self.scene_game1_over,
            self.scene_fight1,
            self.scene_fight2,
            self.scene_mine_sweeping,
            self.scene_game2_over,
        ]
        self.scene = self.scenes[0]

    def listen(self, event: Event):  # 场景所监听的事件
        super().listen(event)

        if event.code == Scene_Code.GAME_BEGIN:
            self.scene = self.scenes[0]
            self.judge_first_time = True
            self.mob = Player1(
                image=pygame.transform.scale(
                    pygame.image.load(Game_Path.player_run_path1[0]),
                    (PlayerSettings.player_width, PlayerSettings.player_height),
                ),
                rect=pygame.Rect(
                    SceneSettings.wlid_player_pos0[0],
                    SceneSettings.wlid_player_pos0[1],
                    PlayerSettings.player_width,
                    PlayerSettings.player_height,
                ),
            )
            self.scene_forest = Scene_Forest(self.mob)
            self.scene_city = Scene_City(self.mob)
            self.scene_boss = Boss_Scene1(self.mob)
            self.scene_shop = Scene_Shop(self.mob)
            self.scene_fight1 = Scene_Fight(self.mob, 1)
            self.scene_fight2 = Scene_Fight(self.mob, 2)
            self.scenes = [
                self.scene_beginning,
                self.scene_forest,
                self.scene_city,
                self.scene_ending,
                self.scene_boss,
                self.scene_win,
                self.scene_shop,
                self.scene_greedy_snake,
                self.scene_game1_over,
                self.scene_fight1,
                self.scene_fight2,
                self.scene_mine_sweeping,
                self.scene_game2_over,
            ]

            self.bgm_player.update(Scene_Code.GAME_BEGIN)
            time.sleep(0.5)

        if event.code == Scene_Code.FOREST:
            self.scene = self.scenes[1]
            self.bgm_player.update(Scene_Code.FOREST)
            time.sleep(0.5)

        if event.code == Scene_Code.CITY:
            self.scene = self.scenes[2]
            self.bgm_player.update(Scene_Code.CITY)
            time.sleep(0.5)

        if event.code == Scene_Code.GAME_OVER:
            self.scene = self.scenes[3]  # 游戏结束场景
            self.bgm_player.update(Scene_Code.GAME_OVER)

        if event.code == Scene_Code.BOSS:
            self.scene = self.scenes[4]  # boss场景
            self.mob.boss = True
            self.bgm_player.update(Scene_Code.BOSS)
            time.sleep(0.5)

        if event.code == Scene_Code.WIN:
            self.scene = self.scenes[5]  # 胜利场景
            self.bgm_player.update(Scene_Code.WIN)
            time.sleep(0.5)

        if event.code == Scene_Code.SHOP:
            self.scene = self.scenes[6]  # 商店场景
            self.bgm_player.update(Scene_Code.SHOP)
            time.sleep(0.5)

        if event.code == Scene_Code.GAME_GREEDY_SNAKE:
            self.scene = self.scenes[7]  # 贪吃蛇场景
            time.sleep(0.5)

        if event.code == Scene_Code.GAME1_OVER:
            self.scene = self.scenes[8]  # 第1关结束场景
            time.sleep(0.2)

        if event.code == Scene_Code.FIGHT1:
            self.scene = self.scenes[9]
            time.sleep(0.5)

        if event.code == Scene_Code.FIGHT2:
            self.scene = self.scenes[10]
            time.sleep(0.5)

        if event.code == Scene_Code.GAME_MINE_SWEEPING:
            self.scene = self.scenes[11]  # 扫雷场景
            time.sleep(0)

        if event.code == Scene_Code.GAME2_OVER:
            self.scene = self.scenes[12]  # 第1关结束场景
            time.sleep(0)

        if event.code == Scene_Code.FRESH_ENEMY:
            self.scene_forest = Scene_Forest(self.mob)
            self.scenes = [
                self.scene_beginning,
                self.scene_forest,
                self.scene_city,
                self.scene_ending,
                self.scene_boss,
                self.scene_win,
                self.scene_shop,
                self.scene_greedy_snake,
                self.scene_game1_over,
                self.scene_fight1,
                self.scene_fight2,
                self.scene_mine_sweeping,
                self.scene_game2_over,
            ]
            time.sleep(0.5)
            # self.scene_forest = Scene_Forest(self.mob)
