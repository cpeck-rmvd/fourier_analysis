import numpy as np

# Define the Weierstrass function
def weierstrass(z):
    return sum(np.abs(np.sin(3**k*np.pi*z))/(3**k) for k in range(100))

# Define the number of terms to use for the Fourier series
N = 100

# Compute the Fourier coefficients
a_n = []
b_n = []
for n in range(1,N+1):
    a_n.append(1/np.pi * quad(lambda x: weierstrass(x)*np.cos(n*x), -np.pi, np.pi)[0])
    b_n.append(1/np.pi * quad(lambda x: weierstrass(x)*np.sin(n*x), -np.pi, np.pi)[0])

# Compute the Fourier series
s_n = lambda z: sum(a_n[i]*np.cos(i*z) + b_n[i]*np.sin(i*z) for i in range(N))

