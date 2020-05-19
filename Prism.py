import Object3D
import numpy as np
from Face import Face
import math


class Prism(Object3D.Object3D):
    def __init__(self, x, y, z, length, height, num_sides, display, color="white",outline="black"):
        super().__init__(x, y, z, display, color, outline)
        self.length = length
        self.height = height
        self.radius = length / math.cos(math.pi / num_sides)
        self.num_sides = num_sides
        self.faces = []
        self.name = "Prism"
        self.create_faces()
        self.rotate_in_place_z(math.pi/4)
        # self.rotate_x(math.pi/2)
        #self.rotate_y(math.pi/num_sides)

    def create_faces(self):
        base = self.create_base(0)
        self.faces.append(Face(base))
        base = self.create_base(self.height)
        self.faces.append(Face(base))

        assert len(self.faces[0].vertices) == len(self.faces[1].vertices)
        l = len(self.faces[0].vertices)
        for i in range(l):
            v1 = self.faces[0].vertices[i]
            v2 = self.faces[1].vertices[i]
            v3 = self.faces[0].vertices[(i + 1) % l]
            v4 = self.faces[1].vertices[(i + 1) % l]
            self.faces.append(Face([v1, v3, v4, v2]))

    def create_base(self, height):
        base = []
        x, y, z = self.bumper()
        for i in range(self.num_sides):
            base.append(np.array([x + self.radius * math.cos(2 * math.pi/self.num_sides * i),
                                  y + self.radius * math.sin(2 * math.pi/self.num_sides * i),
                                  z + height]))
        return base
