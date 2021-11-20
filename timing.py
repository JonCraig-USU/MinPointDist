import datetime
import sys
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import math
from minPoints import createProblem, naiveClosest, closestPair, closestPairR


def naiveTime(n):
    pts = createProblem(n)
    naiveClosest(pts, n)

def recursiveTime(n):
    pts = createProblem(n)
    closestPair(pts, n)

def hybridTime(n):
    pts = createProblem(n)

naiveTL = []
naiveS = []
recursiveTL = []
recursiveS = []
hybridTL = []
hybridS = []

tl = [naiveTL, recursiveTL, hybridTL]
s = [naiveS, recursiveS, hybridS]
funcs = [naiveTime, recursiveTime, hybridTime]

sizes = [2**i for i in range(5, 12)]

def timeFunction(function, time, size):
    for n in sizes:
        startTime = datetime.datetime.now()
        function(n)
        endTime = datetime.datetime.now()
        time_diff = (endTime - startTime)
        elapsed = time_diff.total_seconds() * 1000
        if elapsed > 0: #sometimes the function is too fast and we get 0 time
            time.append(elapsed)
            size.append(n)


plt.xlabel("n")
plt.ylabel("time in milliseconds")
plt.yscale('log')
plt.xscale('log')

plt.plot(naiveS, naiveTL, 'g')
plt.plot(recursiveS, recursiveTL, 'b')
plt.plot(hybridS, hybridTL, 'r')


plt.rcParams["figure.figsize"] = [16,9]
plt.show()

slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in naiveS], [np.log(t) for t in naiveTL])
print("Naive Time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in recursiveS], [np.log(t) for t in recursiveTL])
print("Recursive Time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in hybridS], [np.log(t) for t in hybridTL])
print("Hybrid Time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

