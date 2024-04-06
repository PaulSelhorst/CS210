import math

def pi_arch(num_sides: int) -> float:
    """Return the approximate value of pi using the Archimedes method.

    num_sides is the number of sides in the polygon.
    """
    innerAngleB = 360.0/num_sides
    halfAngleA = innerAngleB/2

    oneHalfSidesS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSidesS*2
    polygonCircumference = num_sides*sideS
    
    pi = polygonCircumference/2

    return pi
