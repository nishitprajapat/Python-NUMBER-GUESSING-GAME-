import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)

guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running: 
    guess = input("Enter your Guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess > 100 or guess < 1:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! try again")
        elif guess > answer:
            print("Too High! try again")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses} ")
            is_running = False

    else:
        print("Invalid Guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")