#  !pip install scikit-learn-extra
from sklearn_extra.cluster import KMedoids
import numpy as np

data = np.asarray([[2, 6], [3, 8], [4, 7], [6, 2], [6, 4], [7, 3], [7, 4], [8, 5], [7, 6], [3, 4]])

k=2
kmedoids = KMedoids(n_clusters=k).fit(data)


clusters = kmedoids.cluster_centers_
medoids_final = data[kmedoids.medoid_indices_]

print(medoids_final)
print(clusters)