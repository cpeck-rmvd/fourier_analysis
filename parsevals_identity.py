import numpy as np
from scipy.integrate import quad

# Define the function and its period
def f(x):
    return x**2
T = 2*np.pi

# Define the number of terms to use for the Fourier series
N = 100

# Compute the Fourier coefficients
a_n = []
b_n = []
for n in range(1,N+1):
    a_n.append(2/T * quad(lambda x: f(x)*np.cos(n*x), -np.pi, np.pi)[0])
    b_n.append(2/T * quad(lambda x: f(x)*np.sin(n*x), -np.pi, np.pi)[0])

# Compute the integral of the square of the function over the interval
integral = quad(lambda x: f(x)**2, -np.pi, np.pi)[0]

# Compute the sum of the squares of the Fourier coefficients
coefficient_sum = sum([a**2 + b**2 for a,b in zip(a_n, b_n)])

# Check if Parseval's identity holds
if np.isclose(integral, coefficient_sum/T):
    print("Parseval's identity holds")
else:
    print("Parseval's identity does not hold")
