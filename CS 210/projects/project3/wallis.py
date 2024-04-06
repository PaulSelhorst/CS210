def pi_wallis(num_pairs: int) -> float:
    """
    Calculates an approximation of pi using the Wallis formula.

    Parameters:
    num_pairs (int): The number of pairs of terms to consider in the Wallis formula.

    Returns:
    float: The approximation of pi.

    """
    acc = 1
    num = 2
    for aPair in range(num_pairs):
        leftterm= num / (num-1)
        rightterm= num / (num+1)

        acc = acc * leftterm * rightterm

        num = num + 2
    pi = acc * 2
    return pi
