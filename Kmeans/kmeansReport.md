# K-Means report
## Clustering for mosquito populations in space

### Artificial inteligence

      Esteban Quintana Cueto - A01184855
      Javier Rodríguez Caballero López - A01152572

Profesor: Ruben Stranders


### Introduction
In this project we developed the algorithm K-Means from scratch. K-Means is a classification algorithm used to cluster numeric data. With this project we want to classificate meta-populations of mosquitos into populations. At the same time, we'll also make an analysis of the algorithm and mention in which kind of problems this algorithm is useful and in which ones it can come up with wrong results.

### Justification
The challenge was chosen thinking about the global problem of the mosquitos. In this case we have a dataset of mosquito meta-population locations and we want to cluster them in order to ease the visualization of the relation between these populations.

### The algorithm
    1.- Given a number of data points in space
    2.- Select K number of clusters, then randomly place them around the 'plot'.
    3.- Calculate the distances between each data point and the centroids.
    4.- Assign a data point to the closest centroid.
    5.- Recalculate the new cluster using the means of all clustered data points.
    6.- Recalculate distances between data points and centroids.
    7.- When the points doesn't change of cluster anymore, break. Else continue.

### Setting up instructions
After installing Python3, run the following commands from the terminal:

    $ python3 -m pip install jupyter
    $ pip install pandas
    $ pip install numpy
    $ pip install matplotlib

### Analysis
After the implementation of K-Means, we tested the algorithm using the dataset of mosquitoes locations. We clustered the data and evaluated the results. Here's an image of the results:

![alt text](kmeans.PNG "Logo Title")

In this case, we calculated two clusters and the results are correct, the metapopulations are classified in the right way. At first glance we can visualize which are the two clusters without the need for colors.

On the other hand, we also analyze counterexamples in which K-Means can throw incorrect results. Here's one:

![alt text](counterexample.PNG "Logo Title")

In this case, at first glace we can see that there's two clusters, one that is the circle in the middle, and the other one is the circle on the outside. But since K-Means is a non-deterministic algorithm the results may vary and bring wrong results: it may sometimes place the random first random centroids in non-conveninent place, or even there are some problems like this one, where placing the new centroids in the mean of the data points will result in having our data clustered like the one this example.

### Conclusion and future work
