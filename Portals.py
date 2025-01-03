import pygame
import time

from Collections import *

from Settings import *


class Portals(EntityLike):
    def __init__(self, speed, type):
        self.speed = speed
        self.image = pygame.image.load(Game_Path.portal_path[0])
        self.rect = pygame.Rect(
            SceneSettings.portal_pos[type][0],
            SceneSettings.portal_pos[type][1],
            SceneSettings.portal_size[0],
            SceneSettings.portal_size[1],
        )
        self.num_portal = 0

    def update(self):
        self.num_portal += self.speed
        if self.num_portal >= 7:
            self.num_portal = 0
        self.image = pygame.transform.scale(
            pygame.image.load(Game_Path.portal_path[int(self.num_portal)]),
            (SceneSettings.portal_size[0], SceneSettings.portal_size[1]),
        )
