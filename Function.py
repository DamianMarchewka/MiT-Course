def f(x):
    x = x + 1
    print('in f(x): x =', x )
    return x
x = 3
z = f(x)
########################################################################################################################
def is_even(i):
    """
    input is a positive int
    Does not return anyithing
    """
    i % 2 == 0
print(is_even(2))
# Python returns the value None, if no return given
########################################################################################################################

def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2
print(f)
print(type(f))

########################################################################################################################
# Keyword arguments amd default values

def print_Name(first_Name, last_Name, reverse = False):
    if reverse:
        print(last_Name + " " + first_Name)
    else:
        print(first_Name + " " + last_Name)

print_Name("Damian", "Marchewka")
print_Name("Damian", "Marchewka", reverse = True)

########################################################################################################################
# Iterative function

def iterPower(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

# Examples:
print(iterPower(2, 3)) # Output: 8
print(iterPower(5, 4)) # Output: 625
print(iterPower(3.5, 2)) # Output: 12.25

########################################################################################################################
# Reccurant function

def recurPower(base, exp):
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

########################################################################################################################
# Reccurent function, check if string is a palindrome using bisection method.

def isIn(char, aStr):
    if aStr == "":
        return False
    if len(aStr) == 1:
        return aStr == char

    mid_index = len(aStr) // 2
    mid_char = aStr[mid_index]

    if char == mid_char:
        return True
    elif char < mid_char:
        return isIn(char, aStr[:mid_index])
    else:
        return isIn(char, aStr[mid_index + 1:])


# Example usage:
print(isIn('a', 'abcdef'))  # True
print(isIn('z', 'abcdef'))  # False

help(f(1, 5))

print(is_even.__doc__)