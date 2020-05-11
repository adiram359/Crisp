from tkinter import *
import time
from Object3D import Object3D
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

    def rotateAll(self, dir):
        if dir == "X":
            for element in self.environment:
                element.rotateZ()
        elif dir == "X-":
            for element in self.environment:
                element.rotateZC()
        if dir == "Y":
            for element in self.environment:
                element.rotateY()
        elif dir == "Y-":
            for element in self.environment:
                element.rotateYC()

    def mousedrag(self, event):
        if self.start_x == None and self.start_y == None:
            self.start_x = event.x
            self.start_y = event.y
        else:
            dx = (event.x - self.start_x)
            dy = (event.y - self.start_y)
            if dx > 1:
                self.rotateAll("X")
            elif dx < -1:
                self.rotateAll("X-")
            if dy > 1:
                self.rotateAll("Y-")
            elif dy < -1:
                self.rotateAll("Y")
            self.start_x = event.x
            self.start_y = event.y

    def mousepressed(self, event):
        for element in self.environment:
            element.rotateZ()
        print("left pressed")

    def mousereleased(self, event):
        for element in self.environment:
            element.rotateY()

        # delta_x = abs(event.x - self.start_x)
        # delta_y = abs(event.y - self.start_y)
        # self.start_x, self.start_y = None, None
        #
        #
        #
        # if delta_x > 0:
        #     for i in range(0, delta_x, 10):
        #         for element in self.environment:
        #             element.rotateZ()
        # if delta_y > 0:
        #     for i in range(0, delta_y, 10):
        #         for element in self.environment:
        #             element.rotateY()
        print("up pressed")

    def add(self, name, *args):
        obj = None
        if name == "Cube":
            obj = Cube(*args)
        elif name == "Pyramid":
            obj = Pyramid(*args)
        self.environment.append(obj)

    def render(self):
        self.canvas.delete(ALL)
        for element in self.environment:
            element.render(self.canvas)
            #element.rotateZ()
            #element.rotateY()
            #element.rotateX()
        self.top.update()

