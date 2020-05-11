import math
import numpy as np


class Object3D:
    def __init__(self, x, y, z):
        self.faces = None
        self.x = x
        self.y = y
        self.z = z

    def rotateX(self):
        self.rotate_helper(ROTATE_X)

    def rotateY(self):
        self.rotate_helper(ROTATE_Y)

    def rotateZ(self):
        self.rotate_helper(ROTATE_Z)

    def rotateXC(self):
        self.rotate_helper(ROTATE_XC)

    def rotateYC(self):
        self.rotate_helper(ROTATE_YC)

    def rotateZC(self):
        self.rotate_helper(ROTATE_ZC)

    def rotate_helper(self, matrix):
        for face in self.faces:
            for i in range(len(face.vertices)):
                face.vertices[i] = np.dot(matrix, face.vertices[i])

    def render(self, canvas):
        self.draw_wireframe(canvas)

    def draw_wireframe(self, canvas):

        for face in self.faces:
            points = []
            self.sort_faces()
            for i in range(len(face.vertices)):
                v0 = face.vertices[i]
                v1 = face.vertices[(i + 1) % len(face.vertices)]
                x0 = v0[1] + self.x
                y0 = v0[2] + self.y
                x1 = v1[1] + self.x
                y1 = v1[2] + self.y
                points.extend([x0, y0, x1, y1])
            canvas.create_polygon(points, outline="black", fill="#82E0AA")
                #canvas.create_line(x0, y0, x1, y1, width=2)

    def sort_faces(self):
        key = lambda face: sum([vertex[0] for vertex in face.vertices])/4
        self.faces.sort(key=key)

PI = math.pi

DELTA_THETA = math.pi / 32

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

DELTA_THETAC = - math.pi / 32

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