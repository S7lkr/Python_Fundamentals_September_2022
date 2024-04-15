from math import sqrt
from math import floor
# NOTE: every DOT in the coordinate system has two parameters -> (x,y) !!


def distance_to_zero(a1, b1, a2, b2):
    return sqrt(pow(a2 - a1, 2) + pow(b2 - b1, 2))
    # the formula above calculates the distance between two DOTS in a coordinate system.
    # Think of it as 2D grid -> two dimensions (x,y)


x1 = floor(float(input()))
y1 = floor(float(input()))
x2 = floor(float(input()))
y2 = floor(float(input()))

# in this case we are looking for distance between a DOT and the CENTER
dist_1 = distance_to_zero(x1, y1, 0, 0)
dist_2 = distance_to_zero(x2, y2, 0, 0)

if dist_1 <= dist_2:
    print(f"({x1}, {y1})")
else:
    print(f"({x2}, {y2})")