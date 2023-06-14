import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Prompt the user for a guess
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        # Compare the guess with the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_the_number()