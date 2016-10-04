from scipy.optimize import leastsq
import numpy as np
import math

hours = np.array([0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50])
passed = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

def dBeta0(beta):
    return sum(2*(passed - 1/(1+np.exp(-(beta[0] + beta[1] * hours)))) * (1 + np.exp(-(beta[0] + beta[1] * hours))) ** (-2))
def dBeta1(beta):
    retVal = sum(2*(passed - 1/(1+np.exp(-(beta[0] + beta[1] * hours)))) * (1 + np.exp(-(beta[0] + beta[1] * hours))) ** (-2) * hours)
    return retVal
def errorFunc(beta):
    return sum((passed - 1/(1 + np.exp(-(beta[0] + beta[1] * hours)))) ** 2)
def betaNew(beta, h):
    beta_new = np.array([beta[0] + h * dBeta0(beta), beta[1] + h * dBeta1(beta)])
    return beta_new

beta = [1,1]
epsilon = 0.05
step = 0.0001
while (dBeta0(beta)** 2 + dBeta1(beta)** 2 ) > epsilon:
    beta = betaNew(beta, step)

#a = leastsq(errorFunc, np.array([1,1]))
print(beta)
#print("")
#print(a)
