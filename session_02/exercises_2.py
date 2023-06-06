# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
width=6
height=7
area = withd * height
print(Rectangle of witdth " +str(width)+ " and height " str(height) + " has an area of " + str(area)"


# 2. Write code that prints the length of the string, 'python'.
print(len("python))"


# 3. Print out the first and third letter of the word 'python'.
word = 'python'
print("python"[0])
print("python"[2])


# 4. Ask the user to enter their name, and print out `Hello, <name>`.
name = input("What is your name?")
print("Hello, " + name)



# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
age = int(input("What is your age? "))
age_in_15_years = age+ 15
print("In 15 years you will be": " + str(age_in_15_years))




# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.

print("Hello " + name + ", you are currently" + str(age) + "years old. In 15 years time you will be " + str(age_in15_years))


# 7. Ask the user to enter their hometown, print it out in uppercase letters.
hometown = input("What is your hometown? )
print(hometown_uppercase()) 



# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
color = input("What is your favorite color? ")
print(len(colour))


# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.
weather = input("What is the weather today?")
month = input("What month is it?")

print("It is " + month + " and it is " + weather + " today.")



# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
temp1 = int(What is the temperature?")
temp2 = int(What is the temperature?")
temp3 = int(What is the temperature?")
temp4 = int(What is the temperature?")
temp5 = int(What is the temperature?")

average+(temp1 + temp2 + temp3 + temp4 + temp5) / 5
print `It is + month + "and the average temperature is " + str(average))

# 11. Print out the above sentence but make the month upper case.
print `It is + month.upper() + "and the average temperature is " + str(average))


# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.
favorite_animals = "Elephant\n\tLion\n\t\tDolphin\n\t\t\tPenguin"
print(favorite_animals)


# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.
name = input("Enter your name: ")
number = int(input("Enter a number: "))

if number < len(name):
    uppercase_char = name[number].upper()
    print("Uppercase character at position", number, "is:", uppercase_char)
else:
    print("Invalid position. The name is not long enough.")



# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
strin="WelcometoPython"
print(len(string))
print(string[1:14:2])
