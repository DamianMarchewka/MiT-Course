#Bisection algorytm "Guess a number"
low = 0
high = 100
numGuesses = False
print("Please think of a number between 0 and 100!")

while not numGuesses:
    guess = (low + high) // 2
    print("Is your secret number is ", guess)
    feedback = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    while feedback not in ['h', 'l', 'c']:
        print("Sorry I did not understand your input.")
        print("Is your secret number is ", guess)
        feedback = input(
            "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if feedback == "h":
        high = guess
    elif feedback == "l":
        low = guess
    elif feedback == "c":
        print("Game over your secret number is ", guess)
        numGuesses = True