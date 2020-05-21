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

CACTUS_GREEN = "#2ECC71"
BLACK = "black"
RED = "#E74C3C"
PURPLE = "#7E1A43"
ORANGE = "#FAAE29"
MAROON = "#A93226"
PUMPKIN = "#BA4A00"
VIOLET = "#9B59B6"
MUSTARD = "#D4AC0D"
SUNSHINE_YELLOW = "#F4D03F"
SAND = "#F7DC6F"
OJ = "#F39C12"
BURNT = "#CB4335"
MAROON2 = "#922B21"
ROSE = "#F5B7B1"

RED2 = "#EC7063"
RED3 = "#CB4335"
RED4 = "#C0392B"
GRAY = "#808B96"
BROWN = "#593C25"
SKY_BLUE = "#5DADE2"
SANDGREEN = "#A2D9CE"



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
def cloud(x, y, z ,r):
    #global e
    step = 5
    for i in range(8):
        s = Sphere(x, y, z, r, "flex", "white", "white")
        e.add(s)
def bridge(e):
    def tower(z):
        p = SpecialObjects.Arch(400, 400, 400 + z, 35, 120, 60, 40, "flex", RED, RED)
        p.color = RED
        p.faces[0].color = MAROON2
        p.faces[16].color =  BURNT
        p.faces[18].color = BURNT

        e.add(p)
        p = RectPrism(400 + z, 352, 270, 25, 200, 40, "flex", RED, RED)
        p.faces[2].color, p.faces[3].color = RED, RED
        p.faces[4].color, p.faces[5].color = MAROON2, BURNT

        e.add(p)
        p = RectPrism(400 + z , 447, 270, 25, 200, 40, "flex", RED, "black")
        p.faces[2].color, p.faces[3].color = RED, BURNT
        p.faces[4].color, p.faces[5].color = MAROON2, RED
        e.add(p)

        p = SpecialObjects.Arch(270, 400, 400 + z, 25, 100, 40, 30, "flex", RED, RED)
        e.add(p)
        p.color = RED
        p.faces[0].color = MAROON2
        p.faces[16].color =  BURNT
        p.faces[18].color = BURNT

        p = RectPrism(400 + z, 362 , 470, 25, 80, 30, "flex", RED, "black")
        p.faces[2].color, p.faces[3].color = RED, RED
        p.faces[4].color, p.faces[5].color = MAROON2, BURNT
        e.add(p)
        p = RectPrism(400 + z, 437, 470, 25, 80, 30, "flex", RED, "black")
        p.faces[2].color, p.faces[3].color = RED, BURNT
        p.faces[4].color, p.faces[5].color = MAROON2, RED
        e.add(p)

        p = SpecialObjects.Arch(180, 400, 400 + z, 15, 70, 30, 20, "flex", RED, RED)
        e.add(p)
        p.color = RED
        p.faces[0].color = MAROON2
        p.faces[16].color =  BURNT
        p.faces[18].color = BURNT

        p = RectPrism(400 + z, 375, 578, 20, 55, 20, "flex", RED, "black")
        p.faces[2].color, p.faces[3].color = RED, RED
        p.faces[4].color, p.faces[5].color = MAROON2, BURNT
        e.add(p)
        p = RectPrism(400 + z, 425, 578, 20, 55, 20, "flex", RED, "black")
        p.faces[2].color, p.faces[3].color = RED, BURNT
        p.faces[4].color, p.faces[5].color = MAROON2,RED
        e.add(p)
    tower(-200)
    tower(200)
    r = RectPrism(400, 400, 320, 65, 10, 360, "flex", "#ABB2B9", "#ABB2B9")
    e.add(r)

    r = RectPrism(680, 400, 320, 65, 10, 130, "flex", "#ABB2B9", "#ABB2B9")
    e.add(r)
    r = RectPrism(600, 400, 320, 60, 10, 30, "flex", "#ABB2B9", "#ABB2B9")
    e.add(r)

    r = RectPrism(120, 400, 320, 65, 10, 130, "flex", "#ABB2B9", "#ABB2B9")
    e.add(r)
    r = RectPrism(200, 400, 320, 60, 10, 30, "flex", "#ABB2B9", "#ABB2B9")
    e.add(r)

    side_rail1 = RectPrism(400, 440, 320, 15, 30, 355, "flex", BURNT, BURNT)
    e.add(side_rail1)
    side_rail2 = RectPrism(400, 360, 320, 15, 30, 355, "flex", BURNT, BURNT)
    e.add(side_rail2)
    side3 = RectPrism(120,440, 320, 15, 30, 130, "flex", BURNT, BURNT)
    e.add(side3)
    side4 = RectPrism(120, 360, 320, 15, 30, 130, "flex", BURNT, BURNT)
    e.add(side4)
    side5 = RectPrism(680, 440, 320, 15, 30, 130, "flex", BURNT, BURNT)
    e.add(side5)
    side6 = RectPrism(680, 360, 320, 15, 30, 130, "flex", BURNT, BURNT)
    e.add(side6)
    def cloud(x, y, z ,r):
        #global e
        step = 5
        for i in range(8):
            s = Sphere(x, y, z, r, "flex", "white", "white")
            e.add(s)
            x += 7
    cloud(450 , 200, 80, 20)
    cloud(400, 200, 120, 30)
    cloud(500, 200, 120, 30)

    cloud(450 , 800, 200, 10)
    cloud(400, 800, 220, 30)
    cloud(500, 800, 230, 10)


