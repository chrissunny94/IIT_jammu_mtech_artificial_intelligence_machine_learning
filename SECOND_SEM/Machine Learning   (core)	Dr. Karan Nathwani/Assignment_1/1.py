import matplotlib.pyplot as plt

x = [4,9,3,1,12,2,14,5,10,7,8,4,3,1,6]
y = [9,1,5,2,5,3,7,10,12,5,8,6,13,8,11]

plt.scatter(x, y)
plt.show()


from sklearn.cluster import KMeans

data = list(zip(x, y))
inertias = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()