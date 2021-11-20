import math
import random
from operator import itemgetter

def createProblem(n):
    return [[100*random.random(), 100*random.random()] for _ in range(n)]
X,Y = 0,1
# My distance function (where X = 0 and Y = 1)
def dist(pt0, pt1):
    return math.sqrt((pt0[X]-pt1[X])**2 + (pt0[Y]-pt1[Y])**2)

#Easy way to sort by X or sort by Y in Python
pts = sorted(pts, key=itemgetter(X))

# Naive Algorithm
def naiveClosest(pts, n):
    dmin = 1000000
    for i in range(n):
        for j in range(i, n):
            if dist(pts[i], pts[j]) < dmin:
                dmin = dist(pts[i], pts[j])
    return dmin

# Wrapper for the recursive function
def closestPair(pts, n):
    pts = sorted(pts, key=itemgetter(X))
    closestPairR(pts, n)

#Basic recursive function. You need to fill in the missing parts
def closestPairR(pts, n):
    # if only two points, return the distance
    if n == 2:
        return dist(pts[0], pts[1])
    # solve each sub problem and get the min distance
    dmin = min(closestPairR(pts[:n/2], n/2), closestPairR(pts[n/2:], n/2))

    # find the x coordinate of between the two sides
    xMid = (pts[n//2-1][X]+pts[n//2][X])/2.0

    # find the points in the band around the center
    # bandPts = []

    # scan over all the points collecting those + or - minD around xMid
    bandPts = [pts[i] for i in pts if math.dist(pts[i, X], xMid) < dmin]
    # sort points in band by Y
    bandPts = sorted(bandPts, key=itemgetter(Y))
    # for each point in band, for each of its 6 neightbors
    for i in range(len(bandPts)):
        endPt = min(i+7, len(bandPts))
        for j in range(i+1, endPt):
            dmin = min(math.dist(bandPts[i], bandPts[j]), dmin)
                #update the min distance

    return dmin

# hybrid Algorithm