import numpy as np
import matplotlib.pyplot as plt

# Define the series
coefficients = [1,1,1,1,1,1,1,1,1,1,...] 

# Define the number of terms to use for the Cesàro means
n = 100

# Compute the partial sums of the series
s = np.cumsum(coefficients)

# Compute the Cesàro means
cesaro_means = [np.mean(s[:i]) for i in range(1, n+1)]

# Check if the Cesàro means converge
if all(np.isclose(cesaro_means[0], cesaro_means[i]) for i in range(1, n)):
    print("The series is Cesàro summable")
    cesaro_sum = cesaro_means[0]
else:
    print("The series is not Cesàro summable")
    cesaro_sum = None

# Plot the Cesàro means
plt.plot(range(1,n+1), cesaro_means)
plt.xlabel("Number of terms")
plt.ylabel("Cesàro means")
