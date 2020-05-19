from Prism import Prism
from Object3D import Object3D
import numpy as np
from Face import Face
import math


class Arch(Object3D):
    def __init__(self, x, y, z, radius, length, height, width, display, color="white"):
        super().__init__(x, y, z, display, color)
        self.width = height
        self.radius = radius
        self.length = length
        self.height = width
        self.faces = []
        Prism.create_faces(self)
        self.rotate_z(math.pi/2)

    def create_base(self, height):
        base = []
        x, y, z = self.bumper()
        base.append(np.array([x + self.width/2, y - self.length/2, z - self.height/2 + height]))
        divisions = 10
        theta = 0
        for i in range(divisions + 1):
            x0 = x + self.width/2 - math.sin(theta) * self.radius
            y0 = y - math.cos(theta) * self.radius
            z0 = z - self.height/2 + height
            base.append(np.array([x0, y0, z0]))
            theta += math.pi/divisions
        base.append(np.array([x + self.width/2, y + self.length/2, z - self.height/2 + height]))
        base.append(np.array([x - self.width/2, y + self.length/2, z - self.height/2 + height]))
        base.append(np.array([x - self.width/2, y - self.length/2, z - self.height/2 + height ]))

        return base
