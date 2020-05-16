import Object3D
import numpy as np
import Face


class Cube(Object3D.Object3D):
    def __init__(self, x, y, z, radius, display="block"):
        super().__init__(x, y, z)
        self.radius = radius
        self.name = "Cube"
        self.faces = []
        self.display = display
        self.create_faces(radius)

    def create_faces(self, radius):
        x_bumper, y_bumper, z_bumper = self.bumpers()
        coefficients = [-1, 1]
        for c in coefficients:
            temp = [np.array([x_bumper + c * radius, y_bumper - radius, z_bumper - radius]),
                    np.array([x_bumper + c * radius, y_bumper + radius, z_bumper - radius]),
                    np.array([x_bumper + c * radius, y_bumper + radius, z_bumper + radius]),
                    np.array([x_bumper + c * radius, y_bumper - radius, z_bumper + radius]),
                    np.array([x_bumper + radius, y_bumper + c * radius, z_bumper - radius]),
                    np.array([x_bumper - radius, y_bumper + c * radius, z_bumper - radius]),
                    np.array([x_bumper - radius, y_bumper + c * radius, z_bumper + radius]),
                    np.array([x_bumper + radius, y_bumper + c * radius, z_bumper + radius]),
                    np.array([x_bumper + radius, y_bumper - radius, z_bumper + c * radius]),
                    np.array([x_bumper + radius, y_bumper + radius, z_bumper + c * radius]),
                    np.array([x_bumper - radius, y_bumper + radius, z_bumper + c * radius]),
                    np.array([x_bumper - radius, y_bumper - radius, z_bumper + c * radius])]
            self.faces.append(Face.Face(temp[0:4]))
            self.faces.append(Face.Face(temp[4:8]))
            self.faces.append(Face.Face(temp[8:12]))
