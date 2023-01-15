import numpy as np
import matplotlib.pyplot as plt

# Define the function and its period
def f(x):
    return x**2
T = 2*np.pi

# Define the Fourier series of the function using the first N terms
N = 10
a_n = []
b_n = []
for n in range(1,N+1):
    a_n.append(2/T * integrate(f(x)*cos(n*x), (x, -np.pi, np.pi))[0])
    b_n.append(2/T * integrate(f(x)*sin(n*x), (x, -np.pi, np.pi))[0])

# Define a set of arbitrary coefficients
a_n_prime = [np.random.rand() for _ in range(N)]
b_n_prime = [np.random.rand() for _ in range(N)]

# Define the function represented by the arbitrary coefficients
f_prime = lambda x: (a_n_prime[0]/2 + sum([a_n_prime[i]*np.cos(i*x) + b_n_prime[i]*np.sin(i*x) for i in range(1,N+1)]))

# Check if the function represented by the arbitrary coefficients is equal to the original function
if all([abs(f(x) - f_prime(x)) < 1e-6 for x in np.linspace(-np.pi, np.pi, 1000)]):
    print("The Fourier series is unique")
else:
    print("The Fourier series is not unique")
