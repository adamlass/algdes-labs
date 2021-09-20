import time
import sys
import re
import os
import math

# Printing is life
def pm(*args):
    return ">> "+" | ".join([str(x) for x in args]) + "\n"

# Point is simple a (x,y) coordinate with a name i
class Point():
    def __init__(self,i,x,y):
        self.i=i
        self.x=float(x)
        self.y=float(y)

    def __repr__(self):
        return str(self.x) + ", " + str(self.y) 

# Pair consist of two points, p1 & p2, and the distance between them, d
class Pair():
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.d = d(p1,p2)
    
    def __repr__(self):
        return " | ".join(map(str,(self.d,self.p1,self.p2)))

# Calculates distance between point(a) and point(b)
def d(a,b):
    return math.sqrt(((b.x-a.x)**2) + ((b.y-a.y)**2))

# Brute force closest pair of points
def brute_force(a):
    m = Pair(a[0], a[1])
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            m = min(m, Pair(a[i], a[j]), key=lambda pair: pair.d)
    return m


def closest_pair(x):
    n=len(x)

    # base case
    if n==2: return Pair(x[0], x[1])
    if n==3: return min(Pair(x[0],x[1]), 
                        Pair(x[0],x[2]), 
                        Pair(x[1],x[2]), 
                        key=lambda pair: pair.d)

    # divide
    mid = n//2

    pair_a  = closest_pair(x[:mid])
    pair_b  = closest_pair(x[mid:])
    pair_c  = min(pair_a, pair_b, key=lambda pair: pair.d)
    
    # combine
    delta   = pair_c.d
    delta_s = x[mid].x - delta
    delta_e = x[mid].x + delta
    
    strip = sorted([p for p in x if delta_s <= p.x <= delta_e], key=lambda p: p.y)
    ls = len(strip)
    
    for i in range(ls):
        for j in range(1, 8):
            if i+j >= ls: break
            pair_c = min(pair_c, Pair(strip[i], strip[i+j]), key=lambda pair: pair.d)

    return pair_c

def find_closest_pair(points):
    xs = sorted(points, key=lambda p: p.x)
    return closest_pair(xs)

def main():
    fl = open("../data/pla85900-tsp.txt", "r")
    # fl = open(sys.argv[1], "r")

    lines = re.compile(".* +-?[<\d\.]+[e\+\-\d]* +-?[\d\.]+[e\+\-\d]*").findall(fl.read())
    points = [Point(*line.split()) for line in lines]
    s = time.time()
    res = find_closest_pair(points)
    
    print(pm(res, time.time()-s))


if __name__ == '__main__':
    main()

# rfile = open("res3.txt", "w")
# for filename in os.listdir("data"):
#     f = os.path.join("data", filename)
#     if os.path.isfile(f):
#         s = time.time()
#         fl = open(f, "r")
        
#         lines = re.compile(".* +-?[<\d\.]+[e\+\-\d]* +-?[\d\.]+[e\+\-\d]*").findall(fl.read())
#         points = [Point(*line.split()) for line in lines]
#         res = find_closest_pair(points)

#         fl.close()

#         print(filename)
#         print(pm(res.d, res.p1, res.p2, time.time()-s))
#         rfile.write(pm(filename))
#         rfile.write(pm(res.d, res.p1, res.p2, time.time()-s))
#         rfile.write("\n")




################## KATTIS ##################
# https://itu.kattis.com/submissions/7667805