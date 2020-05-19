from Environment import Environment
from Object3D import Object3D
from Cube import Cube
from Pyramid import Pyramid
from random import random
from Sphere import Sphere
import Demos
from Prism import Prism
import time
import math
import SpecialObjects

MEDIUMSEAGREEN = "#3CB371"
SEAGREEN = "#2E8B57"
FORRESTGREEN = "#228B22"
GREEN = "#008000"
DARKGREEN = "#006400"
DARKSEAGREEN = "#8FBC8B"
MEDIUMAQUAMARINE = "#66CDAA"
LIGHTGREEN = "#90EE90"

if __name__ == '__main__':
    e = Environment("#AED6F1", 800, 800)
    a = SpecialObjects.Arch(400, 400, 400, 40, 150, 60, 20,"block", "#AEB6BF")
    e.add(a)
    #cube = Cube(400, 400, 400, 40, "flex")
    # s = Sphere(400, 400, 480, 30,"flex", "#D2B4DE")
    # for i in range(10):
    #     c = Cube(random() * 800, random() * 800, random() * 800, random() * 20, "flex")
    #     c.set_face_colors(MEDIUMAQUAMARINE, SEAGREEN, LIGHTGREEN, MEDIUMAQUAMARINE, FORRESTGREEN,MEDIUMAQUAMARINE, SEAGREEN, LIGHTGREEN, MEDIUMAQUAMARINE, FORRESTGREEN)
    #     e.add(c)
    # e.add(s)
    # cube.set_face_colors(MEDIUMAQUAMARINE, SEAGREEN, LIGHTGREEN, MEDIUMAQUAMARINE, FORRESTGREEN)

    theta = 0
    while True:
        theta = theta + 0.02
        #e.rotate_all_y((math.sin(theta + 3 * math.pi/2) + 1)*math.pi/200)
        #e.rotate_all_z((math.sin(theta + 3 * math.pi/2) + 1)*math.pi/200)
        #e.rotate_all_x((math.sin(theta + 3 * math.pi/2) + 1)*math.pi/200)


        e.render()
