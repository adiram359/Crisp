from Environment import Environment
from random import random

import time
if __name__ == '__main__':
    e = Environment("#D6EAF8", 800, 800)
    e.add("Cube", 400, 400, 400, 50)
    for i in range(20):
        e.add("Pyramid", random()*800, random()*800, random() * 800,  20, 30, 6)
    while True:
        e.render()
