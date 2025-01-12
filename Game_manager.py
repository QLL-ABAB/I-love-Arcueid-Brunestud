import pygame
import time
from Collections import *
from Bgm_player import *
from Add_windows import *
from Shop import *
from Game_scene import *
from Game_scene2 import *
from Player import *
from Scenes import *
from Boss_scene import Boss_Scene1
from Game_scene2 import *
from Restart import *
from Settings import *


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
        self.scene_beginning = Scene_Beginning(self.mob)
        self.scene_city = Scene_City(self.mob)
        self.scene_ending = Scene_Ending(self.mob)
        self.scene_boss = Boss_Scene1(self.mob)
        self.scene_win = Scene_Winning(self.mob)
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
            self.scene_beginning = Scene_Beginning(self.mob)
            self.scene_forest = Scene_Forest(self.mob)
            self.scene_city = Scene_City(self.mob)
            self.scene_boss = Boss_Scene1(self.mob)
            self.scene_shop = Scene_Shop(self.mob)
            self.scene_fight1 = Scene_Fight(self.mob, 1)
            self.scene_fight2 = Scene_Fight(self.mob, 2)
            self.scene_mine_sweeping = Mine_sweeping(self.mob)
            self.scene_greedy_snake = Greedy_snake(self.mob)
            self.scene_game1_over = Game1_Over(self.mob)
            self.scene_game2_over = Game2_Over(self.mob)
            self.scene_ending = Scene_Ending(self.mob)
            self.scene_win = Scene_Winning(self.mob)
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
            self.judge_first_time = True

            self.bgm_player.update(Scene_Code.GAME_BEGIN)
            time.sleep(0.5)

        if event.code == Scene_Code.FOREST:
            self.scene = self.scenes[1]
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


