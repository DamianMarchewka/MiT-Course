def getMeanAndStd(x):
    mean = sum(x)/float(len(x))
    tot = 0.0
    for i in x:
        tot += (i - mean)**2
    std = (tot/len(x))**0.5
    # std = (tot / (len(x) - 1)) ** 0.5

    return mean, std

print(getMeanAndStd([0,1,2,3,4,5,6]))
print(getMeanAndStd([3,3,3,3,3,3,3]))
print(getMeanAndStd([0,0,0,3,6,6,6]))
print(getMeanAndStd([3,3,5,7,7]))
print(getMeanAndStd([1,5,5,5,9]))