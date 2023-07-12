# Session 7 Exercises

## Section A
# 1. Write a function that prints your name
def print_name():
    print("Paula")


print_name()


# 2. Write a function that accepts a name as a parameter and prints "Hello, <name>".
def hello(name):
    print("Hello, " + name + "!")

List = ["Alice", "Bob", "Charlie"]
hello("Alice")
hello("Bob")
hello("Charlie")



# 3. Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote.
def hello(name):
    print("Hello, " + name + "!")

names_list = ["Alice", "Bob", "Charlie"]

for name in names_list:
    hello(name)



# 4. Write a function that prints the area of two passed in parameters.
def area(a, b):
    print("The area is " + str(a * c))


area(1, 3)


# 5. Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list.
def print_list(shapes):
    for shape in shapes:
        print(shape)

print_list(["circle", "rectangle", "square"])


print_list(["circle", "rectangle", "square"])



# 6. Put the following into a function that accepts age as a parameter:
#     1. If they are younger than 11, print "You're too young to go to this school".
#     2. If they are between 11 and 16, print "You can can come to this school".
#     3. If they are over 16, print 'You're too old for school".
#     4. If they are 0, print "You're not born yet!".
def school(age):
    if age < 11:
        print("You're too young to go to this school.")
    elif age >= 11 and age <= 16:
        print("You can come to this school.")
    elif age > 16:
        print("You're too old for school.")
    elif age == 0:
        print("You're not born yet.")
    else:
        print("You didn't pick a number.")


school(16)
school(0)
school(19)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers).
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

is_odd(6)
is_odd(5)



# 2. Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'.
def reverse_word(name):
#METHOD 1 
    new_string = ""
    name_length = len(name)
    while name_length != 0:
        name_length -= 1
        new_string += name[name_length]
    return new_string

#METHOD 2
    # reverse = name[::-1]
    # print(reverse)



reverse_word("hello")



# 3. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g:
# ```
# *****
# ****
# ***
# **
# *
# ```
def print_stars(x):
    star = ""
    for y in range(0, x):
        star = star + "*"
    print(star)
    if x > 1:
        print_stars(x-1)


print_stars(10)



# 4. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked".
def padlock(user_guess):

    pin = 8450
    if pin == user_guess:
        print("Unlock")
    else:
        print("Locked")


padlock(3423)
padlock(8450)



# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
#   For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
def multiples_3_and_5(limit):

    sum = 0
    
    for i in range (0, limit+1):
        if limit < 0:
            print("The limit must be greater than 0")
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
    
    print(sum)

multiples_3_and_5(20)
    


# 6. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not.
def is_prime(num):
  count = 0

  for i in range(2, num):
      if(num % i == 0):
          count = count + 1
          break

  if (count == 0 and num != 1):
      print(str(num) + " is a Prime Number")
      return True
  else:
      print(str(num) +" is not a Prime Number")
      return False

is_prime(6)
is_prime(99)
is_prime(83)


# 7. Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is not.
def pallindrome(word):
    reverse_word = word[::-1]
    if word == reverse_word:
        print(True)
    else:
        print(False)

pallindrome("strognsgag")
pallindrome("abba")



# 8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not. 
#   Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.
def pallindrome_sen(sentence):
    formatted_sen = sentence.lower()
    new_sentence = formatted_sen.replace(' ', '')
    rev_sentence = new_sentence[::-1]
    if new_sentence == rev_sentence:
        print(True)
    else:
        print(False)

pallindrome_sen("The cat sat on the mat")
pallindrome_sen("A nut for a jar of tuna")