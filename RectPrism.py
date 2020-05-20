import Object3D
import numpy as np
from Face import Face
import math


class RectPrism(Object3D.Object3D):
    def __init__(self, x, y, z, length, height, width, display, color="white",outline="black"):
        super().__init__(x, y, z, display, color, outline)
        self.length = length
        self.height = height
        self.num_sides = 4
        self.faces = []
        self.name = "RectPrism"
        self.width = width
        self.create_faces()
        #self.rotate_in_place_z(math.pi/4)
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
        base.append(np.array([x + self.width/2, y - self.length/2, z - self.height/2 + height]))
        base.append(np.array([x + self.width/2, y + self.length/2, z - self.height/2 + height]))
        base.append(np.array([x - self.width / 2, y + self.length / 2, z - self.height / 2 + height]))
        base.append(np.array([x - self.width/2, y - self.length/2, z - self.height/2 + height]))


        return base
