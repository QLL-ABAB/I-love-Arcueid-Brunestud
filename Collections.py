import pygame
from Settings import *

pygame.init()


window = pygame.display.set_mode((WindowSettings.width, WindowSettings.height))

event_queue = []  # 全局事件队列


def add_event(event):  # 向事件队列中添加事件
    global event_queue
    event_queue.append(event)


class Event:  # 定义事件类，属性包括用于区分事件种类的编号，以及可选参数body传递一些信息
    def __init__(self, code: int, body={}):
        self.code = code
        self.body = body


class Listener(pygame.sprite.Sprite):  # 定义监听者类，该类可以响应事件以及发送新的事件
    def __init__(self):
        super().__init__()

    def post(self, event: Event):
        add_event(event)

    def listen(self, event: Event): ...


class EntityLike(Listener):  # 实体类
    def __init__(self, image: pygame.Surface, rect: pygame.Rect):
        # 两个属性代表显示的图片路径、显示的矩形的位置和大小
        self.image = image
        self.rect = rect

    def listen(self, event: Event): ...

    def draw(self, camera: tuple[int, int]):
        rect = self.rect.move(*(-i for i in camera))
        window.blit(self.image, rect)


class Compute_tuple:
    def tuple_sub(a, b):
        return (a[0] - b[0], a[1] - b[1])

    def tuple_mul(a, b):
        return (a[0] * b, a[1] * b)

    def tuple_min(a, b):
        return (min(a[0], b[0]), min(a[1], b[1]))

    def tuple_max(a, b):
        return (max(a[0], b[0]), max(a[1], b[1]))


class Attribute_showing:
    def __init__(self, type, rect: pygame.Rect):
        self.image = pygame.image.load(Game_Path.attribute_path[type])
        self.rect = rect
        self.type = type


def change_color(image, R, G, B):

    for x in range(image.get_width()):
        for y in range(image.get_height()):
            r0, g0, b0, a0 = image.get_at((x, y))
            r1 = min(r0 * R, 255)
            g1 = min(g0 * G, 255)
            b1 = min(b0 * B, 255)

            image.set_at(((x, y)), (r1, g1, b1, 255))

    return image


def fellow_change_color(image, R, G, B):

    for x in range(image.get_width()):
        for y in range(image.get_height()):
            r0, g0, b0, a0 = image.get_at((x, y))
            if r0 != 0 and g0 != 0 and b0 != 0:
                r1 = min(r0 + R, 255)
                g1 = min(g0 + G, 255)
                b1 = min(b0 + B, 255)
            else:
                r1 = 0
                g1 = 0
                b1 = 0
            image.set_at(((x, y)), (r1, g1, b1, 255))

    return image


class Fixed_object(Listener):
    def __init__(self, image: pygame.Surface, rect: pygame.Rect):
        # 两个属性代表显示的图片路径、显示的矩形的位置和大小
        self.image = image
        self.rect = rect

    def listen(self, event: Event): ...

    def draw(self):
        window.blit(self.image, self.rect)
