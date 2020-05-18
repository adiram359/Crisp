from Environment import Environment
import Object3D
from random import random
import numpy as np
import time
import math

MEDIUMSEAGREEN = "#3CB371"
SEAGREEN = "#2E8B57"
FORRESTGREEN = "#228B22"
GREEN = "#008000"
DARKGREEN = "#006400"
DARKSEAGREEN = "#8FBC8B"
MEDIUMAQUAMARINE = "#66CDAA"
LIGHTGREEN = "#90EE90"

if __name__ == '__main__':
    e = Environment("#D2B4DE", 800, 800)
    cube = e.add("Cube", 400, 400, 500, 40, "flex")
    cube2 = e.add("Cube",480, 400, 420, 40, "flex")
    cube3 = e.add("Cube",320, 400, 420, 40, "flex")
    cube4 = e.add("Cube", 400, 400, 340, 40, "flex")

    #p =  e.add("Pyramid", 400, 400, 400,10, 300, 3)
    for i in range(11):
        e.add("Pyramid", random()*800,random()*800,random()*800, 10, 30, 5, "block")

    cube.set_face_colors(MEDIUMSEAGREEN, SEAGREEN,
                         FORRESTGREEN, MEDIUMAQUAMARINE,
                         MEDIUMSEAGREEN, DARKSEAGREEN)
    theta = math.pi/64
    while True:
       # e.rotate_all_y(theta)
        # e.rotateAll(Object3D.ROTATE_Y)
        # e.rotateAll(Object3D.ROTATE_X)
        # e.rotateAll(Object3D.ROTATE_Z)
        # e.rotateAll(Object3D.ROTATE_X)
        e.render()
