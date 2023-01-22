import numpy as np

def poisson_integral(T,z,D):
    """
    Calculate the Poisson integral of a function T at a point z in a region D.

    Parameters:
    T (function): The function T defined and bounded on the boundary of D.
    z (complex number): The point in D where the Poisson integral will be evaluated.
    D (list of complex numbers): The boundary of the region D in the counterclockwise direction.

    Returns:
    float: The Poisson integral of T at the point z.
    """
    integral = 0
    for w in D:
        integral += T(w)/(z-w)
    return 1/(2*np.pi)*integral
