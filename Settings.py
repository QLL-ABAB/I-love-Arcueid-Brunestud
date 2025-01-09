from enum import Enum


class WindowSettings:
    name = "I LOVE Aruceid"
    width = 1400
    height = 900
    color = (0, 0, 0)


class SceneSettings:
    tile_size = 40  # 地图块的大小
    map_size = (1500, 1000)  # 地图的大小
    camara_0 = (0, 0)  # 镜头
    wlid_player_pos0 = (610, 330)  # 玩家的初始位置
    attribute_size = 20
    burn_attribute_size = (5, 15)
    portal_pos = [(1000, 350), (150, 350)]  # 传送门的位置
    portal_size = (200, 300)  # 传送门的大小
    portal_size2 = (150, 225)
    portal_speed = 0.2  # 传送门的冷却时间
    game_machine_pos = ((600, 450), (600, 150))
    game_machine_size = (84, 150)
    shop_pos = (100, 500)
    hotel_pos = (100, 300)


class TextSettings:
    Text = ["Let's have fun!", "Game Over!", "菜"]
    text_color = (255, 0, 0)
    font_size = 35
    font_size_plus = 80
    box_width = WindowSettings.width
    box_height = 200
    box_color = (0, 0, 0)


class Snake_Settings:
    snake_speed = 20
    snake_block_size = 20


class PlayerSettings:
    # Initial Player Settings
    player_Speed = 5
    player_width = 60
    player_height = 60
    player_hp = 10
    player_animation_speed = 0.2
    # 战斗设置
    player_attack = 3
    burn_speed = 2


class EnemySettings:
    # 以元组方式存在，代指两种敌人
    enemy_width = (60, 80)
    enemy_height = (60, 80)
    enemy_hp = 5
    # 战斗设置
    enemy_attack = 2
    enemy2_num = 3
    enemy1_num = 5


class BossSettings:
    boss_speed = 6
    boss_bullet_speed = 25
    boss_width = 200
    boss_height = 160
    boss_hp = 80
    boss_animation_speed = 0.2
    # 战斗设置
    boss_attack = 1
    wlid_boss_pos0 = (1100, 370)  # boss的初始位置
    boss_animation_speed = 1


class Fellow_Settings:
    fellow_speed = 1
    fellow_width = 40
    fellow_height = 40
    fellow_hp = 10
    fellow_bullet_speed = 5
    explode_size = 60


class Scene_Code(Enum):

    GAME_BEGIN = 1
    FOREST = 2
    BOSS = 3
    CITY = 4
    WIN = 5
    GAME_OVER = 6
    GAME_MINE_SWEEPING = 7
    GAME_GREEDY_SNAKE = 8
    SHOP = 9
    GAME1_OVER = 10
    GAME2_OVER = 11
    EXIT_SHOP = 12
    FIGHT1 = 13
    FIGHT2 = 14
    FRESH_ENEMY = 15


class Event_Code(Enum):
    CAN_MOVE = 1
    REQUEST_MOVE = 2
    STEP = 3
    DRAW = 4

    MOVE_ANIMATIOM = 5
    STAND_STILL = 6

    DIE = 7

    BURN = 8
    CHECK_FIRE = 9

    CHECK_PORTAL1 = 10
    CHECK_PORTAL2 = 11

    CHECK_ENEMY1 = 14

    CHECK_HP = 12

    BOSS_ANIMATIOM = 15
    BOSS_MOVE = 16
    BOSS_DIE = 17

    WORD1 = 21

    ENEMY_ATTACK = 22

    HURT = 23

    SHOOT_WATER = 24

    SMALL_DIE1 = 25
    SMALL_DIE2 = 25
    # WHETHER_TO_FIGHT_FALSE = 23


