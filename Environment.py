from tkinter import *
import math



class Environment:
    def __init__(self, bgcolor, height, width):
        self.all_objects = []
        self.top = Tk()
        self.canvas = Canvas(self.top, bg=bgcolor, height=height, width=width)
        self.top.bind("<B1-Motion>", self.mousedrag)
        self.canvas.pack()
        self.start_x = None
        self.start_y = None

    def add(self, obj):
        self.all_objects.append(obj)

    def render(self):
        k = lambda obj: obj.coordinates[2]
        self.all_objects.sort(key=k)
        self.canvas.delete(ALL)
        for element in self.all_objects:
            element.render(self.canvas)
        self.top.update()

    def rotate_all_x(self, theta):
        for element in self.all_objects:
            element.rotate_x(theta)

    def rotate_all_y(self, theta):
        for element in self.all_objects:
            element.rotate_y(theta)

    def rotate_all_z(self, theta):
        for element in self.all_objects:
            element.rotate_z(theta)

    def mousedrag(self, event):
        if self.start_x is None and self.start_y is None:
            self.start_x = event.x
            self.start_y = event.y
        else:
            dx = (event.x - self.start_x)
            dy = (event.y - self.start_y)
            theta = math.pi/32 if dx > 0 else -math.pi/64
            if abs(dx) > 1:
                self.rotate_all_z(theta)
            theta = -math.pi/32 if dy > 0 else math.pi/64
            if abs(dy) > 1:
                self.rotate_all_y(theta)
            self.start_x = event.x
            self.start_y = event.y
