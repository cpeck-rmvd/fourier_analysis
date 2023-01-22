import numpy as np
from scipy import fftpack

# Define a function f in L2(R)
f = lambda x: np.exp(-x**2)

# Compute its Fourier transform F
F = fftpack.fft(f)

# Compute the L2 norm of f and the L_infinity norm of F
L2_norm_f = np.linalg.norm(f, ord=2)
L_infinity_norm_F = np.linalg.norm(F, ord=np.inf)

# Print the results
print(f'L2 norm of f: {L2_norm_f}')
print(f'L_infinity norm of F: {L_infinity_norm_F}')
