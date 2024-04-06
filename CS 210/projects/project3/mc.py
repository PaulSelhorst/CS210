def pi_mc(num_darts: int) -> float:
    """Return the approximate value of pi using the Monte Carlo method.

    num_darts is the number of darts to throw.
    """
    import random
    import math
    random.seed(42)
    num_darts_in_circle = 0
    for n in range(num_darts):
        x = random.random()
        y = random.random()
        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            num_darts_in_circle += 1
    pi = num_darts_in_circle / num_darts * 4
    return pi
