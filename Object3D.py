# # import math
# # import numpy as np
# #
# #
# # class Object3D:
# #     def __init__(self, x, y, z):
# #         self.faces = None
# #         self.x = x
# #         self.y = y
# #         self.z = z
# #
# #     def rotateX(self, theta):
# #         for face in self.faces:
# #             for i in range(len(face.vertices)):
# #                 face.vertices[i] = face.vertices[i] - np.array([400, 400, 400])
# #                 face.vertices[i] = np.dot(ROTATE_X, face.vertices[i]) + np.array([400, 400, 400])
# #
# #     def rotateY(self, theta):
# #         for face in self.faces:
# #             for i in range(len(face.vertices)):
# #                 face.vertices[i] = face.vertices[i] - np.array([400, 400, 400])
# #                 face.vertices[i] = np.dot(ROTATE_Y, face.vertices[i]) + np.array([400, 400, 400])
# #
# #     def rotateZ(self, theta):
# #         for face in self.faces:
# #             for i in range(len(face.vertices)):
# #                 face.vertices[i] = face.vertices[i] - np.array([400, 400, 400])
# #                 face.vertices[i] = np.dot(ROTATE_Z, face.vertices[i]) + np.array([400, 400, 400])
# #
# #
# #
# #     def rotate_helper(self, matrix):
# #         for face in self.faces:
# #             for i in range(len(face.vertices)):
# #                 face.vertices[i] = np.dot(matrix, face.vertices[i])
# #             print(face.vertices)
# #
# #     def render(self, canvas):
# #         for face in self.faces:
# #             points = []
# #             self.sort_faces()
# #             for i in range(len(face.vertices)):
# #                 v0 = face.vertices[i]
# #                 v1 = face.vertices[(i + 1) % len(face.vertices)]
# #                 x0 = v0[0]
# #                 y0 = v0[1]
# #                 x1 = v1[0]
# #                 y1 = v1[1]
# #                 points.extend([x0, y0, x1, y1])
# #             canvas.create_polygon(points, outline="black", fill="white")
# #                 #canvas.create_line(x0, y0, x1, y1, width=2)
# #
# #
# #
# #
# #
# #     def sort_faces(self):
# #         key = lambda face: sum([vertex[0] for vertex in face.vertices])/4
# #         self.faces.sort(key=key)
# #
# #     def set_face_colors(self, *args):
# #         for i in range(min(len(self.faces), len(args))):
# #             self.faces[i].set_color(args[i])
# #
# #
# # DELTA_THETA = math.pi / 48
# #
# # ROTATE_X = np.array([[1, 0, 0],
# #                      [0, math.cos(DELTA_THETA), -math.sin(DELTA_THETA)],
# #                      [0, math.sin(DELTA_THETA), math.cos(DELTA_THETA)]
# #                      ])
# #
# # ROTATE_Y = np.array([[math.cos(DELTA_THETA), 0, math.sin(DELTA_THETA)],
# #                      [0, 1, 0],
# #                      [-math.sin(DELTA_THETA), 0, math.cos(DELTA_THETA)]
# #                      ])
# #
# # ROTATE_Z = np.array([[math.cos(DELTA_THETA), -math.sin(DELTA_THETA), 0],
# #                      [math.sin(DELTA_THETA), math.cos(DELTA_THETA), 0],
# #                      [0, 0, 1]
# #                      ])
# #
# # DELTA_THETAC = - math.pi / 32
# #
# # ROTATE_XC = np.array([[1, 0, 0],
# #                      [0, math.cos(DELTA_THETAC), -math.sin(DELTA_THETAC)],
# #                      [0, math.sin(DELTA_THETAC), math.cos(DELTA_THETAC)]
# #                      ])
# #
# # ROTATE_YC = np.array([[math.cos(DELTA_THETAC), 0, math.sin(DELTA_THETAC)],
# #                      [0, 1, 0],
# #                      [-math.sin(DELTA_THETAC), 0, math.cos(DELTA_THETAC)]
# #                      ])
# #
# # ROTATE_ZC = np.array([[math.cos(DELTA_THETAC), -math.sin(DELTA_THETAC), 0],
# #                      [math.sin(DELTA_THETAC), math.cos(DELTA_THETAC), 0],
# #                      [0, 0, 1]
# #
# #                    ])
#
#
# from Environment import Environment
# import Object3D
# from random import random
# import numpy as np
# import time
#
# MEDIUMSEAGREEN = "#3CB371"
# SEAGREEN = "#2E8B57"
# FORRESTGREEN = "#228B22"
# GREEN = "#008000"
# DARKGREEN = "#006400"
# DARKSEAGREEN = "#8FBC8B"
# MEDIUMAQUAMARINE = "#66CDAA"
# LIGHTGREEN = "#90EE90"
#
# if __name__ == '__main__':
#     e = Environment("white", 800, 800)
#     cube = e.add("Cube", 400, 400, 500, 40, "flex")
#     #cube2 = e.add("Cube", 400, 400, 400, 20)
#
#     cube.set_face_colors(MEDIUMSEAGREEN, SEAGREEN,
#                          FORRESTGREEN, MEDIUMAQUAMARINE,
#                          MEDIUMSEAGREEN,DARKSEAGREEN)
#     for i in range(10):
#         pyramid = e.add("Pyramid", random()*800, random()*800, random() * 800,  20, 30, 6, "flex")
#         pyramid.set_face_colors(MEDIUMSEAGREEN, SEAGREEN, FORRESTGREEN, MEDIUMAQUAMARINE, DARKGREEN, DARKSEAGREEN, LIGHTGREEN)
#
#     while True:
#
#         e.render()
import math
import numpy as np


