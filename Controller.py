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
    e = Environment("white", 800, 800)
    cube = e.add("Cube", 440, 400, 500, 40)
    cube2 = e.add("Cube", 360, 400, 500, 40)
    # cube2 = e.add("Cube", 400, 400, 400, 20)

    cube.set_face_colors(MEDIUMSEAGREEN, SEAGREEN,
                         FORRESTGREEN, MEDIUMAQUAMARINE,
                         MEDIUMSEAGREEN, DARKSEAGREEN)

    while True:
        # e.rotateAll(Object3D.ROTATE_Y)
        # e.rotateAll(Object3D.ROTATE_X)
        # e.rotateAll(Object3D.ROTATE_Z)
        # e.rotateAll(Object3D.ROTATE_X)
        e.render()
