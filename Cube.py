import Object3D
import numpy as np
import Face


class Cube(Object3D.Object3D):
    def __init__(self, x, y, z, radius, display, color="white"):
        super().__init__(x, y, z, display, color)
        self.radius = radius
        self.name = "Cube"
        self.faces = []
        self.create_faces(radius)

    def create_faces(self, radius):
        coefficients = [-1, 1]
        x, y, z = self.bumper()
        for c in coefficients:
            temp = [np.array(
                [x + c * radius, y - radius, z - radius]),
                np.array([x + c * radius, y + radius, z - radius]),
                np.array([x + c * radius, y + radius, z + radius]),
                np.array([x + c * radius, y - radius, z + radius]),
                np.array([x + radius, y + c * radius, z - radius]),
                np.array([x - radius, y + c * radius, z - radius]),
                np.array([x - radius, y + c * radius, z + radius]),
                np.array([x + radius, y + c * radius, z + radius]),
                np.array([x + radius, y - radius, z + c * radius]),
                np.array([x + radius, y + radius, z + c * radius]),
                np.array([x - radius, y + radius, z + c * radius]),
                np.array([x - radius, y - radius, z + c * radius])]
            self.faces.append(Face.Face(temp[0:4]))
            self.faces.append(Face.Face(temp[4:8]))
            self.faces.append(Face.Face(temp[8:12]))
