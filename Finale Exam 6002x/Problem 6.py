import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    n = len(choices)
    best = None
    best_sum = -1
    best_count = float('inf')

    for i in range(1 << n):
        bits = bin(i)[2:].zfill(n)
        combo = np.array([int(b) for b in bits])
        current_sum = np.dot(combo, choices)
        count = np.sum(combo)

        if current_sum > total:
            continue

        if (current_sum > best_sum) or (current_sum == best_sum and count < best_count):
            best = combo
            best_sum = current_sum
            best_count = count

    return best


print(find_combination([1,2,2,3], 4))      # [0 1 1 0] lub [1 0 0 1]
print(find_combination([1,1,3,5,3], 5))    # [0 0 0 1 0]
print(find_combination([1,1,1,9], 4))      # [1 1 1 0]
