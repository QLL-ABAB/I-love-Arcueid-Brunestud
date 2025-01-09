from Settings import *
from Collections import *
from Player import *
from Scenes import *
from Game_manager import *
from Add_windows import *
import pygame


pygame.init()

clock = pygame.time.Clock()

running = True

if __name__ == "__main__":

    game_manager = GameManager()

    game_manager.bgm_player.update()
    while True:
        window.fill(WindowSettings.color)

        event_get = pygame.event.get()

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
            # add_event(Event(Event_Code.CHECK_PORTAL3))
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

        if game_manager.scene == game_manager.scene_game1_over:
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
        if keys[pygame.K_q] and game_manager.scene == game_manager.scene_beginning:
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

            game_manager.listen(
                event
            )  # 调用场景管理器的listen方法来尝试对该事件进行响应

            game_manager.mob.listen(event)
            game_manager.scene.listen(
                event
            )  # 调用场景的listen方法来尝试对该事件进行响应

            if game_manager.scene == game_manager.scene_boss:
                game_manager.scene.boss.listen(event)

        if game_manager.scene == game_manager.scene_shop:
            game_manager.scene_shop.word_window(
                game_manager.scene_shop.word_window_judge, event_get
            )

        pygame.display.flip()  # 缓冲绘制到屏幕上

        clock.tick(frame_rate1)  # 设置刷新频率

pygame.quit()
