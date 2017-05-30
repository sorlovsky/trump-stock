import numpy as np
import matplotlib.pyplot as plt

rand = np.random.rand(10)
ones = np.ones((10,2))
ones[:,1] = ones[:,1] - rand
ones[:,0] = rand

point = np.array([.5,.5])
plt.scatter(ones[:,0], ones[:,1])
plt.scatter(point[0], point[1])
plt.title('KNN To Find Magnitude')
plt.ylabel('Negative Likelihood Estimate')
plt.xlabel('Positive Likelihood Estimate')
plt.show()