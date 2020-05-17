from tkinter import *
import time
import Object3D
import numpy as np
from Cube import Cube
from Pyramid import Pyramid
from Icosahedron import Icosahedron


class Environment:
    def __init__(self, bgcolor, height, width):
        self.BACKGROUND = bgcolor
        self.HEIGHT = height
        self.WIDTH = width
        self.environment = []
        self.top = Tk()
        self.canvas = Canvas(self.top, bg=self.BACKGROUND, height=self.HEIGHT, width=self.WIDTH)
        self.top.bind("<B1-Motion>", self.mousedrag)
        self.canvas.pack()
        self.start_x = None
        self.start_y = None

    def rotateAll(self, matrix):
        for element in self.environment:
            element.rotate_helper(matrix)

    def mousedrag(self, event):
        if self.start_x is None and self.start_y is None:
            self.start_x = event.x
            self.start_y = event.y
        else:
            dx = (event.x - self.start_x)
            dy = (event.y - self.start_y)
            if dx > 1:
                self.environment[0].rotateYC()
                self.environment[1].rotateYC()

            elif dx < -1:
                self.environment[0].rotateY()
                self.environment[1].rotateY()

            if dy > 1:
                self.environment[0].rotateXC()
                self.environment[1].rotateXC()

            elif dy < -1:
                self.environment[0].rotateX()
                self.environment[1].rotateX()

            self.start_x = event.x
            self.start_y = event.y

    def add(self, name, *args):
        obj = None
        if name == "Cube":
            obj = Cube(*args)
        elif name == "Pyramid":
            obj = Pyramid(*args)
        self.environment.append(obj)
        return obj

    def render(self):
        self.canvas.delete(ALL)
        for element in self.environment:
            element.render(self.canvas)
        self.top.update()

