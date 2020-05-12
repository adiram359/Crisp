import Object3D
import numpy as np
from Face import Face
import math


class Pyramid(Object3D.Object3D):
    def __init__(self, x, y, z, length, height, num_sides):
        super().__init__(x, y, z)
        self.length = length
        self.height = height
        self.radius = length / math.cos(math.pi / num_sides)
        self.num_sides = num_sides
        self.name = "Pyramid"
        self.faces = []
        self.create_faces(self.height, self.radius, self.num_sides)

    def create_faces(self, height, radius, num_sides):
        base = []
        for i in range(num_sides):
            base.append(np.array([radius * math.cos(2 * math.pi / num_sides * i),
                                  radius * math.sin(2 * math.pi / num_sides * i),
                                  0]))

        self.faces.append(Face(base[:]))

        for i in range(len(base)):
            f = [base[i], base[(i + 1) % num_sides], np.array([0, 0, -height])]
            self.faces.append(Face(f))
