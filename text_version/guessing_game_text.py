#I acknowledge the use of ChatGPT (GPT-5, OpenAI) to assist in creating this code.

import random
import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

#adding style constants from colorama
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA

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

    print(f"{CYAN}{BOLD}Welcome to Number Guessing Game!{RESET}")
    print("I'm thinking of a number between 1 and 100.")
    print(f"you have{YELLOW} {max_tries} {RESET} guesses.")

    if high_score:
        print(f"{GREEN}Current High Score: {high_score} guesses.{RESET}")
    else:
        print(f"{MAGENTA}No high score yet.{RESET}")

    while guess != number and tries < max_tries:
        try:
            guess = int(input(f"{BLUE}Enter your guess: {RESET} "))
            tries += 1
            if guess < number:
                print(f"{YELLOW}Too low!{RESET}")
            elif guess > number:
                print(f"{RED}Too high!{RESET}")
            else:
                print(f"{GREEN}Correct! You guessed it in {tries} tries.{RESET}")
        except ValueError:
            print("Please enter a valid number.")

    if guess != number:
        print(f"{RED}you're out of guesses. The number was {number}.{RESET}")
    else:
        if high_score is None or tries < high_score:
            print(f"{GREEN}{BOLD}New high score!{RESET}")
            save_high_score(tries)
        else:
            print(f"{CYAN}your best so far is {high_score} guesses.{RESET}")


def show_help():
    print(f"{YELLOW}{BOLD}How to PLay:{RESET}")
    print("A number is randomly selected between 1-100. You have 10 guesses to find it.")


def main_menu():
    while True:
        print("Menu:")
        print("1. 🎮 Play Game")
        print("2. 💡Help")
        print("3. 🚪Exit")

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
