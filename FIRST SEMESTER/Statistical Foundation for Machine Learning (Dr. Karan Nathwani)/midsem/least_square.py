
from warnings import warn

import numpy as np
#from scipy.linalg.fblas import dgemm
from scipy.linalg.blas import dgemm


def linear_least_squares(a, b, residuals=False):
    if type(a) != np.ndarray or not a.flags['C_CONTIGUOUS']:
        warn('Matrix a is not a C-contiguous numpy array.')

    a = np.asarray(a, order='c')
    i = dgemm(alpha=1.0, a=a.T, b=a.T, trans_b=True)
    x = np.linalg.solve(i, dgemm(alpha=1.0, a=a.T, b=b)).flatten()

    if residuals:
        return x, np.linalg.norm(np.dot(a, x) - b)
    else:
        return x


if __name__ == "__main__":
    x = np.array([0, 0.25, 1.0, 1.5, 2.0,2,5], float)	# x-values
    y = np.array([0, 0.25, 1.0, 2.25, 4.0,6,25], float)	# y-values (actual)

    A = np.vstack([x, np.ones(len(x))]).T
    A = np.asarray(A, order='c')

    m, c = linear_least_squares(A, y)

    print( m, c)

    import matplotlib.pyplot as plt

    plt.plot(x, y, 'o', label='Original data', markersize=10)
    plt.plot(x, m * x + c, 'r', label='Fitted line')
    plt.legend()
    plt.show()
