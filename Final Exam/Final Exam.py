def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    for c in range(n //  20 + 1):
        for b in range(n // 9 + 1):
            remaining = n - (20 * c + 9 * b)
            if remaining >= 0 and remaining % 6 == 0:
                return True
    return False
print(McNuggets(16))
print(McNuggets(15))
print(McNuggets(24))
print(McNuggets(14))
print(McNuggets(5))
print(McNuggets(38))

######################################################################################################################

L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']


def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    if not L1 and not L2:
        return (None, None, None)
    if len(L1) != len(L2):
        return False
    def count_occurrences(lst):
        counts = {}
        for elem in lst:
            if elem in counts:
                counts[elem] += 1
            else:
                counts[elem] = 1
        return counts
    counts1 = count_occurrences(L1)
    counts2 = count_occurrences(L2)

    if counts1 != counts2:
        return False

    max_elem = None
    max_count = 0
    for elem, count in counts1.items():
        if count > max_count:
            max_elem = elem
            max_count = count
    return (max_elem, max_count, type(max_elem))

print(is_list_permutation(L1, L2))

######################################################################################################################

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
                          N unique lowercase letters.
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
        value is the letter in map_to at index i.
        decoded is a string that contains the decoded version
        of code using the key_code mapping. """
    key_code = {map_from[i]: map_to[i] for i in range(len(map_from))}
    decoded = ''.join(key_code[char] for char in code)
    return (key_code, decoded)

result = cipher("abcd", "dcba", "dab")
print(result)  # ({'a': 'd', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')

######################################################################################################################

class myDict(object):
    """ Implements a dictionary without using a dictionary """

    def __init__(self):
        """ initialization of your representation """
        self.data = []

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        for pair in self.data:
            if pair[0] == k:
                pair[1] = v
                return
        self.data.append([k, v])

    def getval(self, k):
        """ k, immutable object  """
        for pair in self.data:
            if pair[0] == k:
                return pair[1]
        raise KeyError("Key ",k, " not found.")

    def delete(self, k):
        """ k, immutable object """
        for i, pair in enumerate(self.data):
            if pair[0] == k:
                del self.data[i]
                return
        raise KeyError("Key " ,k, " not found.")

md = myDict()
md.assign(1, 2)       # Dodanie klucza 1 z wartością 2
print(md.getval(1))   # Pobranie wartości dla klucza 1, wynik: 2
md.assign(1, 3)       # Nadpisanie wartości dla klucza 1
print(md.getval(1))   # Pobranie nowej wartości dla klucza 1, wynik: 3
md.delete(1)          # Usunięcie pary klucz-wartość z kluczem 1

try:
    print(md.getval(1))  # Próba dostępu do usuniętego klucza
except KeyError as e:
    print(e)             # Wyjątek: Key 1 not found
