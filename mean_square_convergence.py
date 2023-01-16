import numpy as np

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

# Compute the n-th partial sum of the Fourier series
s_n = lambda x, n: (a_n[0]/2 + sum([an[i]np.cos(ix) + b_n[i]np.sin(ix) for i in range(1,n+1)]))

n_values = range(1, N+1)
mean_square_errors = [np.mean((f(x) - s_n(x, n))**2) for n in n_values]

if all(np.isclose(0, error, atol=1e-6) for error in mean_square_errors):
    print("The series converges in mean-square sense")
else:
    print("The series does not converge in mean-square sense")
