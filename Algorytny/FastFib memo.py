# The definition with Fib(0) = 1 is known as the combinatorial definition,
# and Fib(0) = 0 is the classical definition.

def fastFib(n, memo = {}):
    """Assume n is an imt >= 0, memo used only by recursive colls
        Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result

for i in range(2):
    print('Fib(' + str(i) + ') =', fastFib(i))