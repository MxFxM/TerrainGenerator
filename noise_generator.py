"""
test to generate noise but failed for 2d
"""

import math
import random

maxfreq = 1/500
myfrequencies = [random.random() * maxfreq * 2 * math.pi for _ in range(5)]
myphases = [random.random() * math.pi for _ in range(5)]


def myfunction(x, y):
    global myfrequencies
    global myphases
    start = 1
    for f, p in zip(myfrequencies, myphases):
        start = start * math.sin(f * x + p)
    return int((start + 1) * 127)


x = [n for n in range(display_width)]
y = [myfunction(n, 0) for n in x]
