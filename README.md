Logistic Regression:

Our main objective for this assignment was to isolate a value that minimized a non linear line over data involving test scores. Utilizing the equation 1/(1 + np.exp(-(beta[0] + beta[1] * hours))) we worked out iterative operations that would try to reduce the error values.  
For our first system written my Mr Edelson, the operation used a guess and check method to reduce the error value within a number of iterations.  As the iterations continue, the alorithm checks in small steps for a local minimum.  Once the value of error is aproximated, it returns the value.  

Our second algorithm written by Mr. Niskin utilized a derivitive approximation to find the tangent line slope that was nearest to zero. Partial derivities taken with respect to Bo and B1 give us two values that can be minimized. One important note in this design is the iternation step must be selected carefully.  If the value is too large, our error value will increase exponentially and bound off to infinity.  If the value is too small, the iterations will take forever to shrink to the point of the local minimum.  

Our last operation utilized an imbeded optimization algorithm in scipy.  This version was removed as it was not part of the assignment and not part of the original goal.  
