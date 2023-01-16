import numpy as np
from scipy.integrate import quad

# Define the function
def f(x):
    return x**2

# Define the interval
a = -np.pi
b = np.pi

# Define the number of terms to use for the Fourier series
N = 100

# Compute the Fourier coefficients
a_n = []
b_n = []
for n in range(1,N+1):
    a_n.append(1/np.sqrt(2*np.pi)*quad(lambda x: f(x)*np.cos(n*x), a, b)[0])
    b_n.append(1/np.sqrt(2*np.pi)*quad(lambda x: f(x)*np.sin(n*x), a, b)[0])

# Compute the Fourier series
s_n = lambda x: sum(a_n[i]*np.cos(i*x) + b_n[i]*np.sin(i*x) for i in range(N))

# Compute the summation of the function over the integers
sum_f = sum([f(n) for n in range(int(a), int(b)+1)])

# Compute the summation of the Fourier series over the integers
sum_s = sum([s_n(n) for n in range(int(a), int(b)+1)])

# Derive the Poisson summation formula
if np.isclose(sum_f, (b-a)*sum_s):
    print("The Poisson summation formula holds")
else:
    print("The Poisson summation formula does not hold")
