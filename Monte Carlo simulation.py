import random


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''

    successCount = 0

    for _ in range(numTrials):
        balls = ['R'] * 3 + ['G'] * 3
        drawn = random.sample(balls, 3)

        if drawn.count('R') == 3 or drawn.count('G') == 3:
            successCount += 1

    return successCount / numTrials

print(noReplacementSimulation(1000000))