class Game_Path:

    tree_path = r".\assets\tiles\tree.png"
    wall_path = r".\assets\tiles\cityWall.png"
    word_path = f"assets/pop.ttf"
    coin_path = r".\assets\tiles\coin.png"
    shop_path = r".\assets\tiles\shop.png"
    hotel_path = r".\assets\tiles\hotel.png"
    fellow_path = [
        r".\assets\boss_room\boss_fellows\1.png",
        r".\assets\boss_room\boss_fellows\2.png",
    ]
    water_hole_path = r".\assets\tiles\water_hole.png"

    player_sword_light_path = r".\assets\boss_room\player_attack\sword_light.png"

    forest_tiles_path = [
        r".\assets\tiles\1.png",
        r".\assets\tiles\2.png",
        r".\assets\tiles\3.png",
        r".\assets\tiles\4.png",
        r".\assets\tiles\5.png",
        r".\assets\tiles\6.png",
        r".\assets\tiles\water.png",
    ]

    city_tiles_path = [
        r".\assets\tiles\city1.png",
        r".\assets\tiles\city2.png",
        r".\assets\tiles\city3.png",
        r".\assets\tiles\city4.png",
        r".\assets\tiles\city5.png",
        r".\assets\tiles\city6.png",
    ]

    player_run_path1 = [
        r".\assets\player\player1_stand.png",
        r".\assets\player\player1_run1.png",
        r".\assets\player\player1_run2.png",
        r".\assets\player\player1_run3.png",
        r".\assets\player\player1_run4.png",
        r".\assets\player\player1_run5.png",
        r".\assets\player\player1_run6.png",
        r".\assets\player\player1_run7.png",
        r".\assets\player\player1_run8.png",
    ]

    player_run_path2 = [
        r".\assets\player\player1_stand_inverse.png",
        r".\assets\player\player1_run9.png",
        r".\assets\player\player1_run10.png",
        r".\assets\player\player1_run11.png",
        r".\assets\player\player1_run12.png",
        r".\assets\player\player1_run13.png",
        r".\assets\player\player1_run14.png",
        r".\assets\player\player1_run15.png",
        r".\assets\player\player1_run16.png",
    ]

    player_die_path = r".\assets\player\player1_die.png"

    fire_path = [
        r".\assets\tiles\fire1.png",
        r".\assets\tiles\fire2.png",
    ]

    attribute_path = [
        r".\assets\player\hp.png",
        r".\assets\player\shield.png",
        r".\assets\player\burn.png",
        r".\assets\player\add_hp.png",
        r".\assets\player\proof_fire.png",
        r".\assets\player\add_attack.png",
        r".\assets\player\eat_blood.png",
        r".\assets\player\Aruceid.png",
        r".\assets\boss_room\alien\boss_blood.jpg",
        r".\assets\player\shop_exit.png",
        r".\assets\player\attack.png",
        r".\assets\enemy\enemy_hp.png",  # 11
        r".\assets\player\through.png",  # 12
        r".\assets\player\add_bullet_speed.png",  # 13
        r".\assets\player\skill.png",  # 14
        r".\assets\player\attack_harder.png",  # 15
        r".\assets\player\bottle.png",  # 16
        r".\assets\player\water_bottle.png",  # 17
        r".\assets\player\get_water.png",  # 18
        r".\assets\player\shoot.png",  # 19
        r".\assets\player\target.png",  # 20
        r".\assets\player\bg.png",  # 21
        r".\assets\player\energy.png",  # 22
        r".\assets\player\no_energy.png",  # 23
        r".\assets\player\hold_time.jpg",  # 24
    ]

    game_machine_path = r".\assets\tiles\game_machine.jpg"

    portal_path = [
        r".\assets\tiles\portal0.png",
        r".\assets\tiles\portal1.png",
        r".\assets\tiles\portal2.png",
        r".\assets\tiles\portal3.png",
        r".\assets\tiles\portal4.png",
        r".\assets\tiles\portal5.png",
        r".\assets\tiles\portal6.png",
        r".\assets\tiles\portal7.png",
    ]

    background_path = [
        r".\assets\background\bg_init.jpg",
        r".\assets\background\bg_end.png",
        r".\assets\background\bg_win.png",
        r".\assets\background\bg_shop.png",
        r".\assets\background\bg_fight.jpg",
    ]

    bgm_path = [
        r".\assets\bgm\game_begin.mp3",
        r".\assets\bgm\forest.mp3",
        r".\assets\bgm\city.mp3",
        r".\assets\bgm\game_end.mp3",
        r".\assets\bgm\win.mp3",
        r".\assets\bgm\boss.mp3",
    ]

    enemy_path = [
        r".\assets\enemy\enemy.png",
        r".\assets\enemy\great_enemy.png",
        r".\assets\enemy\enemy_inverse.png",
        r".\assets\enemy\great_enemy_inverse.png",
    ]

    boss_tiles_path = [
        r".\assets\boss_room\boss_tiles\1.png",
        r".\assets\boss_room\boss_tiles\2.png",
        r".\assets\boss_room\boss_tiles\3.png",
        r".\assets\boss_room\boss_tiles\4.png",
        r".\assets\boss_room\boss_tiles\5.png",
        r".\assets\boss_room\boss_tiles\6.png",
    ]

    boss_path = [
        r".\assets\boss_room\alien\alien infected idle_0.png",
        r".\assets\boss_room\alien\alien infected idle_1.png",
        r".\assets\boss_room\alien\alien infected idle_2.png",
        r".\assets\boss_room\alien\alien infected idle_3.png",
        r".\assets\boss_room\alien\alien infected idle_4.png",
        r".\assets\boss_room\alien\alien infected idle_5.png",
        r".\assets\boss_room\alien\alien infected idle_6.png",
        r".\assets\boss_room\alien\alien infected idle_7.png",
    ]

    bullet_path = [
        r".\assets\boss_room\zhidan\boss_bullet1.png",
        r".\assets\boss_room\zhidan\boss_bullet2.png",
        r".\assets\boss_room\zhidan\fellow_bullet.png",
        r".\assets\boss_room\zhidan\player_bullet.png",
    ]

    baozha_path = [
        r".\assets\boss_room\baozha\baozha11.png",
        r".\assets\boss_room\baozha\baozha12.png",
        r".\assets\boss_room\baozha\baozha13.png",
        r".\assets\boss_room\baozha\baozha14.png",
        r".\assets\boss_room\baozha\baozha15.png",
        r".\assets\boss_room\baozha\baozha16.png",
        r".\assets\boss_room\baozha\baozha17.png",
        r".\assets\boss_room\baozha\baozha18.png",
        r".\assets\boss_room\baozha\baozha19.png",
    ]

    close_attack = [
        r".\assets\boss_room\zhidan\boss_bullet\boss_shock\1.png",
        r".\assets\boss_room\zhidan\boss_bullet\boss_shock\2.png",
        r".\assets\boss_room\zhidan\boss_bullet\boss_shock\3.png",
        r".\assets\boss_room\zhidan\boss_bullet\boss_shock\4.png",
        r".\assets\boss_room\zhidan\boss_bullet\boss_shock\5.png",
        r".\assets\boss_room\zhidan\boss_bullet\boss_shock\6.png",
    ]

    explode_path = [
        r".\assets\boss_room\baozha\0.png",
        r".\assets\boss_room\baozha\1.png",
        r".\assets\boss_room\baozha\2.png",
        r".\assets\boss_room\baozha\3.png",
        r".\assets\boss_room\baozha\4.png",
        r".\assets\boss_room\baozha\5.png",
    ]


frame_rate1 = 60  # 游戏帧率
frame_rate_small_game = 5
