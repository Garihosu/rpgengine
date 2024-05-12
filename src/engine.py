"""
The core engine.

contribs:
 - Noah Barger
"""

import pygame as pg

from input_manager import InputManager
from entity import Player

import consts

class Engine:
    def __init__(self):
        pg.init()

        self.scr = pg.display.set_mode((consts.SCR_WIDTH, consts.SCR_HEIGHT))
        pg.display.set_caption(consts.WINDOW_TITLE)

        self.clock = pg.time.Clock()

        self.delta = 0

        self.im = InputManager()

        self.entities = [Player(x=0, y=0)]

        self.running = False

    def update(self):
        self.im.update(self)

        for entity in self.entities:
            if type(entity) == Player:
                entity.update(self.delta, self.im)
            else:
                entity.update(self.delta)

    def draw(self):
        self.scr.fill("black")

        for entity in self.entities:
            entity.draw(self.scr)

        pg.display.flip()

    def run(self):
        self.running = True

        while self.running:
            self.update()
            self.draw()

            self.delta = self.clock.tick(consts.FPS) / 1000

        pg.quit()
