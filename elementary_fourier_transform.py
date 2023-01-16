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

# Compare the original function and the Fourier series
x_values = np.linspace(a, b, 1000)
plt.plot(x_values, f(x_values), label='Original function')
plt.plot(x_values, s_n(x_values), label='Fourier series')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