def house_and_cactus(e):
    sand = Prism(400, 400, 70, 400, 20, 25, "flex", SAND, SAND)
    e.add(sand)
    house = Prism(400, 400, 90, 80, 160, 4, "flex", RED, RED)
    house.set_face_colors(RED, RED, "#E74C3C", "#FA8072", "#E74C3C", "#EC7063")
    e.add(house)


    def cactus(s1, s2, s3, s4, x, y, z, r):
        for _ in range(s1):
            circle = Sphere(x, y, z, r, "flex", CACTUS_GREEN, CACTUS_GREEN)
            e.add(circle)
            z -= 5
        for _ in range(s2):
            circle = Sphere(x, y, z, r-3, "flex", CACTUS_GREEN, CACTUS_GREEN)
            e.add(circle)
            x -= 5
        for _ in range(s3):
            z -= 4
            circle = Sphere(x, y, z, r-4, "flex", CACTUS_GREEN, CACTUS_GREEN)
            e.add(circle)
        z += s3 * 4
        x += s2 * 5
        for _ in range(s4):
            circle = Sphere(x, y, z, r-2 , "flex", CACTUS_GREEN, CACTUS_GREEN)
            e.add(circle)
            z -= 5
    def cloud(x, y, z ,r, steps):
        #global e
        for i in range(steps):
            s = Sphere(x, y, z, r, "flex", "white", "white")
            e.add(s)
            x += r/4


    def smoke_stake(x, y, z, r):
        for i in range(5):
            s = Sphere(x, y, z, r, "flex", GRAY, GRAY)
            e.add(s)
            x -= 5

        for i in range(10):
            s = Sphere(x, y, z, r, "flex", GRAY, GRAY)
            e.add(s)
            z -= 5



    cactus(15, 7, 5, 10, 600, 600, 700, 12)
    cactus(10, 6, 4, 6, 250, 100, 700, 10)
    cloud(100, 500, 200,10, 10)
    cloud(200, 650, 250,20, 20)
    cloud(300, 150, 150, 30, 14)
    cloud(400, 100, 80, 30, 20)

    h = SpecialObjects.HouseTop(400, 400, 295, 160, 160, 80, "flex", RED)
    e.add(h)
    whie = RectPrism(400, 400, 250, 160, 10, 162, "flex", "#EBDEF0")
    e.add(whie)


    roof = RectPrism(445, 400, 290, 180, 10, 130, "flex", ROSE,"black")
    roof.rotate_in_place_y(math.pi/4)
    e.add(roof)
    roof = RectPrism(351, 400, 290, 180, 10, 130, "flex",ROSE)
    e.add(roof)
    roof.rotate_in_place_y(-math.pi/4)
    roof = RectPrism(450, 400, 295,180, 1, 120, "flex",BROWN)
    e.add(roof)
    roof.rotate_in_place_y(math.pi/4)
    roof = RectPrism(350, 400, 295, 180, 1,120, "flex", BROWN,"black")
    roof.rotate_in_place_y(-math.pi/4)
    e.add(roof)

    #smoke_stake(320, 400, 570, 10)
    #e.add(Prism(297, 415, 275, 15, 10, 20, "flex", GRAY, GRAY))
    f = RectPrism(400, 480, 140, 50, 100, 0, "flex", CACTUS_GREEN, OJ)
    e.add(f)
    f.rotate_in_place_z(math.pi/2)

    f = RectPrism(418, 482, 140, 1, 8, 8, "flex", SUNSHINE_YELLOW)
    e.add(f)



