"""
Class for input manager.

contribs:
    - Noah Barger
"""

import pygame as pg

class InputManager:
    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def update(self, engine):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                engine.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.up = True
                if event.key == pg.K_DOWN:
                    self.down = True
                if event.key == pg.K_LEFT:
                    self.left = True
                if event.key == pg.K_RIGHT:
                    self.right = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.up = False
                if event.key == pg.K_DOWN:
                    self.down = False
                if event.key == pg.K_LEFT:
                    self.left = False
                if event.key == pg.K_RIGHT:
                    self.right = False

