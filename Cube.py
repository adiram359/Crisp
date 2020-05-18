import Object3D
import numpy as np
import Face


class Cube(Object3D.Object3D):
    def __init__(self, x, y, z, radius):
        super().__init__(x, y, z)
        self.radius = radius
        self.name = "Cube"
        self.faces = []
        self.create_faces(radius)

    def create_faces(self, radius):
        coefficients = [-1, 1]
        for c in coefficients:
            temp = [np.array(
                [self.coordinates[0] + c * radius, self.coordinates[1] - radius, self.coordinates[2] - radius]),
                np.array(
                    [self.coordinates[0] + c * radius, self.coordinates[1] + radius, self.coordinates[2] - radius]),
                np.array(
                    [self.coordinates[0] + c * radius, self.coordinates[1] + radius, self.coordinates[2] + radius]),
                np.array(
                    [self.coordinates[0] + c * radius, self.coordinates[1] - radius, self.coordinates[2] + radius]),
                np.array(
                    [self.coordinates[0] + radius, self.coordinates[1] + c * radius, self.coordinates[2] - radius]),
                np.array(
                    [self.coordinates[0] - radius, self.coordinates[1] + c * radius, self.coordinates[2] - radius]),
                np.array(
                    [self.coordinates[0] - radius, self.coordinates[1] + c * radius, self.coordinates[2] + radius]),
                np.array(
                    [self.coordinates[0] + radius, self.coordinates[1] + c * radius, self.coordinates[2] + radius]),
                np.array(
                    [self.coordinates[0] + radius, self.coordinates[1] - radius, self.coordinates[2] + c * radius]),
                np.array(
                    [self.coordinates[0] + radius, self.coordinates[1] + radius, self.coordinates[2] + c * radius]),
                np.array(
                    [self.coordinates[0] - radius, self.coordinates[1] + radius, self.coordinates[2] + c * radius]),
                np.array(
                    [self.coordinates[0] - radius, self.coordinates[1] - radius, self.coordinates[2] + c * radius])]
            self.faces.append(Face.Face(temp[0:4]))
            self.faces.append(Face.Face(temp[4:8]))
            self.faces.append(Face.Face(temp[8:12]))
