import pygame
import sys
import random
from pygame.locals import *
import subprocess

# 游戏常量
MINE_SIZE = 30
TILE_SIZE = 30
GRID_SIZE = 10  # 10x10的网格
MINE_COUNT = 10  # 雷的数量

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 初始化pygame
pygame.init()
screen = pygame.display.set_mode((GRID_SIZE * TILE_SIZE, GRID_SIZE * TILE_SIZE))
pygame.display.set_caption("扫雷游戏")


# 创建游戏板
def create_board():
    board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    mines = set()
    while len(mines) < MINE_COUNT:
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if (x, y) not in mines:
            mines.add((x, y))
            board[y][x] = -1
    for x, y in mines:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and board[ny][nx] != -1:
                    board[ny][nx] += 1
    return board


# 渲染函数
def draw_board(board, revealed, dict):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
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


# 主函数
def main():
    board = create_board()
    revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    running = True
    dict = {}
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            dict[(x, y)] = 0  # 记录已经打开的格子
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                with open("coins.txt", "a") as f:
                    f.write("0\n")
                subprocess.Popen(["python", "Main.py"])
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                x, y = event.pos[0] // TILE_SIZE, event.pos[1] // TILE_SIZE
                if event.button == 1:  # 左键点击
                    if board[y][x] == -1:
                        print("Game Over!")
                        with open("coins.txt", "a") as f:
                            f.write("0\n")
                        subprocess.Popen(["python", "Main.py"])
                        running = False
                    else:
                        revealed[y][x] = True
                        dict[(x, y)] = 1  # 记录已经打开的格子
                elif event.button == 3:  # 右键点击
                    if (x, y) in dict and dict[(x, y)] != 1:
                        dict[(x, y)] = 2  # 记录已经标记的格子
                        revealed[y][x] = not revealed[y][x]  # 翻转格子
                    elif (x, y) in dict and dict[(x, y)] == 1:
                        pass
        draw_board(board, revealed, dict)
        pt = 0
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if board[y][x] == -1:
                    if revealed[y][x] and dict[(x, y)] == 2:
                        pt += 1
                if board[y][x] != -1:
                    if revealed[y][x] and dict[(x, y)] == 1:
                        pt += 1
        if pt == 100:
            print("Congratulations! You win!")
            with open("coins.txt", "a") as f:
                f.write("20\n")
            subprocess.Popen(["python", "Main.py"])
            running = False
        pygame.display.flip()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
