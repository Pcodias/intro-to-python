# Session 5 Exercises

## Section A
# 1. Print 10 random numbers.
import random 
for number in range (10):
  print (random.random())

# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .
import random
guess = None
while guess !=7:
while True:
    guess = int(input("Guess the computer's number:\n")) 
  print ("Wow! Lucky number 7!")
    import random
computer_choice = random.randint (1,10)
user_choice = None
while computer_choice != user_choice:
  user_choice = int(input("Guess the computer's number:n\"))
print("well done! You guess the computer's number")



# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.
import math
  
width = int(input("What is the width of your rectangle:\n"))
height = int(input("What is the height of your rectangle:\n"))

area_in_cm = width * height
area_in_m2 = math.ceil(area_in_cm/10000)
print("Your rectangle is " + str(area_in_m2) + ' metres squared.')



# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".
user_input = input("What is your password?\n")
password = "qwerty123"

user_guesses = 0

while user_guesses < 2:
    if user_input == password:
        print("You have successfully logged in.")
        break
    else:
        print("PASSWORD FAILURE\n")
        user_input = input("What is your password?\n")
        user_guesses += 1

if user_guesses == 2:
  print("PASSWORD FAILURE\n")
  print("System Failure - You have entered 3 incorrect passwords.")


# 5. Add up all the numbers from 1 to 500 and print the answer.
total = 0
number = 1

while True:
    total = total + number
    number = number + 1

    if number > 500:
        break

print(total)



# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.

num_list = []
numbers = ""
i = 0
x = 0 
print("Pick 10 numbers, one of those numbers must be 99")

while i < 10:
  numbers = int(input("Pick a number:\n"))
  num_list.append(numbers)
  i += 1 

while x < len(num_list):
  if num_list[x] == 99:
    print("Number 99 is at index " + str(x))
  x += 1

# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36
number = 18

i=0
while i < 15:
  print(i*18)
  i += 1



# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.
number = 1

while number <= 100:
    print(number)
    number += 1



# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
lesson = None

print("REPORT CARD:")

while lesson != "":
    lesson = input("Input your lesson:\n")
    mark = int(input("Input your mark:\n"))
    if mark > 80:
        print(lesson + " - A grade")
    elif mark <= 80 and mark > 60:
        print(lesson + " - B grade")
    elif mark <= 60 and mark > 50:
        print(lesson + " - C grade")
    elif mark <= 50 and mark> 45:
        print(lesson + " - D grade")
    elif mark <= 45 and mark > 25:
        print(lesson + " - E grade")
    elif mark < 25:
        print(lesson + " - F grade")
    else:
        print("Go to see your teacher")



# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name
import random

participants = []

# Ask for participants' names
num_participants = int(input("Enter the number of participants: "))
for _ in range(num_participants):
    name = input("Enter a participant's name: ")
    participants.append(name)

# Select a random winner
winner = random.choice(participants)

# Print the winner's name
print("The winner is:", winner)



# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games
import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors!")

# Best of 3 game loop
while player_score < 2 and computer_score < 2:
    print("------------------------------")
    print("Player Score: ", player_score)
    print("Computer Score: ", computer_score)
    print("------------------------------")

    # Player's choice
    print("\nChoose one: Rock, Paper, or Scissors")
    player_choice = input("Your choice: ").lower()

    # Computer's choice
    computer_choice = random.choice(choices)

    # Compare choices and determine the winner
    if player_choice == computer_choice:
  
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1
    else:
        print("Invalid choice. Please choose either Rock, Paper, or Scissors.")


