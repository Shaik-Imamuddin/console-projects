import random

attempts = 3
random_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("You have 3 attempts to guess the number between 1 and 10.")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == random_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        attempts -= 1
        print(f"Wrong guess. {attempts} attempts remaining.")
else:
    print(f"Sorry, you couldn't guess the number. \nThe correct number was {random_number}.")
