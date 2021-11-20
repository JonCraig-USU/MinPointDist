import math
import random
from operator import itemgetter
import timing as tim

def createProblem(n):
    return [[100*random.random(), 100*random.random()] for _ in range(n)]
X,Y = 0,1
# My distance function (where X = 0 and Y = 1)
def dist(pt0, pt1):
    return math.sqrt((pt0[X]-pt1[X])**2 + (pt0[Y]-pt1[Y])**2)

#Easy way to sort by X or sort by Y in Python
# pts = sorted(pts, key=itemgetter(X))

# Naive Algorithm
def naiveClosest(pts, n):
    dmin = 1000000
    for i in range(n):
        for j in range(i + 1, n):
            if dist(pts[i], pts[j]) < dmin:
                dmin = dist(pts[i], pts[j])
    return dmin

# Wrapper for the recursive function
def closestPair(pts, n):
    pts = sorted(pts, key=itemgetter(X))
    return closestPairR(pts, n)

#Basic recursive function. You need to fill in the missing parts
def closestPairR(pts, n):
    # if only two points, return the distance
    if n == 2:
        return dist(pts[0], pts[1])
    # solve each sub problem and get the min distance
    dmin = min(closestPairR(pts[:n//2], n//2), closestPairR(pts[n//2:], n//2))

    # find the x coordinate of between the two sides
    xMid = (pts[n//2-1][X]+pts[n//2][X])/2.0

    # find the points in the band around the center
    bandPts = []

    # scan over all the points collecting those + or - minD around xMid
    bandPts = [pts[i] for i in range(len(pts)) if  math.dist([pts[i][X]], [xMid]) < dmin] 
    
    # sort points in band by Y
    bandPts = sorted(bandPts, key=itemgetter(Y))
    
    # for each point in band, for each of its 6 neightbors
    for i in range(len(bandPts)):
        endPt = min(i+7, len(bandPts))
        for j in range(i+1, endPt):
            dmin = min(math.dist(bandPts[i], bandPts[j]), dmin)
                #update the min distance
    return dmin

# hybrid wrapper
def hybridWrapper(pts, n):
    pts = sorted(pts, key=itemgetter(X))
    return hybrid(pts, n)

# hybrid Algorithm
def hybrid(pts, n):
    # if only two points, return the distance
    if n <= 2**7:
        return naiveClosest(pts, n)
    
    # solve each sub problem and get the min distance
    dmin = min(hybrid(pts[:n//2], n//2), hybrid(pts[n//2:], n//2))

    # find the x coordinate of between the two sides
    xMid = (pts[n//2-1][X]+pts[n//2][X])/2.0

    # find the points in the band around the center
    bandPts = []

    bandPts = [pts[i] for i in range(len(pts)) if math.dist([pts[i][X]], [xMid]) < dmin]
    
    # sort points in band by Y
    bandPts = sorted(bandPts, key=itemgetter(Y))
    
    # for each point in band, for each of its 6 neightbors
    for i in range(len(bandPts)):
        endPt = min(i+7, len(bandPts))
        for j in range(i+1, endPt):
            dmin = min(math.dist(bandPts[i], bandPts[j]), dmin)
                #update the min distance
    return dmin

# timing study set up

def naiveTime(n):
    pts = createProblem(n)
    naiveClosest(pts, n)

def recursiveTime(n):
    pts = createProblem(n)
    closestPair(pts, n)

def hybridTime(n):
    pts = createProblem(n)
    hybridWrapper(pts, n)
    

# arrays that will be passed in
naiveTL = []
naiveS = []
recursiveTL = []
recursiveS = []
hybridTL = []
hybridS = []

# sizes chosen for each algorithm
sizes1 = [2**i for i in range(8, 15)]
sizes2 = [2**i for i in range(13, 20)]
sizes3 = [2**i for i in range(15, 22)]
allSizes = [sizes1, sizes2, sizes3]

# arrays or the arrays to pass in
tl = [naiveTL, recursiveTL, hybridTL]
s = [naiveS, recursiveS, hybridS]
funcs = [naiveTime, recursiveTime, hybridTime]
color = ['g', 'b', 'r']

# loop for running timimng study
def timingStudy():
    for i in range(3):
        print(tim.timeFunction(funcs[i], tl[i], s[i], allSizes[i], color[i]))
    tim.buildGraph()

# accuracy test
def acc(n):
    for i in range(10):
        print("Accuracy Test " + str(i))
        pts = createProblem(n)
        print(naiveClosest(pts, n))
        print(closestPair(pts, n))


def main():
    timingStudy()
    acc(2**10)

if __name__ == "__main__":
    main()