Statistical Foundation for Machine Learning (Dr. Karan Nathwani)


Linear Equations 

    - Disadvantace of closed 

    Vector in Regression 

        - 




Lp NORM 


Linear Regression 

    - L2 Norm
    - L3 Norm 
    - Regularize 




Loss Function 

Regularizer 

        - To prevent Overfitting 
        - 


ANgle Between Vectors 

- 


Efficiency of Diagonal Matrix 




-----------------------------

- Unit Vector 

    - A vector with Unit Norm 

- Orthogonal Vectors 

    - A vector X and a vector y are orthogonal to each other 


- Orthonormal Vectors

    - Vectors are orthogonal and have unit norm 
    
    - Orthogonal Matrix 
        - A square matrix whose rows are mutually orthogonal 


- Matrix Decomposition 

    - Matrices can be decomposed into factors to learn universal propertiers 
        - Just like integers
            - Decomposition of integer

            - Decomposition of matrix 

                - Eigen vectors 
                - Eigen values 

Eigenvector 

    - 


Suppose that matrix A has n linearly independent eigenvectors 

Concatenate eigen vectors to form matrix V

Concatenate eigenvalues to form vector 

Eigendecomposition of A is given by



Positive definite matrix 

- When eigne values are more than zero and 
    - positive semidefinite
- If Eigen values are all negative 
    - Positive definite matrices guarantee 

SVD(Singular Value Decomposition)

- SVD is applied is when our matrix is not Square
- A = UDV^t




Psuedo Inverse


Moore-Penrose Pseudoinverse


Trace of a Matrix

Frobenius norm 

Determinanent of a matrix 

PCA (Principal Component Analysis)

Probability 


Random Variable is a mapping function from the space U onto real number 

If U has a space E1 , E2 , E3 ....


Posterior = Pior X Likelihood 


Baysian theorm , 
    - Prior
    - Basis
    - Variance 
    - Covariance 


Data augmentation 

    - adding more evidences 
    - Increasing the data 
    - synthetic data
    - 

Markov Chain Monte Carlo 

    - Variational Bayes


Closed form solution 

    - Gausian 
    - Bernauli distribution 

Metro polis hashing 

P(w/D) = Likelihood X Prior

Multivariant distribution 

    - 



[0:03 pm, 02/07/2023] Shivam Sharma Iit Jammu: Write equation of individual components, integrate and use log as well
[0:03 pm, 02/07/2023] Shivam Sharma Iit Jammu: What individual comports mean and variance ??

[0:04 pm, 02/07/2023] Koustav Ghosh Iit Jammu: Normal distribution will come up
[0:04 pm, 02/07/2023] Koustav Ghosh Iit Jammu: From the probability function you need to get it




Entropy 

H = -I 
H = -log_base_2(p) where p 0<p<1
Range 0 <  H < Infinity

H = 1 = 0  at p =1 

The reason why is logarithimic , it makes the product into summation .

Total information is 

Imn = log_2(pm pn) = log_2(pm) + log_2(pn)

                   = Im + In


example , 26 letters of the alphabet .

Find H(x) = all of them are equiprobable . 

Ensimble of entropy . 



