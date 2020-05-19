import math
import numpy as np


class Object3D:
    def __init__(self, x, y, z, display, color, outline):
        self.display = display
        self.faces = None
        self.coordinates = np.array([x, y, z])
        self.color = color
        self.outline = outline

    def rotate(self, matrix, center):
        c = 1 if self.display == "flex" else 0
        for face in self.faces:
            for i in range(len(face.vertices)):
                face.vertices[i] = face.vertices[i] - c * center
                face.vertices[i] = np.dot(matrix, face.vertices[i]) + c * center
        if c:
            self.coordinates = np.dot(matrix, self.coordinates - c * center) + c * center

    def rotate_x(self, theta, center=400):
        matrix = np.array([[1, 0, 0],
                           [0, math.cos(theta), -math.sin(theta)],
                           [0, math.sin(theta), math.cos(theta)]])

        self.rotate(matrix, center)

    def rotate_y(self, theta, center=400):
        matrix = np.array([[math.cos(theta), 0, math.sin(theta)],
                           [0, 1, 0],
                           [-math.sin(theta), 0, math.cos(theta)]])
        self.rotate(matrix, center)

    def rotate_z(self, theta, center=400):
        matrix = np.array([[math.cos(theta), -math.sin(theta), 0],
                           [math.sin(theta), math.cos(theta), 0],
                           [0, 0, 1]
                           ])
        self.rotate(matrix, center)

    def render(self, canvas):
        c = 1 if self.display == "block" else 0
        for face in self.faces:
            points = []
            self.sort_faces()
            for i in range(len(face.vertices)):
                v0 = face.vertices[i]
                v1 = face.vertices[(i + 1) % len(face.vertices)]
                x0 = v0[1] + c * self.coordinates[1]
                y0 = v0[2] + c * self.coordinates[2]
                x1 = v1[1] + c * self.coordinates[1]
                y1 = v1[2] + c * self.coordinates[2]
                points.extend([x0, y0, x1, y1])
            fill = self.color if face.color == "white" else face.color
            outline = self.outline if face.outline == "black" else face.outline
            canvas.create_polygon(points, outline=outline, fill=fill)


    def sort_faces(self):
        key = lambda face: sum([vertex[0] for vertex in face.vertices]) / len(face.vertices)
        self.faces.sort(key=key)

    def set_face_colors(self, *args):
        for i in range(min(len(self.faces), len(args))):
            self.faces[i].set_color(args[i])

    def bumper(self):
        if self.display == "flex":
            return self.coordinates[0], self.coordinates[1], self.coordinates[2]
        else:
            return 0, 0, 0

    def rotate_in_place_x(self, theta):
        self.rotate_x(theta, self.coordinates)
        # matrix = np.array([[1, 0, 0],
        #            [0, math.cos(theta), -math.sin(theta)],
        #            [0, math.sin(theta), math.cos(theta)]])
        # for face in self.faces:
        #     for i in range(len(face.vertices)):
        #         face.vertices[i] -= self.coordinates
        #         face.vertices[i] = np.dot(matrix, face.vertices[i]) + self.coordinates

    def rotate_in_place_y(self, theta):
        self.rotate_y(theta, self.coordinates)
        # matrix = np.array([[math.cos(theta), 0, math.sin(theta)],
        #                    [0, 1, 0],
        #                    [-math.sin(theta), 0, math.cos(theta)]])
        # for face in self.faces:
        #     for i in range(len(face.vertices)):
        #         face.vertices[i] -= self.coordinates
        #         face.vertices[i] = np.dot(matrix, face.vertices[i]) + self.coordinates

    def rotate_in_place_z(self, theta):
        self.rotate_z(theta, self.coordinates)
        # matrix = np.array([[math.cos(theta), -math.sin(theta), 0],
        #                    [math.sin(theta), math.cos(theta), 0],
        #                    [0, 0, 1]
        #                    ])
        #
        # for face in self.faces:
        #     x, y, z = self.coordinates[0], self.coordinates[1], self.coordinates[2]
        #     for i in range(len(face.vertices)):
        #         print("before ",  face.vertices[i])
        #         face.vertices[i] = face.vertices[i] - np.array([x, y, z ])
        #         face.vertices[i] = np.dot(matrix, face.vertices[i]) + np.array([x, y, z])
        #         print("after ",  face.vertices[i])
