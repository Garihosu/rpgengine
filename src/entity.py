"""
Base classes for entities.

contribs:
    - Noah Barger
"""

import pygame as pg

import consts

class Entity:
    """
Base class for an entity of any sort.
    """
    def __init__(self, name, x, y, surface):
        self.name = name
        
        self.x = x
        self.y = y

        # this is for other classes that may wish for movement
        self.dx = 0
        self.dy = 0

        self.surface = surface

    def update(self, delta):
        # TODO: collision
        self.x += self.dx
        self.y += self.dy

    def draw(self, scr):
        scr.blit(self.surface, (self.x, self.y))

class Player(Entity):
    """
Base class for a player entity.
    """
    def __init__(self, name="player", x=0, y=0):
        # the 32x32 red square is temporary currently until we get suitable sprites
        super().__init__(name, x, y, pg.Surface((32,32)))
        self.surface.fill("red")

    def update(self, delta, im):
        if im.up:
            self.dy = -consts.PLR_SPEED*delta
        if im.down:
            self.dy = consts.PLR_SPEED*delta
        if im.left:
            self.dx = -consts.PLR_SPEED*delta
        if im.right:
            self.dx = consts.PLR_SPEED*delta

        super().update(delta)

        self.dx = 0
        self.dy = 0
