from scipy.fft import fft, ifft
import numpy as np

def inverse_fourier_transform(fft_image):
    """
    Find the inverse of a given Fourier Transform.

    Parameters:
        fft_image (numpy array): The input Fourier Transform.

    Returns:
        inverse_fft_image (numpy array): The inverse of the input Fourier Transform.
    """
    inverse_fft_image = np.real(ifft(fft_image))
    return inverse_fft_image

# Example usage:

# Input image
image = np.random.rand(3,3)
# Perform Fourier Transform
fft_image = fft(image)
# Find Inverse Fourier Transform
inverse_fft_image = inverse_fourier_transform(fft_image)
print(inverse_fft_image)
