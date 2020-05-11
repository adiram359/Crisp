from Environment import Environment
from random import random

import time
if __name__ == '__main__':
    e = Environment("#D6EAF8", 800, 800)
    e.add("Cube", 400, 400, 400, 50)
    for i in range(200):
        e.add("Cube", random()*800, random()*800, random()*800, 10)
    while True:
        e.render()

        #time.sleep(0.01)