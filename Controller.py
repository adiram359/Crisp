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
    e = Environment("#FCF3CF", 800, 800)
    # a = Prism(400, 400, 600, 40, 40, 100,"block")
    # e.add(a)

    # p = SpecialObjects.Arch(400, 400, 400, 20, 50, 50, 50, "flex")
    # e.add(p)
    # p.rotate_in_place_z(math.pi/2)
    # p.rotate_in_place_y(math.pi/2)
    # cube = Cube(400, 400, 400, 40, "flex")
    # s = Sphere(400, 400, 480, 30,"flex", "#D2B4DE")
    # for i in range(10):
    #     c = Cube(random() * 800, random() * 800, random() * 800, random() * 20, "flex")
    #     c.set_face_colors(MEDIUMAQUAMARINE, SEAGREEN, LIGHTGREEN, MEDIUMAQUAMARINE, FORRESTGREEN,MEDIUMAQUAMARINE, SEAGREEN, LIGHTGREEN, MEDIUMAQUAMARINE, FORRESTGREEN)
    #     e.add(c)
    # e.add(s)
    # cube.set_face_colors(MEDIUMAQUAMARINE, SEAGREEN, LIGHTGREEN, MEDIUMAQUAMARINE, FORRESTGREEN)
    #Demos.bridge(e)
    #Demos.house_and_cactus(e)
    #Demos.tower(e)
    #Demos.storm(e)
    Demos.capitol_hill(e)


        #e.render()
    #e.rotate_all_y(math.pi/2)
    e.rotate_all_z(-math.pi/2)
    def y():
        theta = 0
        while theta < math.pi/4:
            theta = theta + 0.01
            e.rotate_all_y(abs(math.sin(theta)) * math.pi / 100)
            # e.rotate_all_z(abs(math.sin(theta)) * math.pi / 100)
            # e.rotate_all_x((math.sin(theta + 3 * math.pi/2) + 1)*math.pi/200)

            # e.all_objects[0].rotate_z(math.pi/32)
            e.render()
        while theta > 0:
            theta = theta - 0.01
            e.rotate_all_y((math.sin(-theta)) * math.pi / 100)
            # e.rotate_all_z(abs(math.sin(theta)) * math.pi / 100)
            # e.rotate_all_x((math.sin(theta + 3 * math.pi/2) + 1)*math.pi/200)

            # e.all_objects[0].rotate_z(math.pi/32)
            e.render()


    def x():
        theta = 0
        while theta < math.pi:
            theta = theta + 0.01
            # e.rotate_all_y((math.sin(theta + 3 * math.pi/2) + 1)*math.pi/200)
            e.rotate_all_z(abs(math.sin(theta)) * math.pi / 100)
            # e.rotate_all_x((math.sin(theta + 3 * math.pi/2) + 1)*math.pi/200)

            # e.all_objects[0].rotate_z(math.pi/32)
            e.render()


    def z():
        theta = 0
        while theta < math.pi/4:
            theta = theta + 0.01
            # e.rotate_all_y((math.sin(theta + 3 * math.pi/2) + 1)*math.pi/200)
            e.rotate_all_x(abs(math.sin(theta)) * math.pi / 100)
            # e.rotate_all_x((math.sin(theta + 3 * math.pi/2) + 1)*math.pi/200)

            # e.all_objects[0].rotate_z(math.pi/32)
            e.render()
    while True:
        e.render()
        #e.canvas.create_arc(100, 100, 200, 200)
        #e.top.update()
        x()
        #y()

    # z()
    # y()
    # z()
    # x()
    # y()
    # z()
