# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
fruits = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
print(fruits)



# 2. Add "Grapes" to the list and print the list.
Add "Grapes" to the list and print the list.


# 3. Change "Pears" to "Strawberries" and print the list.
fruits = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
fruits[2] = "Strawberries"
print(fruits)




# 4. Remove "Apples" from the list and print the list.
fruits = ["Apples", "Cherries", "Strawberries", "Pineapple", "Peaches", "Mango"]
fruits.remove("Apples")
print(fruits)



# 5. Print out the current length of the list.
fruits = ["Cherries", "Strawberries", "Pineapple", "Peaches", "Mango"]
length = len(fruits)
print("Length of the list:", length)



# 6. Order the list alphabetically.
sorted
fruits = ["Cherries", "Strawberries", "Pineapple", "Peaches", "Mango"]
fruits.sort()
print(fruits)


# 7. Print out the list again.
Order the list alphabetically.
sorted
fruits = ["Cherries", "Strawberries", "Pineapple", "Peaches", "Mango"]
fruits.sort()
print(fruits)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
names = ["Alice", "Bob", "Charlie"]

for person in names:
    print(person)

# Alice
# Bob
# Charlie


# 2. Print the numbers 1 to 100 (including the number 100).
for number in range(1, 101):
    print(number)



# 3. Print all odd numbers from 1 to 100.
for number in range(1, 101):
    if number % 2 != 0:
        print(number)



# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
excluded_years = [1916, 1940, 1944, 2020]

for year in range(1896, 2023, 4):
    if year not in excluded_years:
        print(year)



# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
import random

# Create an empty list to store the random numbers
numbers = []

# Generate ten random numbers and append them to the list
for _ in range(10):
    numbers.append(random.randint(1, 100))

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Loop through the list and count the number of even and odd numbers
for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print the counts
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)



# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

for name in names:
    print("Hello", name)



# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
word = "supercalifragilisticexpialidocious"

for letter in word:
    print(letter)



# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
numbers = [2, 5, 7, 10, 3]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num ** 2)

print(squared_numbers)



# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
new_list = []

for name in names:
    new_list.append("Dr. " + name)

print(new_list)



# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
