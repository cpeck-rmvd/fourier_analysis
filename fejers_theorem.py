import numpy as np
import matplotlib.pyplot as plt

# Define the function and its period
def f(x):
    return x**2
T = 2*np.pi

# Define the number of terms to use for the Fourier series
N = 100

# Compute the partial sums of the Fourier series
a_n = []
b_n = []
for n in range(1,N+1):
    a_n.append(2/T * integrate(f(x)*cos(n*x), (x, -np.pi, np.pi))[0])
    b_n.append(2/T * integrate(f(x)*sin(n*x), (x, -np.pi, np.pi))[0])
s_n = lambda x: (a_n[0]/2 + sum([a_n[i]*np.cos(i*x) + b_n[i]*np.sin(i*x) for i in range(1,n+1)]))

# Compute the Cesàro means of the partial sums
n = 1000
s = [s_n(x) for x in np.linspace(-np.pi, np.pi, n)]
cesaro_means = [np.mean(s[:i]) for i in range(1, n+1)]

# Check if the Cesàro means converge uniformly to f(x)
if all(np.isclose(f(x), cesaro_means[i]) for x in np.linspace(-np.pi,np.pi,1000) for i in range(n)):
    print("Fejér's theorem holds")
else:
    print("Fejér's theorem does not hold")
