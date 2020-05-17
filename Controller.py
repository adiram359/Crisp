# from Environment import Environment
# import Object3D
# from random import random
# import numpy as np
# import time
# from Cube import Cube
#
# # if __name__ == '__main__':
# #     e = Environment("white", 800, 800)
# #     cube = e.add("Cube", 400, 400, 500, 40, "block")
# #
# #     while True:
# #         cube.rotateX(Object3D.DELTA_THETA)
# #         #e.rotateAll(Object3D.ROTATE_Y)
# #         #e.rotateAll(Object3D.ROTATE_X)
# #         #e.rotateAll(Object3D.ROTATE_Z)
# #
# #         e.render()
#
# from tkinter import *
# import math
#
# theta = math.pi / 4
# if __name__ == "__main__":
#     top = Tk()
#     canvas = Canvas(top, width=1000, height=1000)
#     canvas.pack()
#
#     # square = [np.array([360, 360]),
#     #           np.array([440, 360]),
#     #           np.array([440, 440]),
#     #           np.array([360, 440])]
#
#     #
#     # matrix = np.array([[math.cos(theta), -math.sin(theta)],
#     #                    [math.sin(theta), math.cos(theta)]])
#     #
#     #
#
#
#     #
#     #
#     # def render():
#     #     points = []
#     #     for i in range(len(square)):
#     #         v0 = square[i]
#     #         v1 = square[(i + 1) % len(square)]
#     #         x0 = v0[0]
#     #         y0 = v0[1]
#     #         x1 = v1[0]
#     #         y1 = v1[1]
#     #         points.extend([x0, y0, x1, y1])
#     #     canvas.create_polygon(points, outline="black", fill="white")
#     #
#     # def rotate():
#     #     for j in range(len(square)):
#     #         square[j] = np.dot(matrix, square[j] - np.array([400, 400])) + np.array([400, 400])
#     #         print(square[j])
#
#     cube = Cube(400, 400, 300, 40)
#
#     while (True):
#         canvas.delete(ALL)
#         canvas.create_oval(399, 399, 400, 400)
#         cube.render(canvas)
#         cube.rotateX(theta)
#         cube.rotateY(theta)
#         cube.rotateZ(theta)
#
#         top.update()
#
#

from Environment import Environment
import Object3D
from random import random
import numpy as np
import time

MEDIUMSEAGREEN = "#3CB371"
SEAGREEN = "#2E8B57"
FORRESTGREEN = "#228B22"
GREEN = "#008000"
DARKGREEN = "#006400"
DARKSEAGREEN = "#8FBC8B"
MEDIUMAQUAMARINE = "#66CDAA"
LIGHTGREEN = "#90EE90"

if __name__ == '__main__':
    e = Environment("white", 800, 800)
    cube = e.add("Cube", 440, 400, 500, 40)
    cube2 = e.add("Cube", 360, 400, 500, 40)
    #cube2 = e.add("Cube", 400, 400, 400, 20)

    cube.set_face_colors(MEDIUMSEAGREEN, SEAGREEN,
                         FORRESTGREEN, MEDIUMAQUAMARINE,
                         MEDIUMSEAGREEN,DARKSEAGREEN)

    while True:
        #e.rotateAll(Object3D.ROTATE_Y)
        #e.rotateAll(Object3D.ROTATE_X)
        #e.rotateAll(Object3D.ROTATE_Z)

        e.render()

