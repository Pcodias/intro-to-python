# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
if name == "Bob"
print("Hello Bob")


# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
if name != "Alice":
    print("You are not Alice")


# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".
password = input("Enter the password: ")

if password == "qwerty123":
    print("You have successfully logged in.")
else:
    print("Password failure.")


# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")



# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

total = number1 + number2

if total > 21:
    print("Bust")
else:
    print("Safe")



# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

if length == width:
    print("It is a square.")
else:
    print("It is not a square.")



# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
salary = float(input("Enter your current salary: "))
years_of_service = int(input("Enter your years of service: "))

if years_of_service > 3:
    bonus = salary * 0.1
    total_salary = salary + bonus
    print("Your salary: $", salary)
    print("Bonus: $", bonus)
    print("Total salary with bonus: $", total_salary)
else:
    print("Your salary: $", salary)
    print("No bonus")



# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
number = int(input("Enter a whole number: "))

if number > 0:
    result = number ** 3
    print("Number cubed:", result)
elif number < 0:
    result = number / 2
    print("Half of the number:", result)
else:
    print("The number is zero.")




# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".
name = input("What is your name? ")

if name == "Alice":
    print("Hello, Alice")
elif name == "Bob":
    print("You're not Bob! I'm Bob")
else:
    print("You must be Charlie")



# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age entered.")
elif age < 11:
    print("You're too young to go to this school.")
elif age <= 16:
    print("You can come to this school.")
elif age > 16:
    print("You're too old for school.")
elif age == 0:
    print("You're not born yet!")



# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".
month = input("Enter the name of a month: ")

if month.lower() in ["march", "april", "may"]:
    print(month + " is in Spring.")
elif month.lower() in ["june", "july", "august"]:
    print(month + " is in Summer.")
elif month.lower() in ["september", "october", "november"]:
    print(month + " is in Autumn.")
elif month.lower() in ["december", "january", "february"]:
    print(month + " is in Winter.")
else:
    print("I don't know.")



# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Even")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Odd")
else:
    print(num1 * num2)



# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("The first number,", num1, "is the highest.")
elif num2 > num1:
    print("The second number,", num2, "is the highest.")
else:
    print("Both numbers are equal.")



# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
current_salary = float(input("Enter your current salary: "))
years_of_service = int(input("Enter your years of service: "))

bonus = 0

if years_of_service > 7:
    bonus = 0.2
elif years_of_service > 5:
    bonus = 0.15
elif 3 <= years_of_service <= 5:
    bonus = 0.1

if bonus > 0:
    bonus_amount = current_salary * bonus
    new_salary = current_salary + bonus_amount
    print("Your salary: $", current_salary)
    print("Bonus: $", bonus_amount)
    print("New salary with bonus: $", new_salary)
else:
    print("No bonus")



# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.
# Get the details of the first person
name1 = input("Enter the name of the first person: ")
age1 = int(input("Enter the age of the first person: "))

# Get the details of the second person
name2 = input("Enter the name of the second person: ")
age2 = int(input("Enter the age of the second person: "))

# Get the details of the third person
name3 = input("Enter the name of the third person: ")
age3 = int(input("Enter the age of the third person: "))

# Determine the oldest person
oldest_age = max(age1, age2, age3)
oldest_names = []

# Determine the youngest person
youngest_age = min(age1, age2, age3)
youngest_names = []

# Find the names of the oldest and youngest people
if age1 == oldest_age:
    oldest_names.append(name1)
if age2 == oldest_age:
    oldest_names.append(name2)
if age3 == oldest_age:
    oldest_names.append(name3)

if age1 == youngest_age:
    youngest_names.append(name1)
if age2 == youngest_age:
    youngest_names.append(name2)
if age3 == youngest_age:
    youngest_names.append(name3)

# Print the results
print("Oldest person(s):")
for name in oldest_names:
    print(f"Name: {name}, Age: {oldest_age}")

print("Youngest person(s):")
for name in youngest_names:
    print(f"Name: {name}, Age: {youngest_age}")

# If all three ages are the same
if age1 == age2 == age3:
    print("All three people have the same age.")



# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
# Get the details for the first lesson
lesson1 = input("Enter the name of the first lesson: ")
marks1 = float(input("Enter the marks for the first lesson: "))

# Get the details for the second lesson
lesson2 = input("Enter the name of the second lesson: ")
marks2 = float(input("Enter the marks for the second lesson: "))

# Get the details for the third lesson
lesson3 = input("Enter the name of the third lesson: ")
marks3 = float(input("Enter the marks for the third lesson: "))

# Function to calculate the grade based on marks
def calculate_grade(marks):
    if marks > 80:
        return "A"
    elif 60 <= marks <= 80:
        return "B"
    elif 50 <= marks < 60:
        return "C"
    elif 45 <= marks < 50:
        return "D"
    elif 25 <= marks < 45:
        return "E"
    else:
        return "F"

# Calculate grades for each lesson
grade1 = calculate_grade(marks1)
grade2 = calculate_grade(marks2)
grade3 = calculate_grade(marks3)

# Print the results
print("Grades for each lesson:")
print(f"{lesson1}: {grade1}")
print(f"{lesson2}: {grade2}")
print(f"{lesson3}: {grade3}")
