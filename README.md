# MinPointDist
Advanced algorithms assignment 8

Starter code located in the dicussion board

# Requirements

For this assignment we will implement a series of algorithms that all solve the following problem:

Given a list of two-dimensional points in an arbitrary order, Find the minimum distance between all pairs of points in the list.

Once you have each algorithm returning the same answer over a set of smaller problems, perform a timing study that will compare the performance of the algorithms. Here we are interested not just in the slope of the line on the log-log graph (the power of n), but also when the two algorithm's run time crosses on the graph.

Do the following:

1) Implement a problem generator that takes n as an input and outputs n randomly located points in a 100 by 100 square region (use floats for coordinates) <mark>(10 points)</mark><br>
-       [100*random.random(), 100*random.random()]

2) Implement the simple 2 nested loop algorithm <mark>(10 points)</mark>

3) Implement the D and C algorithm that avoids the n^2 work per call by sorting by y that we discussed in class. <mark>(20 points)</mark>

4) Write some testing code that repeatedly creates a random problem of (say 2^10) and checks that for each problem, the two algorithms return exactly the same answer <mark>(10 points)</mark>

5) Produce a timing study comparing the run times of the two algorithms as a function of the problem size. This time, run 10 random problems of the same size (n) and take the average of the run time to get the point on the graph. This way our graphs should be less bumpy. Identify the size of n when the recursive algorithm becomes quicker than the n^2 algorithm. Create the plot on a log-log graph as before. <mark> (10 points)</mark>

6) Now implement a hybrid algorithm that modifies the recursive algorithm by switching to the simple n^2 algorithm once the problem size has got small enough. Here add an additional case before the first base case that checks whether n (the number of points) is less than some threshold, then return the result of calling the simple n^2 algorithm. Determine the threshold value from the timing study graph by noting when the run times of the two algorithms cross. <mark>(10 points)</mark>

7) Perform a timing study on this hybrid algorithm and add it to the graph. In what way is the hybrid algorithm faster? Does it change the slope of the line or the offset from the line? <mark> (10 points)</mark>

>> Always use a power of two for the number of points.