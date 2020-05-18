import math
import numpy as np


class Object3D:
    def __init__(self, x, y, z):
        self.faces = None
        self.coordinates = np.array([x, y, z])

    def rotate(self, matrix):
        for face in self.faces:
            for i in range(len(face.vertices)):
                face.vertices[i] = face.vertices[i] - np.array([400, 400, 400])
                face.vertices[i] = np.dot(matrix, face.vertices[i]) + np.array([400, 400, 400])
        self.coordinates = np.dot(matrix, self.coordinates - 400) + 400

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
        for face in self.faces:
            points = []
            self.sort_faces()
            for i in range(len(face.vertices)):
                v0 = face.vertices[i]
                v1 = face.vertices[(i + 1) % len(face.vertices)]
                x0 = v0[0]  # + self.x
                y0 = v0[1]  # + self.y
                x1 = v1[0]  # + self.x
                y1 = v1[1]  # + self.y
                points.extend([x0, y0, x1, y1])
            canvas.create_polygon(points, outline="black", fill=face.color)
            # canvas.create_line(x0, y0, x1, y1, width=2)

    def bumpers(self):
        return self.x, self.y, self.z

    def sort_faces(self):
        key = lambda face: sum([vertex[2] for vertex in face.vertices]) / 4
        self.faces.sort(key=key)

    def set_face_colors(self, *args):
        for i in range(min(len(self.faces), len(args))):
            self.faces[i].set_color(args[i])


DELTA_THETA = math.pi / 64

ROTATE_X = np.array([[1, 0, 0],
                     [0, math.cos(DELTA_THETA), -math.sin(DELTA_THETA)],
                     [0, math.sin(DELTA_THETA), math.cos(DELTA_THETA)]
                     ])

ROTATE_Y = np.array([[math.cos(DELTA_THETA), 0, math.sin(DELTA_THETA)],
                     [0, 1, 0],
                     [-math.sin(DELTA_THETA), 0, math.cos(DELTA_THETA)]
                     ])

ROTATE_Z = np.array([[math.cos(DELTA_THETA), -math.sin(DELTA_THETA), 0],
                     [math.sin(DELTA_THETA), math.cos(DELTA_THETA), 0],
                     [0, 0, 1]
                     ])

DELTA_THETAC = - math.pi / 64

ROTATE_XC = np.array([[1, 0, 0],
                      [0, math.cos(DELTA_THETAC), -math.sin(DELTA_THETAC)],
                      [0, math.sin(DELTA_THETAC), math.cos(DELTA_THETAC)]
                      ])

ROTATE_YC = np.array([[math.cos(DELTA_THETAC), 0, math.sin(DELTA_THETAC)],
                      [0, 1, 0],
                      [-math.sin(DELTA_THETAC), 0, math.cos(DELTA_THETAC)]
                      ])

ROTATE_ZC = np.array([[math.cos(DELTA_THETAC), -math.sin(DELTA_THETAC), 0],
                      [math.sin(DELTA_THETAC), math.cos(DELTA_THETAC), 0],
                      [0, 0, 1]
                      ])
