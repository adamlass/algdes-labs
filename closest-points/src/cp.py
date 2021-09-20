import glob
import sys
import time
import math
import copy

arguments = sys.argv
# arguments = ["", "data/pla85900-tsp.txt"]

def distance(p1, p2):
    return math.sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))

def get_min_of_three(points):
    return min(distance(points[0], points[1]), distance(points[1], points[2]), distance(points[0], points[2]))

def get_points_in_strip(Py, mid, delta):
    return [p for p in Py if p[0] >= mid-delta and p[0] <= mid + delta]

# --------------------------------------------------------------
def closest_pair_rec(Px, Py):
    n = len(Px)

    if(n == 2): return distance(Px[0], Px[1])
    if(n == 3): return get_min_of_three(Px)

    mid_index = n // 2
    midpoint = Px[mid_index]
    
    Qx = Px[:mid_index]
    Qy = copy.copy(Qx)
    Qy.sort(key=lambda x: x[1])

    Rx = Px[mid_index:]
    Ry = copy.copy(Rx)
    Ry.sort(key=lambda x: x[1])

    closest_distance_left = closest_pair_rec(Qx, Qy)
    closest_distance_right = closest_pair_rec(Rx, Ry)

    delta = min(closest_distance_left, closest_distance_right)

    S = get_points_in_strip(Py, midpoint[0], delta)

    for i in range(len(S) - 1):
        to = min(8, len(S) - i)
        for j in range(1, to):
            delta = min(delta, distance(S[i], S[i + j]))

    return delta
# --------------------------------------------------------------
def closest_pair(points):
    points_y = copy.copy(points)

    points.sort(key=lambda points: points[0])
    points_y.sort(key=lambda points: points[1])

    return closest_pair_rec(points, points_y)
# --------------------------------------------------------------

for argument in arguments[1:]:
    N = 0
    result = 0

    f = open(argument)

    points = []

    for line in f:
        line = str(line)

        found = line.find("DIMENSION") != -1

        if(found):
            split = line.split(":")
            N = int(split[1].strip())

        found = line.find("NODE_COORD_SECTION") != -1

        if(found):
            for i in range(N):
                values = tuple([float(x) for x in f.readline().split()][1:])
                points.append(values)
            break

    print(f"../{argument}: {N}",end='')

    t = time.time()
    result = closest_pair(points)
    print(f" {result}")
    print(f"Time: {time.time() - t}")

