import numpy as np
from matplotlib import pyplot as plt
X= [[0.1,0.6],[0.15,0.71],[0.08,0.9],[0.16,0.85],[0.2,0.3],[0.25,0.5],[0.24,0.1],[0.3,0.2]]
centers = np.array([[0.1,0.6],[0.3,0.2]])
print("Initial Centroid : ",centers)
from sklearn.cluster import KMeans
model = KMeans(n_clusters=2, init=centers, n_init=1)
model.fit(X)
print('Labels :',model.labels_)
print('P6 belongs to cluster : ',model.labels_[5])
print('No. of population around cluster 2 : ',np.count_nonzero(model.labels_== 1))
print('New Centroids :\n',model.cluster_centers_)
new_centers = np.array(model.cluster_centers_)
X=np.array(X)
plt.scatter(X[:,0:1],X[:,1:2], c='orange')
plt.scatter(new_centers[:,0:1],new_centers[:,1:2],c='red')
plt.show()