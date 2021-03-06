import datetime
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


def timeFunction(function, time, size, sizes, color):
    for n in sizes:
        startTime = datetime.datetime.now()
        function(n)
        endTime = datetime.datetime.now()
        time_diff = (endTime - startTime)
        elapsed = time_diff.total_seconds() * 1000
        # print(n)
        # print(time)
        if elapsed > 0: #sometimes the function is too fast and we get 0 time
            time.append(elapsed)
            size.append(n)

    plt.plot(size, time, color)

    slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in size], [np.log(t) for t in time])
    print(str(function) + " = %.6f n ^ %.3f" % (np.exp(intercept), slope))

def buildGraph():
    plt.xlabel("n")
    plt.ylabel("time in milliseconds")
    plt.yscale('log')
    plt.xscale('log')



    plt.rcParams["figure.figsize"] = [16,9]
    plt.show()

# slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in naiveS], [np.log(t) for t in naiveTL])
# print("Naive Time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

# slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in recursiveS], [np.log(t) for t in recursiveTL])
# print("Recursive Time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

# slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in hybridS], [np.log(t) for t in hybridTL])
# print("Hybrid Time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

