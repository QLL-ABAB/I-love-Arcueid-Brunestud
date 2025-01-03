import pygame
from Settings import *
from Collections import *


class BgmPlayer(Listener):
    def __init__(self):
        pygame.mixer.init()

    def play(self, loop=-1):
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loop)

    def stop(self):
        pygame.mixer.music.stop()

    def update(self, event=Scene_Code.GAME_BEGIN):
        self.stop()
        if event == Scene_Code.GAME_BEGIN:
            pygame.mixer.music.load(Game_Path.bgm_path[0])
        elif event == Scene_Code.CITY:
            pygame.mixer.music.load(Game_Path.bgm_path[2])
        elif event == Scene_Code.FOREST:
            pygame.mixer.music.load(Game_Path.bgm_path[1])
        elif event == Scene_Code.GAME_OVER:
            pygame.mixer.music.load(Game_Path.bgm_path[3])
        elif event == Scene_Code.WIN:
            pygame.mixer.music.load(Game_Path.bgm_path[4])

        elif event == Scene_Code.BOSS:
            pygame.mixer.music.load(Game_Path.bgm_path[5])

        self.play()
