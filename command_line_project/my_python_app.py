import random

def number_guessing_game():
    secret_number = random.randint(1, 100)

    start = 1
    end = 100
    random_number = random.randint(start, end)
    print(random_number)

    start = 1
    end = 100

    guess = int(input("Guess a number between 1 and 100: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

    categories = ("even", "odd")
    for category in categories:
        print(category)

number_guessing_game()
