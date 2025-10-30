import random
import sys
import os

HIGHSCORE_FILE = "text_version/highscore.txt"

def get_high_score():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return None
    return None

def save_high_score(score):
    with open(HIGHSCORE_FILE, "w") as file:
        file.write(str(score))



def play_game():
    number = random.randint(1, 100)
    guess = None
    tries = 0
    max_tries = 10

    high_score = get_high_score()
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"you have {max_tries} guesses.")

    if high_score:
        print(f"Current High Score: {high_score} guesses.")
    else:
        print("No high score yet.")

    while guess != number and tries < max_tries:
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

    if guess != number:
        print(f"you're out of guesses. The number was {number}.")
    else:
        if high_score is None or tries < high_score:
            print("New high score!")
            save_high_score(tries)
        else:
            print(f"your best so far is {high_score} guesses.")


def show_help():
    print("How to PLay:")
    print("A number is randomly selected between 1-100. You have 10 guesses to find it.")


def main_menu():
    while True:
        print("Menu:")
        print("1. Play Game")
        print("2. Help")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            play_game()
        elif choice == "2":
            show_help()
        elif choice == "3":
            print("Goodbye!")
            sys.exit()
        else:
            print("Please enter a valid choice (1-3).")

if __name__ == "__main__":
    main_menu()
