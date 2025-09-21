import numpy as np
import pylab

def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) < 3 or not fields[0].isdigit():
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

def highTemps():
    _, high = loadFile()
    return high

def lowTemps():
    low, _ = loadFile()
    return low


diffTemps = list(np.array(highTemps()) - np.array(lowTemps()))
print(loadFile())

pylab.figure()
pylab.plot(range(1,32), diffTemps)
pylab.show()