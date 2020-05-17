import Object3D
import numpy as np
from Face import Face
import math


class Pyramid(Object3D.Object3D):
    def __init__(self, x, y, z, length, height, num_sides, display="block"):
        super().__init__(x, y, z)
        self.display = display
        self.length = length
        self.height = height
        self.radius = length / math.cos(math.pi / num_sides)
        self.num_sides = num_sides
        self.name = "Pyramid"
        self.faces = []
        self.create_faces(self.height, self.radius, self.num_sides)



    def create_faces(self, height, radius, num_sides):
        x_bumper, y_bumper, z_bumper = self.bumpers()
        base = []
        for i in range(num_sides):
            base.append(np.array([x_bumper + radius * math.cos(2 * math.pi / num_sides * i),
                                  y_bumper + radius * math.sin(2 * math.pi / num_sides * i),
                                  z_bumper + 0]))

        self.faces.append(Face(base[:]))

        for i in range(len(base)):
            f = [base[i], base[(i + 1) % num_sides], np.array([x_bumper + 0, y_bumper + 0, z_bumper + -height])]
            self.faces.append(Face(f))
