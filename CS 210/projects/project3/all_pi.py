import math
from arch import pi_arch
from mc import pi_mc
from wallis import pi_wallis

def all_pi(err_tol: float) -> list:
    """
    Calculates the values of pi using different methods until the difference between the calculated value and math.pi
    is less than the specified error tolerance.

    Parameters:
    - err_tol (float): The maximum allowed difference between the calculated value of pi and math.pi.

    Returns:
    - list: A list containing the number of sides for Archimedes' method, the number of pairs for Wallis' method,
      and the number of darts for Monte Carlo method.
    """
    
    pi1 = math.pi
    num_sides = 1
    num_darts = 1
    num_pairs = 1

    while True:
        if abs(pi1 - pi_arch(num_sides)) < err_tol:
            break
        elif abs(pi1 - pi_arch(num_sides)) > err_tol:
            num_sides += 1
    while True:
        if abs(pi1 - pi_mc(num_darts)) < err_tol:
            break
        elif abs(pi1 - pi_mc(num_darts)) > err_tol:
            num_darts += 1
    while True:
        if abs(pi1 - pi_wallis(num_pairs)) < err_tol:
            break
        elif abs(pi1 - pi_wallis(num_pairs)) > err_tol:
            num_pairs += 1

    pi2 = pi_arch(num_sides)
    pi3 = pi_mc(num_darts)
    pi4 = pi_wallis(num_pairs)

    print(f"Archimedes: num_sides = {num_sides} (Differs by {abs(pi1 - pi2)})")
    print(f"Wallis: num_pairs = {num_pairs} (Differs by {abs(pi1 - pi4)})")
    print(f"Monte Carlo: num_darts = {num_darts} (Differs by {abs(pi1 - pi3)})")
    
    return [num_sides, num_pairs, num_darts]

print(all_pi(0.1))