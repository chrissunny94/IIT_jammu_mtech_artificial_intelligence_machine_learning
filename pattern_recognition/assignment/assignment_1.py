import statistics
import numpy as np

from scipy.stats import multivariate_normal 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# initializing list
x1w1 = [2.1,1.1,1.4,3.3]
x1w2 = [4.4,3.4,4.5,4.1]
x1w3 = [-1.3,-3.2,-3.2,-2.1]
x2w1 = [-2.5,-3.1,-2.1,-1.8]
x2w2 = [6.5,5.8,7.2,5.65]
x2w3 = [-2.3,-4.5,-4.5,-3.3]
#Find Mean for x1 & x2 classes
x1 = [2.1,1.1,1.4,3.3,4.4,3.4,4.5,4.1,-1.3,-3.2,-3.2,-2.1]
x2 = [-2.5,-3.1,-2.1,-1.8,6.5,5.8,7.2,5.65,-2.3,-4.5,-4.5,-3.3]
# using mean() to calculate average of list of elements
print ("Mean( x1 for w1) : ",end="")
print (statistics.mean(x1w1))
print ("Mean( x1 for w12) : ",end="")
print (statistics.mean(x1w2))
print ("Mean( x1 for w3) : ",end="")
print (statistics.mean(x1w3))
print ("Mean( x2 for w1) : ",end="")
print (statistics.mean(x2w1))
print ("Mean( x2 for w2) : ",end="")
print (statistics.mean(x2w2))
print ("Mean( x2 for w3) : ",end="")
print (statistics.mean(x2w3))
print ("Mean(x1 class) : ",end="")
print (statistics.mean(x1))
print ("Mean(x2 class) : ",end="")
print (statistics.mean(x2))


#Q,2.(b). Use numpy.cov() to compute covariance matrix Σ for each class Σ1, Σ2,␣ ↪Σ3.
####Covariance of each class for 3 ws: E1 E2 E3 # Python code to demonstrate the use of numpy.cov import numpy as np
x1w1 = [2.1,1.1,1.4,3.3]
x1w2 = [4.4,3.4,4.5,4.1]
x1w3 = [-1.3,-3.2,-3.2,-2.1]
x2w1 = [-2.5,-3.1,-2.1,-1.8]
x2w2 = [6.5,5.8,7.2,5.65]
x2w3 = [-2.3,-4.5,-4.5,-3.3]



print("Covariance matrix of x1w1 is :\n", np.cov(x1w1)) 
print("Covariance matrix of x1w2 is :\n", np.cov(x1w2)) 
print("Covariance matrix of x1w3 is :\n", np.cov(x1w3)) 
print("Covariance matrix of x2w1 is :\n", np.cov(x2w1)) 
print("Covariance matrix of x2w2 is :\n", np.cov(x2w2)) 
print("Covariance matrix of x2w3 is :\n", np.cov(x2w3)) 
print("Shape of array of x1 is :\n", np.shape(x1)) 
print("Shape of array of x2 is :\n", np.shape(x2)) 
print("Covariance matrix of x1 is :\n", np.cov(x1)) 
print("Covariance matrix of x2 is :\n", np.cov(x2))

# Defining the data in matrix form
X1 = np.array([[2.1,1.1],[1.4,3.3],[-2.5,-3.1],[-2.1,-1.8]]) #X1 is same as W1 
X2 = np.array([[4.4,3.4],[4.5,4.1],[6.5, 5.8],[7.2, 5.65]]) #X2 same as W2
X3 = np.array([[-1.3,-3.2],[-3.2,-2.1],[-2.3,-4.5],[-4.5, -3.3]]) #X3 same as W3
# Computing the mean vectors for each class
mean1 = np.mean(X1, axis=0)
mean2 = np.mean(X2, axis=0)
mean3 = np.mean(X3, axis=0)
print("The Mean of w1,w2,w3 are:" , mean1,mean2,mean3)
# Computing the covariance matrices for each class
cov1 = np.cov(X1.T)
cov2 = np.cov(X2.T)
cov3 = np.cov(X3.T)
print("The variance of w1,w2,w3 are:" , (cov1,cov2,cov3))
# Defining the prior probabilities for each class
p1 = 0.4
p2 = 0.35
p3 = 0.25
# Defining the discriminant functions for each class
def discriminant(x):
    g1 = multivariate_normal(mean=mean1, cov=cov1).logpdf(x) + np.log(p1) 
    g2 = multivariate_normal(mean=mean2, cov=cov2).logpdf(x) + np.log(p2) 
    g3 = multivariate_normal(mean=mean3, cov=cov3).logpdf(x) + np.log(p3) 
    return g1, g2, g3
# Computing and plotting the discriminant functions and sample points in x1 &␣ ↪x2.
x1 = np.linspace(-5, 10, 100)
y1 = np.linspace(-10, 10, 100)


X1,Y1 = np.meshgrid(x1,y1)
x2 = np.linspace(-5, 10, 100)
y2 = np.linspace(-10, 10, 100)
X2,Y2 = np.meshgrid(x2,y2)
#Define Z1,Z2,Z3 before loop starts
Z1,Z2,Z3 = np.zeros((100,100)),np.zeros((100,100)),np.zeros((100,100))
#For loop to read discriminate function for g1,g2,g3
for i in range(100): 
    for j in range(100):
        x = [X2[i,j], Y2[i,j]]
        g1,g2,g3 = discriminant(x)
        Z1[i,j] = g1
        Z2[i,j] = g2
Z3[i,j] = g3
#This will print an array of discriminant function values for each sample in␣ ↪the input data.
g_values = discriminant(x)
print("Prints the discriminant functions for case-3 for g1,g2,g3 are:",g_values)
#Plotting commands
fig=plt.figure(figsize=(15,5))
#Uncomment this sample Points and comment the below one , else if you keep same␣ ↪for both Discrete function & Sample space.
ax=fig.add_subplot(151)
ax.scatter(X1[:,0], X1[:,1], color='r')
ax.scatter(X2[:,0], X2[:,1], color='g')
ax.scatter(X3[:,0], X3[:,1], color='b')
ax.plot(X2,Y2,Z1-Z2)
ax.plot(X2,Y2,Z1-Z3)
ax.plot(X2,Y2,Z2-Z3)
ax.set_title('Discriminant Function and Sample Space')
'''
ax=fig.add_subplot(131)
ax.contour(X2,Y2,Z1-Z2,[0])
ax.contour(X2,Y2,Z1-Z3,[0])
ax.contour(X2,Y2,Z2-Z3,[0])
ax.scatter(X1[:,0], X1[:,1], color='r')
ax.scatter(X2[:,0], X2[:,1], color='g')
ax.scatter(X3[:,0], X3[:,1], color='b')
ax.set_title('Discriminant Functions')
'''

ax=fig.add_subplot(132)
ax.scatter(X1[:,0], X1[:,1], color='r')
ax.scatter(X2[:,0], X2[:,1], color='g')
ax.scatter(X3[:,0], X3[:,1], color='b')
ax.set_title('Sample---Points')

ax=fig.add_subplot(133, projection='3d')

ax.plot_surface(X2,Y2,Z1-Z2)
ax.plot_surface(X2,Y2,Z1-Z3)
ax.plot_surface(X2,Y2,Z2-Z3)

ax.set_title('Discriminant Function and 3D Plot')

#Below function to plot the graph
plt.show()