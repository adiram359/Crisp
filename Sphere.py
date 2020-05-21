import numpy as np
from Object3D import Object3D
from Face import Face


class Sphere(Object3D):
    def __init__(self, x, y, z, radius, display, color="white",outline="black"):
        super().__init__(x, y, z, display, color, outline)
        self.radius = radius
        self.faces = []
        self.name = "Sphere"

    def render(self, canvas):
        x, y, z = self.coordinates[0], self.coordinates[1], self.coordinates[2]
        canvas.create_oval(y - self.radius, z - self.radius, y + self.radius, z + self.radius, outline=self.color, fill=self.color)
