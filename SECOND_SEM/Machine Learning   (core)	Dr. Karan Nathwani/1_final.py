import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Data points from the question
data = [(4, 9), (9, 1), (3, 5), (1, 2), (12, 5), (2, 3), (14, 7), (5, 10),
        (10, 12), (8, 8), (4, 6), (3, 13), (1, 8), (6, 11)]

# Initial centroids as specified in the question (A2, A7, A15)
centroids = [(9, 1), (14, 7), (6, 11)]

# Function to perform a single iteration of K-means clustering
def kmeans_iteration(data, centroids):
  clusters = [[] for _ in range(len(centroids))]  # List to store cluster assignments

  # Calculate distances and assign points to closest centroids
  for point in data:
    min_distance = float('inf')  # Initialize minimum distance to infinity
    closest_centroid = None
    for centroid in centroids:
      distance = ((point[0] - centroid[0])**2 + (point[1] - centroid[1])**2)**0.5  # Euclidean distance
      if distance < min_distance:
        min_distance = distance
        closest_centroid = centroid
    clusters[centroids.index(closest_centroid)].append(point)

  # Recompute centroids as the mean of points in each cluster
  new_centroids = []
  for cluster in clusters:
    if cluster:  # Check if cluster is empty (no points assigned)
      x_sum, y_sum = 0, 0
      for point in cluster:
        x_sum += point[0]
        y_sum += point[1]
      new_centroids.append((x_sum / len(cluster), y_sum / len(cluster)))
    else:
      # Handle empty clusters (assign original centroid to avoid errors)
      new_centroids.append(centroids[clusters.index(cluster)])

  return clusters, new_centroids

# Perform multiple iterations until centroids converge (you can adjust the number of iterations)
iterations = 3
for i in range(iterations):
  clusters, centroids = kmeans_iteration(data, centroids)

# Print cluster assignments after the final iteration
print("Final Clusters:")
for i, cluster in enumerate(clusters):
  print(f"Cluster {i+1}: {cluster}")

# Optional: Plot the data points and centroids for visualization
colors = ['red', 'green', 'blue']  # Colors for different clusters

plt.scatter([point[0] for point in data], [point[1] for point in data], color=colors[0])  # Plot data points
for i, centroid in enumerate(centroids):
  plt.scatter(centroid[0], centroid[1], color=colors[i], marker='x', label=f"Centroid {i+1}")  # Plot centroids

plt.legend()
plt.title("K-means Clustering Results")
plt.show()

