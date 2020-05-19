import numpy as np
from Object3D import Object3D
from Face import Face


class Sphere(Object3D):
    def __init__(self, x, y, z, radius, display, color="white"):
        super().__init__(x, y, z, display, color)
        self.radius = radius
        self.faces = []

    def render(self, canvas):
        x, y, z = self.coordinates[0], self.coordinates[1], self.coordinates[2]
        canvas.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius, outline="black", fill=self.color)
