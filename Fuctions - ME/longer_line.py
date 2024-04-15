from math import sqrt
from math import floor


def distance(a1, b1, a2=0, b2=0):
    return sqrt(pow(a2 - a1, 2) + pow(b2 - b1, 2))


def longer_line(a1, b1, a2, b2, a3, b3, a4, b4):
    # line1 -> line btw dot1 & dot2; line2 -> line btw dot3 & dot4
    line_1 = distance(x1, y1, x2, y2)
    line_2 = distance(x3, y3, x4, y4)

    # Every "dist" is a DOT's distance to the center (0,0). Thus, we will find the closest one to it.
    dist_1 = distance(x1, y1)
    dist_2 = distance(x2, y2)
    dist_3 = distance(x3, y3)
    dist_4 = distance(x4, y4)
    if line_1 > line_2:
        if dist_1 <= dist_2:
            return f"({a1}, {b1})({a2}, {b2})"
        return f"({a2}, {b2})({a1}, {b1})"
    elif line_1 < line_2:
        if dist_3 <= dist_4:
            return f"({a3}, {b3})({a4}, {b4})"
        return f"({a4}, {b4})({a3}, {b3})"
    return f"({a1}, {b1})({a2}, {b2})"


x1 = floor(float(input()))
y1 = floor(float(input()))
x2 = floor(float(input()))
y2 = floor(float(input()))
x3 = floor(float(input()))
y3 = floor(float(input()))
x4 = floor(float(input()))
y4 = floor(float(input()))

print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))