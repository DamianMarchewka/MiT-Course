import random
import math
import matplotlib.pyplot as plt


class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        # use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]



class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

# The following function is new, and returns the actual x and y distance from the start point to the end point of a random walk.

def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())

# Here are several different variations on a drunk.

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)]
        return random.choice(stepChoices)


########################################################################################


def performWalk(field, drunk, numSteps):
    path = [field.getLoc(drunk)]  # zapisujemy pozycję startową
    for _ in range(numSteps):
        field.moveDrunk(drunk)
        path.append(field.getLoc(drunk))
    return path


# Funkcja wizualizująca ścieżkę jako rozkład punktowy (scatter plot)
def plotWalk(path):
    xs = [loc.getX() for loc in path]
    ys = [loc.getY() for loc in path]

    plt.figure(figsize=(8, 8))
    plt.clf()
    plt.title("Random Walk - Rozkład punktowy PhotoDrunka")

    # Rysujemy każdy krok jako pojedynczy punkt
    plt.scatter(xs, ys, c="blue", s=10, label="Kroki")

    # Oznaczamy punkt startowy oraz końcowy kolorami
    plt.scatter(xs[0], ys[0], c="green", s=100, label="Start")
    plt.scatter(xs[-1], ys[-1], c="red", s=100, label="Koniec")

    plt.xlabel("Współrzędna x")
    plt.ylabel("Współrzędna y")

    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # Inicjalizacja pola oraz instancji PhotoDrunka
    field = Field()
    photo_drunk = PhotoDrunk("Fotodruszek")
    startLocation = Location(0, 0)
    field.addDrunk(photo_drunk, startLocation)

    numSteps = 300  # Liczba kroków spaceru
    path = performWalk(field, photo_drunk, numSteps)

    # Wizualizacja rozkładu punktowego spaceru
    plotWalk(path)