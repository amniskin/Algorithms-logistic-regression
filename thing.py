from scipy.optimize import leastsq
import numpy as np
import math

hours = np.array([0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50])
passed = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

def errorFunc(beta):
    return passed - 1/(1 + np.exp(-(beta[0] + beta[1] * hours)))

a = leastsq(errorFunc, np.array([1,1]))
print(a)
