from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import Birch

# initialize the data set we'll work with
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# define the model
birch_model = Birch(threshold=0.03, n_clusters=2)

# train the model
birch_model.fit(training_data)

# assign each data point to a cluster
birch_result = birch_model.predict(training_data)

# get all of the unique clusters
birch_clusters = unique(birch_result)

# plot the BIRCH clusters
for birch_cluster in birch_clusters:
    # get data points that fall in this cluster
    index = where(birch_result == birch_clusters)
    # make the plot
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# show the BIRCH plot
pyplot.show()