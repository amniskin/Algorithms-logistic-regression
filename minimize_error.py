#!/Users/edelsonc/anaconda/bin/python
"""

author: edelsonc
created: 10/04/2016
"""
from itertools import product
import numpy as np


def errorFunc(beta):
    """
    Gives the sum of the squares of our error function, which is the logistic
    function

    Arguments
    ---------
    beta -- array of parameters
    """
    err = passed - 1/(1 + np.exp(-(beta[0] + beta[1] * hours)))
    return sum(err**2)


def minimum_error(func, beta, df = 0.01, tol = 0.00001):
    """
    Finds a local minimum by guessing and checking in the area surrounding the
    point with a predefined stepsize

    Arguments
    ---------
    func -- error function to min
    beta -- array of parameters
    df -- step size, default of 0.01
    tol -- tolerance, default of 0.00001 ( not necessary currently )
    """
    error = func(beta)
    counter = 1
    while error > tol and counter < 10**5:
        counter += 1
        beta_x = [beta[0] - df, beta[0] + df]
        beta_y = [beta[1] + df, beta[1] - df]
        beta_list = list(product(beta_x, beta_y))

        for tuple in beta_list:
            error_new = func(tuple)
            if error_new < error:
                error = error_new
                beta = tuple

    return beta

if __name__ == "__main__":
    hours = np.array([0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50])
    passed = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

    min_b = minimum_error(errorFunc, [1,1], 0.001,)

    for i in min_b:
        print(i)