def run_game(game_manager: GameManager):
    window.fill(WindowSettings.color)

    event_get = pygame.event.get()
    keys = pygame.key.get_pressed()

    for event in event_get:  # 将pygame默认事件如键盘等转换到自己的队列中
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        else:
            add_event(Event(event.type))
    add_event(Event(pygame.KEYDOWN))
    add_event(Event(Event_Code.STEP))  # 在while循环中，每轮都添加周期事件STEP
    add_event(Event(Event_Code.DRAW))  # 在while循环中，每轮都添加描绘事件DRAW
    add_event(
        Event(Event_Code.CHECK_FIRE)
    )  # 在while循环中，每轮都添加检查火焰事件CHECK_FIRE

    if game_manager.scene == game_manager.scene_forest:
        add_event(Event(Event_Code.CHECK_PORTAL1))
        add_event(Event(Event_Code.CHECK_ENEMY1))

    if game_manager.scene == game_manager.scene_city:
        add_event(Event(Event_Code.CHECK_PORTAL2))

    if game_manager.scene == game_manager.scene_boss:
        add_event(Event(Event_Code.BOSS_ANIMATIOM))

    if game_manager.scene == game_manager.scene_greedy_snake:
        for event in event_get:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if (
                        game_manager.scene_greedy_snake.x_change
                        != game_manager.scene_greedy_snake.snake_block_size
                    ):
                        game_manager.scene_greedy_snake.x_change = (
                            -game_manager.scene_greedy_snake.snake_block_size
                        )
                        game_manager.scene_greedy_snake.y_change = 0

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if (
                        game_manager.scene_greedy_snake.x_change
                        != -game_manager.scene_greedy_snake.snake_block_size
                    ):
                        game_manager.scene_greedy_snake.x_change = (
                            game_manager.scene_greedy_snake.snake_block_size
                        )
                        game_manager.scene_greedy_snake.y_change = 0

                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if (
                        game_manager.scene_greedy_snake.y_change
                        != game_manager.scene_greedy_snake.snake_block_size
                    ):
                        game_manager.scene_greedy_snake.y_change = (
                            -game_manager.scene_greedy_snake.snake_block_size
                        )
                        game_manager.scene_greedy_snake.x_change = 0

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if (
                        game_manager.scene_greedy_snake.y_change
                        != -game_manager.scene_greedy_snake.snake_block_size
                    ):
                        game_manager.scene_greedy_snake.y_change = (
                            game_manager.scene_greedy_snake.snake_block_size
                        )
                        game_manager.scene_greedy_snake.x_change = 0

                elif event.key == pygame.K_ESCAPE:
                    game_manager.scene_greedy_snake.game_close = True

    if game_manager.scene == game_manager.scene_mine_sweeping:
        for event in event_get:
            if event.type == MOUSEBUTTONDOWN:
                x, y = (
                    event.pos[0] // game_manager.scene_mine_sweeping.tile_size,
                    event.pos[1] // game_manager.scene_mine_sweeping.tile_size,
                )
                if event.button == 1:  # 左键点击
                    if game_manager.scene_mine_sweeping.board[y][x] == -1:
                        game_manager.scene_mine_sweeping.game_close = True
                    else:
                        game_manager.scene_mine_sweeping.revealed[y][x] = True
                        game_manager.scene_mine_sweeping.dict[(x, y)] = (
                            1  # 记录已经打开的格子
                        )
                elif event.button == 3:  # 右键点击
                    if (
                        (x, y) in game_manager.scene_mine_sweeping.dict
                        and game_manager.scene_mine_sweeping.dict[(x, y)] != 1
                    ):
                        game_manager.scene_mine_sweeping.dict[(x, y)] = (
                            2  # 记录已经标记的格子
                        )
                        game_manager.scene_mine_sweeping.revealed[y][
                            x
                        ] = not game_manager.scene_mine_sweeping.revealed[y][
                            x
                        ]  # 翻转格子
                    elif (
                        (x, y) in game_manager.scene_mine_sweeping.dict
                        and game_manager.scene_mine_sweeping.dict[(x, y)] == 1
                    ):
                        pass

        if (
            game_manager.scene_mine_sweeping.whether_begin_game == True
            and keys[pygame.K_SPACE]
        ):
            game_manager.scene_mine_sweeping.whether_begin_game = False

        if keys[pygame.K_ESCAPE]:
            add_event(Event(Scene_Code.CITY))
            pygame.display.flip()

    if game_manager.scene == game_manager.scene_game1_over:
        for event in event_get:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    add_event(Event(Scene_Code.CITY))
                if event.key == pygame.K_SPACE:
                    add_event(Event(Scene_Code.GAME_GREEDY_SNAKE))

    if game_manager.scene == game_manager.scene_game2_over:
        for event in event_get:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    add_event(Event(Scene_Code.CITY))
                if event.key == pygame.K_SPACE:
                    add_event(Event(Scene_Code.GAME_GREEDY_SNAKE))
    """
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    """

    keys = pygame.key.get_pressed()

    if (
        keys[pygame.K_q]
        and game_manager.scene == game_manager.scene_beginning
        and game_manager.scene_beginning.choose_saver_over
    ):
        game_manager.scene_beginning.choose_saver_over = False
        game_manager.scene_beginning.show_choose = True
        add_event(Event(Scene_Code.FOREST))
    if game_manager.mob.hp < 0 and game_manager.judge_first_time:
        game_manager.judge_first_time = False
        time.sleep(1)
        add_event(Event(Scene_Code.GAME_OVER))

    if game_manager.mob.hp == 0 and game_manager.scene == game_manager.scene_boss:
        time.sleep(1)
        add_event(Event(Scene_Code.GAME_OVER))

    if (
        game_manager.scene_boss.boss.hp <= 0
        and game_manager.scene == game_manager.scene_boss
    ):
        add_event(Event(Event_Code.BOSS_DIE))

    """
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    """

    while event_queue:  # 依次将事件队列中的事件取出并处理

        event = event_queue.pop(0)  # 取出一个事件

        game_manager.listen(event)  # 调用场景管理器的listen方法来尝试对该事件进行响应

        game_manager.mob.listen(event)
        game_manager.scene.listen(event)  # 调用场景的listen方法来尝试对该事件进行响应

        if game_manager.scene == game_manager.scene_boss:
            game_manager.scene.boss.listen(event)

    if game_manager.scene == game_manager.scene_shop:
        game_manager.scene_shop.word_window(
            game_manager.scene_shop.word_window_judge, event_get
        )
