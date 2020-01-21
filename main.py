import pygame
import os
import sys
from cards_classes import *


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Board:
    # создание поля
    def __init__(self):
        self.width = 7
        self.height = 3
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size1 = int(width / 7)
        self.cell_size2 = int(height / 3)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size1, cell_size2):
        self.left = left
        self.top = top
        self.cell_size1 = cell_size1
        self.cell_size2 = cell_size2

    def render(self):
        color = pygame.Color('White')
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, color, (self.left + self.cell_size1 * j,
                                                 self.top + self.cell_size2 * i,
                                                 self.cell_size1, self.cell_size2), 1)


class Tower1:
    def __init__(self):
        self.width = 100
        self.height = Board().cell_size2 / 100 * 20
        self.left = 0
        self.top = (height / 3) - self.height

    def set_view(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def render(self):
        color = pygame.Color('Grey')
        pygame.draw.rect(screen, color, (Board().cell_size1 + self.left,
                                         Board().cell_size2 + self.top,
                                         self.width, self.height))

    def add_tower(self, count):
        self.height = Board().cell_size2 / 100 * (20 + count)


class Tower2:
    def __init__(self):
        self.width = 100
        self.height = Board().cell_size2 / 100 * 20
        self.left = 174
        self.top = (height / 3) - self.height

    def set_view(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def render(self):
        color = pygame.Color('Grey')
        pygame.draw.rect(screen, color, (Board().cell_size1 * 5 + self.left,
                                         Board().cell_size2 + self.top,
                                         self.width, self.height))

    def add_tower(self, count):
        self.height = Board().cell_size2 / 100 * (20 + count)


class Wall1:
    def __init__(self):
        self.width = 70
        self.height = Board().cell_size2 / 100 * 10
        self.left = 0
        self.top = (height / 3) - self.height

    def set_view(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def render(self):
        color = pygame.Color('Brown')
        pygame.draw.rect(screen, color, (Board().cell_size1 * 2 + self.left,
                                         Board().cell_size2 + self.top,
                                         self.width, self.height))

    def add_wall(self, count):
        self.height = Board().cell_size2 / 100 * (10 + count)


class Wall2:
    def __init__(self):
        self.width = 70
        self.height = Board().cell_size2 / 100 * 10
        self.left = 204
        self.top = (height / 3) - self.height

    def set_view(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def render(self):
        color = pygame.Color('Brown')
        pygame.draw.rect(screen, color, (Board().cell_size1 * 4 + self.left,
                                         Board().cell_size2 + self.top,
                                         self.width, self.height))

    def add_wall(self, count):
        self.height = Board().cell_size2 / 100 * (10 + count)


class Player1Information:
    def __init__(self):
        font = pygame.font.Font(None, 13)
        self.text_1 = font.render('Игрок 1', 1, pygame.Color('Black'))
        self.text_2 = font.render(f'Кирпичей: {Player1().bricks}   производится за ход: {Player1().bricks_per_turn}',
                                  1, pygame.Color('Black'))
        self.text_3 = font.render(f'магии: {Player1().magic}   производится за ход: {Player1().magic_per_turn}',
                                  1, pygame.Color('Black'))
        self.text_4 = font.render(f'рекрутов: {Player1().recruits}  производится за ход: {Player1().recruits_per_turn}',
                                  1, pygame.Color('Black'))
        self.text_5 = font.render(f'Высота башни: {Player1().tower}',
                                  1, pygame.Color('Black'))
        self.text_6 = font.render(f'Высота стены: {Player1().wall}',
                                  1, pygame.Color('Black'))

        self.text_x = 0
        self.text_y_1 = Board().cell_size2 + Board().cell_size2 / 7
        self.text_y_2 = Board().cell_size2 + Board().cell_size2 / 7 * 2
        self.text_y_3 = Board().cell_size2 + Board().cell_size2 / 7 * 3
        self.text_y_4 = Board().cell_size2 + Board().cell_size2 / 7 * 4
        self.text_y_5 = Board().cell_size2 + Board().cell_size2 / 7 * 5
        self.text_y_6 = Board().cell_size2 + Board().cell_size2 / 7 * 6


class Player2Information:
    def __init__(self):
        font = pygame.font.Font(None, 13)
        self.text_1 = font.render('Игрок 2', 1, pygame.Color('Black'))
        self.text_2 = font.render(f'Кирпичей: {Player2().bricks}   производится за ход: {Player2().bricks_per_turn}',
                                  1, pygame.Color('Black'))
        self.text_3 = font.render(f'магии: {Player2().magic}   производится за ход: {Player2().magic_per_turn}',
                                  1, pygame.Color('Black'))
        self.text_4 = font.render(f'рекрутов: {Player2().recruits}  производится за ход: {Player2().recruits_per_turn}',
                                  1, pygame.Color('Black'))
        self.text_5 = font.render(f'Высота башни: {Player2().tower}',
                                  1, pygame.Color('Black'))
        self.text_6 = font.render(f'Высота стены: {Player2().wall}',
                                  1, pygame.Color('Black'))

        self.text_x = Board().cell_size1 * 6
        self.text_y_1 = Board().cell_size2 + Board().cell_size2 / 7
        self.text_y_2 = Board().cell_size2 + Board().cell_size2 / 7 * 2
        self.text_y_3 = Board().cell_size2 + Board().cell_size2 / 7 * 3
        self.text_y_4 = Board().cell_size2 + Board().cell_size2 / 7 * 4
        self.text_y_5 = Board().cell_size2 + Board().cell_size2 / 7 * 5
        self.text_y_6 = Board().cell_size2 + Board().cell_size2 / 7 * 6


pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.flip()
board = Board()
tower1 = Tower1()
tower2 = Tower2()
wall1 = Wall1()
wall2 = Wall2()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 100, 10))
    board.render()
    tower1.render()
    tower2.render()
    wall1.render()
    wall2.render()
    pygame.display.flip()
pygame.quit()


