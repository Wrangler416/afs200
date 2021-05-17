import random 
guesses = 0 
a = random.randint(1, 10)
print("Welcome to the number guessing game, type exit to leave the game")
print("The computer has generated a number between 1 and 10")
while guesses < 10:
    print("Place your guess")
    guess = input()
    guess = int(guess)

    guesses = guesses + 1 
    if guess > a:
            print("Your guess is too high")
    if guess < a: 
            print("Your number is too low")
    if guess == a: 
        break 
if guess == a:
    guesses = str(guesses)
    print("Nice work, you guessed the number!")
    print("Number of guesses: ", guesses)
if guess != a: 
    a = str(a)
    print("Sorry, better luck next time!")

