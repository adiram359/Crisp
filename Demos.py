from Object3D import Object3D
from Cube import Cube
from Pyramid import Pyramid
from random import random
from Sphere import Sphere
import math
from Prism import Prism
from Environment import Environment

def tower(e):
    grass = Prism(400, 400, 700, 200, 10, 4, "flex", "#7DCEA0", "#45B39D")
    cube = Cube(500, 400, 400, 20, "flex", "blue", "black")
    e.add(cube)
    e.add(grass)

