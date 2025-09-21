import random
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

class TempDatum:
    def __init__(self, s):
        info = s.split(',')
        self.high = float(info[1])
        self.year = int(info[2][:4])

    def getHigh(self):
        return self.high

    def getYear(self):
        return self.year

def getTempData(filename):
    data = []
    with open(filename) as inFile:
        next(inFile)
        for line in inFile:
            if line.strip():
                data.append(TempDatum(line))
    return data

def getYearlyMeans(data):
    years = defaultdict(list)
    for d in data:
        years[d.getYear()].append(d.getHigh())
    return {year: sum(values) / len(values) for year, values in years.items()}

# Funkcja do obliczenia współczynnika determinacji R-kwadrat
def r_squared(y_true, y_pred):
    y_mean = np.mean(y_true)
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    ss_res = sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred))
    return 1 - ss_res / ss_tot

# Dzieli dane na zbiór treningowy i testowy w losowy sposób
def splitData(xVals, yVals):
    toTrain = random.sample(range(len(xVals)), len(yVals) // 2)
    trainX, trainY, testX, testY = [], [], [], []
    for i in range(len(xVals)):
        if i in toTrain:
            trainX.append(xVals[i])
            trainY.append(yVals[i])
        else:
            testX.append(xVals[i])
            testY.append(yVals[i])
    return trainX, trainY, testX, testY

# Wczytanie danych
data = getTempData("data.csv")
years = getYearlyMeans(data)

# Przygotowanie danych do wykresu
xVals, yVals = [], []
for year in sorted(years):
    xVals.append(year)
    yVals.append(years[year])

plt.figure()
plt.plot(xVals, yVals)
plt.xlabel('Year')
plt.ylabel('Mean Daily High (°C)')
plt.title('Select U.S. Cities')
plt.show()

# Liczba prób testowych oraz stopnie wielomianów do dopasowania
numSubsets = 10
dimensions = (1, 2, 3)
rSquares = {d: [] for d in dimensions}

# Trening i testowanie dla każdego stopnia wielomianu
for _ in range(numSubsets):
    trainX, trainY, testX, testY = splitData(xVals, yVals)
    for d in dimensions:
        model = np.polyfit(trainX, trainY, d)           # dopasowanie modelu wielomianowego
        estYVals = np.polyval(model, testX)             # przewidywane wartości
        r2 = r_squared(testY, estYVals)                 # oblicz R-kwadrat
        rSquares[d].append(r2)

# Wyświetlenie średnich i odchyleń standardowych R-kwadrat
print('Mean R-squares for test data:')
for d in dimensions:
    mean = round(sum(rSquares[d]) / len(rSquares[d]), 4)
    std_dev = round(np.std(rSquares[d]), 4)
    print(f'For dimensionality {d}: mean = {mean}, Std = {std_dev}')
