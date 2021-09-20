import glob
import sys
import time
import math
import copy

arguments = sys.argv
arguments = ["", "data/a280-tsp.txt"]

x_sorter=lambda points: points[0]
y_sorter=lambda points: points[1]

MAX_WITHIN = 15

def distance(p1, p2):
    return math.sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))


def split_points(Px, Py):
    mid = len(Px) // 2

    Qx = Px[:mid]
    Rx = Px[mid:]

    Qy = copy.copy(Qx)
    Ry = copy.copy(Rx)

    Qy.sort(key=y_sorter)
    Ry.sort(key=y_sorter)

    return (Qx, Qy, Rx, Ry)


def closest_pair(points):
    points_x = points
    points_y = copy.copy(points)

    # Sorting the two lists according to x and y coordinates respectively
    points_x.sort(key=x_sorter)
    points_y.sort(key=y_sorter)

    return closest_pair_rec(points_x, points_y)

def get_min_pair(points):
    Px_len = len(points)
    
    min_dist = None
    min_pair = None

    for i in range(Px_len - 1):
        for j in range(i + 1, Px_len):
            cur = points[i]
            other = points[j]
            dist = distance(cur, other)
            
            if(min_dist == None or dist < min_dist):
                min_dist = dist
                min_pair = (cur, other)

    return min_pair

def closest_pair_rec(Px, Py):
    if(len(Px) <= 3):
        return get_min_pair(Px)
        
    (Qx, Qy, Rx, Ry) = split_points(Px, Py)

    closest_pair_left = closest_pair_rec(Qx, Qy)
    closest_pair_right = closest_pair_rec(Rx, Ry)

    left_distance = distance(closest_pair_left[0], closest_pair_left[1])
    right_distance = distance(closest_pair_right[0], closest_pair_right[1])
    delta = min(left_distance, right_distance)

    L = Qx[len(Qx) - 1]

    P = [*Qx, *Rx]

    # Constructing Sy
    Sy = [s for s in P if(s[0] <= ) <= delta]
    Sy.sort(key=y_sorter)
    Sy_len = len(Sy)

    s_min = None
    s_mark_min = None
    s_min_distance = delta


    for i in range(Sy_len - 1):
        s = Sy[i]
        n_checks = min(Sy_len - 1 - i, MAX_WITHIN)
        for j in range(n_checks):
            s_mark = Sy[i + 1 + j]
            s_distance = distance(s, s_mark)

            if(s_distance <= s_min_distance):
                s_min = s
                s_mark_min = s_mark
                s_min_distance = s_distance

    s_distance = distance(s_min,s_mark_min)

    if(s_distance < delta):
        return (s_min, s_mark_min)
    elif(left_distance < right_distance):
        return closest_pair_left
    return None 



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

    # Sorting points on x coordinate
    # print(points)

    cp = closest_pair(points)

    result = distance(cp)

    print(f"../{argument}: {N} {result}")
