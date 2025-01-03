import pygame
import random
from Boss_and_fellows import *
from Collections import *
from Settings import *
from Portals import *
from Boss_scene_entityLike import *
from Add_windows import *
from Player import *
from Boss_and_fellows import Boss1

pygame.init()


class Boss_Scene1(Listener):
    def __init__(self, player):
        super().__init__()
        self.boss = Boss1(None, None)
        self.tiles = []
        self.hp_showings = []
        self.walls = []
        self.walls_collision = []
        self.player = player
        self.image = self.boss.image
        self.rect = self.boss.rect
        self.window_scale = (
            WindowSettings.width,
            WindowSettings.height,
        )
        self.attribute_size = SceneSettings.attribute_size  # 属性显示的大小
        self.blood_showings = []
        self.skills = []
        self.first_add1 = True
        self.first_add2 = True
        self.first_add3 = True
        self.first_add4 = True

        self.attack_showing = Attribute_showing(
            10, pygame.Rect(40, 120, self.attribute_size * 2, self.attribute_size * 2)
        )

        self.blood_eat = Attribute_showing(
            6, pygame.Rect(10, 140, self.attribute_size * 2, self.attribute_size * 2)
        )
        self.skill = Attribute_showing(
            14, pygame.Rect(10, 140, self.attribute_size * 2, self.attribute_size * 2)
        )
        self.through = Attribute_showing(
            12, pygame.Rect(10, 140, self.attribute_size * 2, self.attribute_size * 2)
        )
        self.add_bullet_speed = Attribute_showing(
            13, pygame.Rect(10, 140, self.attribute_size * 2, self.attribute_size * 2)
        )

        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """

        for i in range(self.window_scale[0] // 40 + 1):
            for j in range(self.window_scale[1] // 40 + 1):
                self.tiles.append(
                    Boss_Tile(random.randint(0, 5), pygame.Rect(i * 40, j * 40, 40, 40))
                )

        for i in range(21):
            hp = Attribute_showing(
                0,
                pygame.Rect(i * 25 + 40, 80, self.attribute_size, self.attribute_size),
            )
            self.hp_showings.append(hp)

        for i in range(5):
            wall = Shelt(pygame.Rect(500, 120 + i * 40, 40, 40))
            self.walls_collision.append(wall)

        for i in range(5):
            wall = Shelt(pygame.Rect(500, 500 + i * 40, 40, 40))
            self.walls_collision.append(wall)

        for i in range(self.window_scale[0] // 40 + 1):
            self.walls.append(Shelt(pygame.Rect(i * 40, 0, 40, 40)))

        for i in range(self.window_scale[0] // 40 + 1):
            self.walls.append(Shelt(pygame.Rect(i * 40, 880, 40, 40)))

        for j in range(self.window_scale[1] // 40 + 1):
            self.walls_collision.append(Shelt(pygame.Rect(0, j * 40, 40, 40)))

        for j in range(self.window_scale[1] // 40 + 1):
            self.walls.append(Shelt(pygame.Rect(1360, j * 40, 40, 40)))

        for i in range(41):
            blood = Attribute_showing(
                8,
                pygame.Rect(i * 18 + 300, 30, 18, 40),
            )
            self.blood_showings.append(blood)
        """
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """

    def listen(self, event: Event):  # 场景所监听的事件
        super().listen(event)

        keys = pygame.key.get_pressed()

        if event.code == Event_Code.REQUEST_MOVE:  # 监听玩家的移动请求事件
            can_move = 1
            target_rect = pygame.Rect(
                event.body["POS"][0],
                event.body["POS"][1],
                self.player.width,
                self.player.height,
            )
            for wall in self.walls:
                if wall.rect.colliderect(target_rect):
                    can_move = 0
                    break

            for wall in self.walls_collision:
                if wall.rect.colliderect(target_rect):
                    can_move = 0
                    break

            if can_move:
                self.post(Event(Event_Code.CAN_MOVE, event.body))

            """
            》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》
            """
            for bullet in self.boss.boss_bullets:
                if bullet.rect.colliderect(self.player.rect):
                    if self.player.hp > 0:
                        self.player.hp -= 1
                        self.post(Event(Event_Code.HURT))
                        bullet.kill()
                    # if self.player.hp <= 0:
                    #     self.post(Event(Event_Code.DIE))
                    #     self.post(Event(Event_Code.DRAW))

                for wall in self.walls_collision:
                    if bullet.rect.colliderect(wall.rect):
                        bullet.kill()

            for bullet in self.boss.boss_bullets1:
                if bullet.rect.colliderect(self.player.rect):
                    if self.player.hp > 0:
                        self.player.hp -= 2
                        self.post(Event(Event_Code.HURT))
                        bullet.kill()
                    # if self.player.hp <= 0:
                    #     self.player.image = pygame.transform.scale(
                    #         pygame.image.load(Game_Path.player_die_path),
                    #         (self.player.width, self.player.height),
                    #     )
                    #     self.post(Event(Event_Code.DIE))
                    #     self.post(Event(Event_Code.DRAW))

            """
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            """
            if self.boss.hp > 0:
                for bullet in self.player.player_bullets:
                    if not self.player.through:
                        for wall in self.walls_collision:
                            if bullet.rect.colliderect(wall.rect):
                                bullet.kill()

                    if bullet.rect.colliderect(self.boss.rect):
                        self.boss.hp -= self.player.attack
                        bullet.kill()
                        if self.player.blood_eat:
                            a = random.randint(0, 8)
                            if a == 1 and self.player.hp < 20:
                                self.player.hp += 1

            """
            >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            """

        if event.code == Event_Code.DRAW:  # DRAW事件，用于描绘场景中的实体

            for tile in self.tiles:  # 遍历所有地图背景图块并描绘
                tile.draw()

            window.blit(self.player.image, self.player.rect)  # 描绘玩家图像

            for i in range(self.player.hp):
                hp = self.hp_showings[i]
                window.blit(hp.image, hp.rect)

            for wall in self.walls:  # 遍历所有墙并描绘
                wall.draw()

            for wall in self.walls_collision:  # 遍历所有墙并描绘
                wall.draw()

            for i in range(self.boss.hp):
                blood = self.blood_showings[i]
                window.blit(blood.image, blood.rect)

            window.blit(self.attack_showing.image, self.attack_showing.rect)
            attack_num = font1.render(str(self.player.attack), True, (255, 255, 255))
            window.blit(attack_num, (85, 120))

            if self.player.skill == True and self.first_add1 == True:
                self.skills.append(self.skill)
                self.first_add1 = False
            if self.player.through == True and self.first_add2 == True:
                self.skills.append(self.through)
                self.first_add2 = False
            if self.player.add_bullet_speed == True and self.first_add3 == True:
                self.skills.append(self.add_bullet_speed)
                self.first_add3 = False
            if self.player.blood_eat == True and self.first_add4 == True:
                self.skills.append(self.blood_eat)
                self.first_add4 = False

            for i in range(len(self.skills)):
                window.blit(
                    pygame.transform.scale(
                        self.skills[i].image,
                        (self.attribute_size * 2, self.attribute_size * 2),
                    ),
                    pygame.Rect(
                        40 + i * 50,
                        200,
                        self.attribute_size * 2,
                        self.attribute_size * 2,
                    ),
                )

            self.boss.draw()
            for bullet in self.player.player_bullets:  # 遍历所有玩家子弹并描绘
                bullet.update()
                bullet.draw()
