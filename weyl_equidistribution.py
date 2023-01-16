import numpy as np
from scipy.stats import norm

# Define the sequence
x_n = (np.arange(1,1000) * np.pi) % 1

# Define the function
f = lambda x: norm.cdf(x, loc=0.5, scale=0.1)

# Define the number of intervals
N_intervals = 100

# Define the intervals
intervals = np.linspace(0, 1, N_intervals+1)

# Compute the proportion of terms in each interval for different values of n
n_values = range(100, 1000, 100)
proportions = [[np.sum((f(x_n[:n]) >= intervals[i]) & (f(x_n[:n]) < intervals[i+1]))/n for i in range(N_intervals)] for n in n_values]

# Plot the proportion of terms in each interval for different values of n
for i, prop in enumerate(proportions):
    plt.plot(intervals[:-1], prop, label='n = {}'.format(n_values[i]))
plt.xlabel('Interval')
plt.ylabel('Proportion of terms')
plt.legend()
