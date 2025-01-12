from Game_manager import *
import pygame

pygame.init()

clock = pygame.time.Clock()

if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.bgm_player.update()
    while True:
        run_game(game_manager)
        pygame.display.flip()  # 缓冲绘制到屏幕上
        clock.tick(frame_rate1)  # 设置刷新频率

pygame.quit()