def capitol_hill(e):
    BOTTOM = ""
    RIGHT = "#F4F6F6"
    BACK = "#E5E7E9"
    BONE = "#CCC2C0"
    BONE2 = "#9F9592"
    BONE3 = "#7C6D66"
    BONE4 = "#E3DBDA" # 227 219 218
    BONE6 = "#F6F0F0"
    TOP = "#D5D8DC"
    WHITE_HOUSE_BASE = "#F6F0F0"
    GRASS_GREE = "#2ECC71"
    grass = Prism(400, 325, 170, 290, 15, 30, "flex", GRASS_GREE)
    e.add(grass)
    p = RectPrism(400, 400, 194, 30, 20, 140, "flex", "#CCD1D1")
    p.set_face_colors(BOTTOM, TOP, "#9F9592", BONE, "#BDC3C7")
    e.add(p)
    piller = Prism(450, 400, 205, 10, 100, 8, "flex", "#EAEDED")
    e.add(piller)
    piller = Prism(415, 400, 205, 10, 100, 8, "flex", "#EAEDED")
    e.add(piller)
    piller = Prism(380, 400, 205, 10, 100, 8, "flex", "#EAEDED")
    e.add(piller)
    piller = Prism(345, 400, 205, 10, 100, 8, "flex", "#EAEDED")
    e.add(piller)
    p = RectPrism(400, 400, 310, 30, 10, 140, "flex")
    e.add(p)
    p.set_face_colors(BOTTOM, TOP, BONE3, BONE2, BOTTOM,  BONE)
    #PRISM ORDER: BOTTOM, TOP, LEFT, FRONT, righBACKt
    p = RectPrism(400, 400, 320, 30, 10, 150, "flex", "#CCD1D1")
    e.add(p)
    p.set_face_colors(BOTTOM, TOP, BONE2, "#E3DBDA", BONE)
    top = SpecialObjects.HouseTop(400, 400, 345, 30,150, 40, "flex", "#CCD1D1")
    #House ORDER: BOTTOM, BACK, FRONT, LEFT, RIGHT
    top.set_face_colors(BOTTOM, BOTTOM, "#E3DBDA", BONE, BONE2)
    e.add(top)
    b = RectPrism(400, 320, 195, 150, 20, 400, "flex", "#D0D3D4")
    e.add(b)
    b.set_face_colors(BOTTOM, TOP, BONE6,BONE4, BONE)
    b = RectPrism(400, 320, 265, 120, 120, 105, "flex", "#56473D")
    e.add(b)
    b.set_face_colors("white", "white", "white", "#909497", "white", BACK)
    #RECT PRISM: bottom, top, left, front, right, back
    b = RectPrism(520, 320, 265, 120, 120, 135, "flex", "#E5E7E9")
    e.add(b)
    b.set_face_colors(BOTTOM,TOP,BONE,BONE4,RIGHT,BACK)
    b = RectPrism(280, 320, 265, 120, 120, 135, "flex", "#E5E7E9")
    b.set_face_colors(BOTTOM,TOP,BONE,BONE4,RIGHT,BACK)
    e.add(b)
    b = RectPrism(400, 320, 335, 120, 20, 180, "flex", "#ABB2B9")
    b.set_face_colors(BOTTOM,TOP,BONE4,BONE6,RIGHT,BACK)
    e.add(b)
    b = RectPrism(400, 320, 350, 100, 10, 130, "flex", BONE4)
    e.add(b)

    b = Pyramid(260, 320, 325, 40, 25, 4, "flex", SANDGREEN)
    b.set_face_colors("", "#76D7C4", "#48C9B0", "#1ABC9C", "#48C9B0")
    e.add(b)
    b.rotate_in_place_y(math.pi/2)
    b.rotate_in_place_z(math.pi/4)

    b = Pyramid(535, 320, 325, 40, 25, 4, "flex", SANDGREEN)
    e.add(b)
    b.set_face_colors("", "#76D7C4", "#48C9B0", "#1ABC9C", "#48C9B0")
    b.rotate_in_place_y(math.pi/2)
    b.rotate_in_place_z(math.pi/4)
    b = Prism(400, 320, 355, 50, 10, 12, "flex", BONE)
    e.add(b)
    b = Sphere(400, 320, 450, 50, "flex", "#EAECEE")
    e.add(b)
    d = 380
    h = 245
    z = RectPrism(560, d, h, 2, 55, 15, "flex", BONE2)
    e.add(z)
    z = RectPrism(525, d, h, 2, 55, 15, "flex", BONE2)
    e.add(z)
    z = RectPrism(490, d, h, 2, 55, 15, "flex", BONE2)
    e.add(z)
    z = RectPrism(310, d, h, 2, 55, 15, "flex", BONE2)
    e.add(z)
    z = RectPrism(275, d, h, 2, 55, 15, "flex", BONE2)
    e.add(z)
    z = RectPrism(240, d, h, 2, 50 + 5, 15, "flex", BONE2)
    z.set_face_colors(GRAY)
    e.add(z)
    h = 300
    z = RectPrism(560, d, h, 2, 15, 15, "flex", BONE2)
    e.add(z)
    z = RectPrism(525, d, h, 2, 15, 15, "flex", BONE2)
    e.add(z)
    z = RectPrism(490, d, h, 2, 15, 15, "flex", BONE2)
    e.add(z)
    z = RectPrism(310, d, h, 2, 15, 15, "flex", BONE2)
    e.add(z)
    z = RectPrism(275, d, h, 2, 15, 15, "flex", BONE2)
    e.add(z)
    z = RectPrism(240, d, h, 2, 15, 15, "flex", BONE2)
    z.set_face_colors(GRAY)
    e.add(z)
    def cloud(x, y, z ,r, steps):
        #global e
        for i in range(steps):
            s = Sphere(x, y, z, r, "flex", "white", "white")
            e.add(s)
            x += r/4
    cloud(600, 500, 200, 10, 15)
    cloud(500, 400, 180, 20, 10)
    cloud(500, 400, 210, 10, 10)
    cloud(200, 200, 50, 25, 5)
    cloud(100, 200, 100, 15, 20)
    cloud(700, 600, 135, 23, 10)
