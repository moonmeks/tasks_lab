import sys
import math

def read_circle(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip().split()
        center_x, center_y = float(line[0]), float(line[1])
        radius = float(file.readline().strip())
        return center_x, center_y, radius

def read_dots(filename):
    dots = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            dots.append((x, y))
    return dots

def dot_position(center_x, center_y, radius, dot):
    dist = math.sqrt((dot[0] - center_x)**2 + (dot[1] - center_y)**2)
    if dist == radius:
        return 0
    elif dist < radius:
        return 1
    else:
        return 2

if __name__ == '__main__':
    if len(sys.argv) == 3:
        center_x, center_y, radius = read_circle(sys.argv[1])
        dots = read_dots(sys.argv[2])

        for dot in dots:
            pos = dot_position(center_x, center_y, radius, dot)
            print(pos)
    else:
        print('Error: expected 3 arguments')