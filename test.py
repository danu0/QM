import numpy as np
from scipy import integrate

y = lambda x : np.cos(x)
integral = integrate.quad(y, -1,1)
print(integral)