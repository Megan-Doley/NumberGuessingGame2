import random

def play_game():
    number = random.randint(1, 100)
    guess = None
    tries = 0

    print("Welcome to Number Guessing Game 2!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            tries += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {tries} tries.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play_game()
