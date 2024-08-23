import json
import pygame
from random import randint
from utils import SpriteSheet


# Анимация
# Условие конца
# state отрисовки конца

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, entity, srite_file, flip=False):
        super().__init__()

        self.change_x = 0
        self.change_y = 0
        self.flip = flip
        data = self.read_json(entity)
        ss = SpriteSheet(f'assets/images/{srite_file}.png')

        self.standing = []
        for row in data['standing']:
            self.standing += self.append_img(ss.get_image(*row), flip=flip)

        self.appercot = []
        for row in data['appercot']:
            self.appercot += self.append_img(ss.get_image(*row), flip=flip)

        self.attack = False
        self.image = self.standing[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.stand_indx = 1
        self.appercot_indx = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit_cooldown = 0
        self.enemy = None

    def read_json(self, charachter):
        with open('animation.json', 'r') as f:
            data = json.load(f)
        data = data[charachter]
        return data

    def append_img(self, img, flip=False):
        lst = []
        img = pygame.transform.scale2x(img)
        if flip:
            img = pygame.transform.flip(img, True, False)
        for _ in range(3):
            lst.append(img)
        return lst

    def update(self):
        if not self.attack:
            self.image = self.standing[self.stand_indx % len(self.standing)]
            self.stand_indx += 1
        else:
            self.image = self.appercot[self.appercot_indx % len(self.appercot)]
            self.appercot_indx += 1
            if self.appercot_indx >= len(self.appercot):
                self.attack = False
                self.appercot_indx = 0

        if self.flip:
            if randint(0, 100) > 95:
                self.attack = True
            self.rect.x += randint(-6, 6)        
        else:
            self.rect.x += self.change_x
        
        if self.hit_cooldown:
            self.hit_cooldown -= 1

    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0

