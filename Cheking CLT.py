import random

import pylab

def getMeanAndStd(x):
    mean = sum(x)/float(len(x))
    tot = 0.0
    for i in x:
        tot += (i - mean)**2
    std = (tot/len(x))**0.5
    return mean, std


def plotMeans(numDice, numRolls, numBins, legend, color, style):
    means = []
    for i in range(numRolls//numDice):
        vals = 0
        for j in range(numDice):
            vals += 5*random.random()
        means.append(vals/float(numDice))
    pylab.hist(means, numBins, color = color, label = legend,
               weights = pylab.array(len(means)*[1])/len(means), hatch = style)
    return getMeanAndStd(means)

mean, std = plotMeans(1,1000000, 19, '1 die', 'b', '*')
print('Mean of rolling 1 die =', str(mean) + ',', 'Std =', std)
mean, std = plotMeans(50, 1000000, 19, 'Mean of 50 dice', 'r', '//')
print('Mean of rolling 50 dice =', str(mean) + ',', 'Std =', std)
pylab.title('Rolling Continuoes Dice')
pylab.xlabel('Value')
pylab.ylabel('Probablity')
pylab.legend
pylab.show()