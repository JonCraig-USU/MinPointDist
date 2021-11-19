import math
import random

def createProblem(n):
    return [[100*random.random(), 100*random.random()] for _ in range(n)]
X,Y = 0,1
# My distance function (where X = 0 and Y = 1)
def dist(pt0, pt1):
    return math.sqrt((pt0[X]-pt1[X])**2 + (pt0[Y]-pt1[Y])**2)

#Easy way to sort by X or sort by Y in Python
from operator import itemgetter
pts = sorted(pts, key=itemgetter(X))

#Basic recursive function. You need to fill in the missing parts
def closestPairR(pts, n):
    # if only two points, return the distance
    if n == 2:
        return dist(pts[0], pts[1])
    # solve each sub problem and get the min distance

    # find the x coordinate of between the two sides
    xMid = (pts[n//2-1][X]+pts[n//2][X])/2.0
    # find the points in the band around the center
    bandPts = []
    # scan over all the points collecting those + or - minD around xMid

    # sort points in band by Y

    # for each point in band, for each of its 6 neightbors

                #update the min distance

    return minD