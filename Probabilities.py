import random

def probability(space, event):
    return len(event) / len(space)

def chek_prime(number):
    if number != 1:
        for factor in range(2, number):
            if number % factor == 0:
                return False
    else:
        return False
    return True

if __name__ == '__main__':
    space = set(range(1, 21))
    primes = []
    for num in space:
        if chek_prime(num):
            primes.append(num)
    event= set(primes)
    p = probability(space, event)
    print('Przestrzeń próbek lospowych: {0}'.format(space))
    print('Zdarzenie: {0}'.format(event))
    print('Prawdopodobieństwo wyrzucenia liczby pierwszej: {0:5f}'.format(p))
