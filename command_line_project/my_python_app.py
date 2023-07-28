import random

def display_question_mark():
    question_mark = """ 
        -
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p
     "^^"              T####
                       d###P
                    _g###@F
                 _gN##@P
               gN###F"
              d###F
             0###F
             0###F
             0###F
             "NN@'
    
              ___
             q###r
              ""
    """
    print(question_mark)

def guess_number_game():
    display_question_mark()
    print("Hello and welcome to Number guessing game!")
    secret_number = random.randint(1, 100)

    guess = int(input("Guess a number between 1 and 100: "))
    while guess != secret_number:
        if guess < secret_number:
            print("Too low. Try again.")
            guess = int(input("Guess a number between 1 and 100: "))
        else:
            print("Too high. Try again.")
            guess = int(input("Guess a number between 1 and 100: "))
    try:
        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_number_game()


