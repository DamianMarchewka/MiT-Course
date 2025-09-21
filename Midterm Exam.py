def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''

    if x < b:
        return 0
    else:
        return 1 + myLog(x // b, b)

print(myLog(16, 2))
print(myLog(15, 3))

########################################################################################################################

listA = [1, 2, 3]
listB = [4, 5, 6]

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    sum = 0
    for a, b in zip(listA, listB):
        sum += a * b
    return sum
result = dotProduct(listA, listB)

print(result)

########################################################################################################################

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keys = [key for key, value in aDict.items() if value == target]
    keys.sort()
    return keys

aDict = {1: 3, 2: 5, 3: 3, 4: 5, 5: 1}
target = 3
print(keysWithValue(aDict, target))

########################################################################################################################

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    result = []

    def flatten_element(element):
        if isinstance(element, list):
            for item in element:
                flatten_element(item)
        else:
            result.append(element)

    flatten_element(aList)
    return result

########################################################################################################################

def applyF_filterG(L, f, g):
    new_L = [i for i in L if g(f(i))]
    L[:] = new_L
    return max(L) if L else -1

def f(i):
    return i + 2

def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)
