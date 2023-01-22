import numpy as np
from scipy.integrate import quad

def fourier_stieltjes(g, w):
    """
    Calculate the Fourier-Stieltjes Transform of a function g at a point w.
    """
    integrand = lambda t: g(t)*np.exp(-1j*w*t)
    return quad(integrand, -np.inf, np.inf)[0]
