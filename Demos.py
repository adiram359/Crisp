from Object3D import Object3D
from Cube import Cube
from Pyramid import Pyramid
from random import random
from Sphere import Sphere
import SpecialObjects
import math
from Prism import Prism
from Environment import Environment
from RectPrism import RectPrism

BLACK = "black"
RED = "#E74C3C"
PURPLE = "#7E1A43"
ORANGE = "#FAAE29"
MAROON = "#A93226"
PUMPKIN = "#BA4A00"
VIOLET = "#9B59B6"
MUSTARD = "#D4AC0D"
SUNSHINE_YELLOW = "#F4D03F"
def tower(e):

    t = SpecialObjects.Arch(400, 400, 400, 40, 180, 70, 50, "flex")
    t.color = MAROON
    t.set_face_colors(RED, RED)
    e.add(t)
    t = SpecialObjects.Arch(400, 465, 335, 40, 180, 70, 50, "flex")
    t.rotate_in_place_z(math.pi / 2)
    t.set_face_colors(ORANGE, ORANGE)
    t.color = PUMPKIN
    e.add(t)
    t = SpecialObjects.Arch(400, 335, 335, 40, 180, 70, 50, "flex")
    t.rotate_in_place_z(math.pi / 2)
    t.set_face_colors(VIOLET, VIOLET)
    t.color = PURPLE
    e.add(t)
    t = SpecialObjects.Arch(400, 400, 270, 40, 180, 70, 50, "flex")
    t.set_face_colors(SUNSHINE_YELLOW, SUNSHINE_YELLOW)
    t.color = MUSTARD
    e.add(t)


    t = Cube(400, 465, 460, 25, "flex")
    t.set_face_colors(RED, MAROON, BLACK, RED, ORANGE, BLACK)
    e.add(t)
    t = Cube(400, 465, 340, 25, "flex")
    t.set_face_colors(RED, MAROON, BLACK, RED, ORANGE, BLACK)
    e.add(t)
    t = Cube(400, 465, 290, 25, "flex")
    t.set_face_colors(RED, MAROON, BLACK, RED, ORANGE, BLACK)
    e.add(t)
    # t = Cube(400, 465, 240, 25, "flex")
    # t.set_face_colors(RED, MAROON, BLACK, RED, ORANGE, BLACK)
    # e.add(t)

    t = Cube(400, 335, 340, 25, "flex")
    t.set_face_colors(PURPLE, VIOLET, BLACK, RED, MAROON, BLACK)
    e.add(t)
    t = Cube(400, 335, 460, 25, "flex")
    t.set_face_colors(PURPLE, VIOLET, BLACK, RED, MAROON, BLACK)
    e.add(t)
    t = Cube(400, 335, 290, 25, "flex")
    e.add(t)
    t.set_face_colors(PURPLE, VIOLET, BLACK, RED, MAROON, BLACK)
    # t = Cube(400, 335, 240, 25, "flex")
    # e.add(t)
    # t.set_face_colors(PURPLE, VIOLET, BLACK, RED, MAROON, BLACK)


    t = Cube(270, 335, 460, 25, "flex")
    e.add(t)
    t.set_face_colors(SUNSHINE_YELLOW, VIOLET, BLACK, PURPLE, MUSTARD, BLACK)
    t = Cube(270, 335, 340, 25, "flex")
    e.add(t)
    t.set_face_colors(SUNSHINE_YELLOW, VIOLET, BLACK, PURPLE, MUSTARD, BLACK)
    t = Cube(270, 335, 290, 25, "flex")
    t.set_face_colors(SUNSHINE_YELLOW, VIOLET, BLACK, PURPLE, MUSTARD, BLACK)
    e.add(t)
    # t = Cube(270, 335, 240, 25, "flex")
    # t.set_face_colors(SUNSHINE_YELLOW, VIOLET, BLACK, PURPLE, MUSTARD, BLACK)
    # e.add(t)

    t = Cube(270, 465, 460, 25, "flex")
    t.set_face_colors(SUNSHINE_YELLOW, ORANGE, BLACK, PUMPKIN, ORANGE, BLACK)
    e.add(t)
    t = Cube(270, 465, 340, 25, "flex")
    t.set_face_colors(SUNSHINE_YELLOW, ORANGE, BLACK, PUMPKIN, ORANGE, BLACK)
    e.add(t)
    t = Cube(270, 465, 290, 25, "flex")
    t.set_face_colors(SUNSHINE_YELLOW, ORANGE, BLACK, PUMPKIN, ORANGE, BLACK)
    e.add(t)
    # t = Cube(270, 465, 240, 25, "flex")
    # t.set_face_colors(SUNSHINE_YELLOW, ORANGE, BLACK, PUMPKIN, ORANGE, BLACK)
    # e.add(t)

def bridge(e):
    SF = "#C0392B"
    p = SpecialObjects.Arch(400, 400, 400, 40, 120, 60, 40, "flex", RED, "black")
    e.add(p)
    p = SpecialObjects.Arch(500, 400, 400, 40, 120, 60, 40, "flex", RED, "black")
    e.add(p)
    p.rotate_in_place_x(math.pi)
    p = RectPrism(400, 350, 350, 20, 50, 40, "flex", RED, "black")
    e.add(p)
    p = RectPrism(400, 450, 350, 20, 50, 40, "flex", RED, "black")
    e.add(p)
    p = SpecialObjects.Arch(270, 400, 400, 30, 90, 40, 30, "flex", RED, "black")
    e.add(p)
    p = SpecialObjects.Arch(350, 400, 400, 30, 90, 40, 30, "flex", RED, "black")
    e.add(p)
    p.rotate_in_place_x(math.pi)
    p = RectPrism(400, 362, 490, 15, 40, 30, "flex", RED, "black")
    e.add(p)
    p.rotate_in_place_x(math.pi)
    p = RectPrism(400, 437, 490, 15, 40, 30, "flex", RED, "black")
    e.add(p)
    p = SpecialObjects.Arch(180, 400, 400, 20, 60, 30, 15, "flex", RED, "black")
    e.add(p)
    p = SpecialObjects.Arch(235, 400, 400, 20, 60, 30, 30/2, "flex", RED, "black")
    p.rotate_in_place_x(math.pi)
    e.add(p)
    p = RectPrism(400, 375, 593, 10, 25, 15, "flex", RED, "black")
    e.add(p)
    p.rotate_in_place_x(math.pi)
    p = RectPrism(400, 425, 593, 10, 25, 15, "flex", RED, "black")
    e.add(p)