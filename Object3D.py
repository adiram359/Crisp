import math
import numpy as np


class Object3D:
    def __init__(self, x, y, z, display, color="white"):
        self.display = display
        self.faces = None
        self.coordinates = np.array([x, y, z])
        self.color = color

    def rotate(self, matrix):
        c = 1 if self.display == "flex" else 0
        for face in self.faces:
            for i in range(len(face.vertices)):
                face.vertices[i] = face.vertices[i] - c * 400
                face.vertices[i] = np.dot(matrix, face.vertices[i]) + c * 400
        if c:
            self.coordinates = np.dot(matrix, self.coordinates - c * 400) + c * 400

    def rotate_x(self, theta):
        matrix = np.array([[1, 0, 0],
                           [0, math.cos(theta), -math.sin(theta)],
                           [0, math.sin(theta), math.cos(theta)]])

        self.rotate(matrix)

    def rotate_y(self, theta):
        matrix = np.array([[math.cos(theta), 0, math.sin(theta)],
                           [0, 1, 0],
                           [-math.sin(theta), 0, math.cos(theta)]])
        self.rotate(matrix)

    def rotate_z(self, theta):
        matrix = np.array([[math.cos(theta), -math.sin(theta), 0],
                           [math.sin(theta), math.cos(theta), 0],
                           [0, 0, 1]
                           ])
        self.rotate(matrix)

    def render(self, canvas):
        c = 1 if self.display == "block" else 0
        for face in self.faces:
            points = []
            self.sort_faces()
            for i in range(len(face.vertices)):
                v0 = face.vertices[i]
                v1 = face.vertices[(i + 1) % len(face.vertices)]
                x0 = v0[0] + c * self.coordinates[0]
                y0 = v0[1] + c * self.coordinates[1]
                x1 = v1[0] + c * self.coordinates[0]
                y1 = v1[1] + c * self.coordinates[1]
                points.extend([x0, y0, x1, y1])
            fill = self.color if face.color == "white" else face.color
            canvas.create_polygon(points, outline="black", fill=fill)


    def sort_faces(self):
        key = lambda face: sum([vertex[2] for vertex in face.vertices]) / len(face.vertices)
        self.faces.sort(key=key)

    def set_face_colors(self, *args):
        for i in range(min(len(self.faces), len(args))):
            self.faces[i].set_color(args[i])

    def bumper(self):
        if self.display == "flex":
            return self.coordinates[0], self.coordinates[1], self.coordinates[2]
        else:
            return 0, 0, 0
