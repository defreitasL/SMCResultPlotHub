import numpy as np

def wMOORE(D50):
    """
    Fall velocity based on Moore (1982) formula.

    Parameters:
    - D50 (float): Particle diameter in meters.

    Returns:
    - float: Fall velocity.
    """
   
    if D50 <= 0.1 * 1e-3:
        return 1.1 * 1e6 * D50**2
    elif 0.1 * 1e-3 < D50 < 1 * 1e-3:
        return 273 * D50**1.1
    elif D50 >= 1 * 1e-3:
        return 4.36 * D50**0.5

def Hunt(Hs, Tp):
    """
    Calculates wave number based on Hunt formula.

    Parameters:
    - Hs (float): Significant wave height.
    - Tp (float): Wave period.

    Returns:
    - float: Wave number.
    """
    g = 9.81
    a = [0.66667, 0.35555, 0.16084, 0.06320, 0.02174, 0.00654, 0.00171, 0.00039, 0.00011]
    sigma = 2. * np.pi / Tp
    w = sigma**2. / g
    y = w * Hs
    k1 = y + 1. / (1. + a[0] * y + a[1] * y**2. + a[2] * y**3. + a[3] * y**4. + a[4] * y**5. +
                  a[5] * y**6. + a[6] * y**7. + a[7] * y**8. + a[8] * y**9.)
    k = np.sqrt(w * k1 / Hs)
    return 2. * np.pi / k

def memclear():
    """
    Clears the memory using garbage collection.
    """
    import gc   # garbage collector
    cleared = gc.collect()