class Object3D:
    def __init__(self, x, y, z):
        self.faces = None
        self.x = x
        self.y = y
        self.z = z

    def rotateX(self):
        for face in self.faces:
            for i in range(len(face.vertices)):
                face.vertices[i] = face.vertices[i] - np.array([400, 400, 400])
                face.vertices[i] = np.dot(ROTATE_X, face.vertices[i]) + np.array([400, 400, 400])

    def rotateY(self):
        for face in self.faces:
            for i in range(len(face.vertices)):
                face.vertices[i] = face.vertices[i] - np.array([400, 400, 400])
                face.vertices[i] = np.dot(ROTATE_Y, face.vertices[i]) + np.array([400, 400, 400])

    def rotateZ(self):
        for face in self.faces:
            for i in range(len(face.vertices)):
                face.vertices[i] = face.vertices[i] - np.array([400, 400, 400])
                face.vertices[i] = np.dot(ROTATE_ZC, face.vertices[i]) + np.array([400, 400, 400])

    def rotateXC(self):
        for face in self.faces:
            for i in range(len(face.vertices)):
                face.vertices[i] = face.vertices[i] - np.array([400, 400, 400])
                face.vertices[i] = np.dot(ROTATE_XC, face.vertices[i]) + np.array([400, 400, 400])

    def rotateYC(self):
        for face in self.faces:
            for i in range(len(face.vertices)):
                face.vertices[i] = face.vertices[i] - np.array([400, 400, 400])
                face.vertices[i] = np.dot(ROTATE_YC, face.vertices[i]) + np.array([400, 400, 400])

    def rotateZC(self):
        for face in self.faces:
            for i in range(len(face.vertices)):
                face.vertices[i] = face.vertices[i] - np.array([400, 400, 400])
                face.vertices[i] = np.dot(ROTATE_ZC, face.vertices[i]) + np.array([400, 400, 400])

    def rotate_helper(self, matrix):
        for face in self.faces:
            for i in range(len(face.vertices)):
                face.vertices[i] = np.dot(matrix, face.vertices[i])

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
        key = lambda face: sum([vertex[0] for vertex in face.vertices]) / 4
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
