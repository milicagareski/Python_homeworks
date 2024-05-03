from functools import reduce

#Part 1: Review

#A Functions

#TASK NUMBER 1
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

num1 = 6
num2 = 7
print(is_even(num1), is_even(num2))


#TASK NUMBER 2
def factorial(num):
    if(num < 0):
        return "Please provide positive number"
    elif num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))


#TASK NUMBER 3
def fibonacci(n):
    fib_list = []
    for i in range(n):
        if i == 0 or i == 1:
            fib_list.append(i)
        else:
            fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[-1]

list_1 = fibonacci(8)
print(list_1)


# B While Loops


#TASK NUMBER 1
correct_ans = 7
is_true = False

while not is_true:
    user_input = input("What is the secret number? ")
    user_input = int(user_input)
    
    if user_input == correct_ans:
        is_true = True
        print("Gongratilations! The answer is correct.")
        break
    else:
        print("Wrong answer!Try again.")
    

#TASK NUMBER 2

is_prime = True
prime_numbers = []


i = 2
while len(prime_numbers) < 15:
    for j in prime_numbers:
        is_prime = True
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)
    i += 1

print(prime_numbers)


# For Loops

#TASK NUMBER 1

fruits = ['apple', 'banana', 'cherry']
new_fruits = []

for i in fruits:
   print( f"{i.upper()} has length of {len(i)}")

#TASK NUMBER 2 
for i in range(1,11):
    print(7 * i)



# If Statements
#TASK NUMBER 1

user_input = float(input("Write one number: "))

if user_input > 0:
    print("The number is positive")
elif user_input < 0:
    print("The number is negative")
else:
    print("The number is zero")

# TASK NUMBER 2
user_input = float(input("Write your grade: "))

if user_input < 0 or user_input > 100:
    print ("Please enter your grade from 0-100")
elif user_input >=0 and user_input < 60:
    print("letter grade: F")
elif user_input >=60 and user_input < 70:
    print("letter grade: D")
elif user_input >=70 and user_input < 80:
    print("letter grade: C")
elif user_input >=80 and user_input < 90:
    print("letter grade: B")
else:
    print("letter grade: A")



# Part 2: Object Oriented Programming (OOP)

# A Defining a Class
# B Instance Methods
# C Working with Instances
# D Additional Method in Class

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print (f"Woof! My name is {self.name}")

    def have_birthday(self):
        print (f"Happy nirthday {self.name}. You are {self.age + 1} years")
        

dog1 = Dog("Johny", 5)
dog2 = Dog("Lesi", 8)

dog_pack = [dog1, dog2]
average_age = 0

for i in dog_pack:
    i.bark()
    average_age += i.age
    print(average_age / len(dog_pack))


dog1.have_birthday()
dog2.have_birthday()


# Bonus Task

class Cat:
    def __init__(self,name,age, color):
        self.name = name
        self.age = age
        self.color = color

    def meow(self):
        print (f"Meow! I am {self.name}")

    def info(self):
        print (f"I am {self.name}. I have {self.age} years")

    def color_of_dog(self):
        print (f"The color of the cat is {self.color}")

cat1 = Cat("Sara", 5, "white")
cat2 = Cat("lea", 8, "black")

cats_pack = [cat1, cat2]

for i in cats_pack:
    i.meow()
    i.info()

cat2.color_of_dog()
cat1.color_of_dog()

# Part 3: map(), filter(), reduce()


# A map() Function


# TASK NUMBER 1

# Define a function that returns the square of a number
def square(n):
    return n*n

# Define a list of numbers
list_of_numbers = [1,2,3,4,5,6,7]

# Map through the elements in the list and return a new list with squared elements
new_list = list(map(square, list_of_numbers))
print(new_list)

# TASK NUMBER 2

# Define a function
def capitalize_word(word):
    return word.capitalize()

# Define a list of strings
fruits = ["apple", "banana", "mango"]

# Map through the elements in the list and return a new list with capitalized strings
list_of_fruits = list(map(capitalize_word, fruits))
print(list_of_fruits)

# B filter() Function
# TASK NUMBER 1

# Defining a function that check if the number is positive
def is_positive(num):
    if num > 0:
        return True

# List of numbers
numbers = [1,2,-3,-4,5,6,-7,-8]

# Filtering throught the list of numbers and returning a new list with only positive numbers
positive_numbers = list(filter(is_positive, numbers))
print(positive_numbers)

# TASK NUMBER 2

# Defining a function that check if a character exist 
def is_vowel(char):
    vowels = "aeiouAEIOU"
    if char in vowels:
        return True

word = "programming"
list_of_letters = []

# iterating throught the variable "word" and append every letter in list 
for i in word:
    list_of_letters.append(i)

# filtering the list and returning only the vowels. After that join the vowels in a string
list_of_vowels = "".join(list(filter(is_vowel, list_of_letters)))
print(list_of_vowels)


# C reduce() Function

# TASK NUMBER 1

# Defining a function that multiply two numbers
def multiply(a,b):
    return a * b

# List of numbers
array_of_numbers = [1,2,3,4,5,6]

# Reducing the list to only one number as a result of multiple the all numbers in the list
final_product = reduce(multiply, array_of_numbers)
print(final_product)

# TASK NUMBER 2

# Defining a function that concatinate two strings
def concatenate(str1, str2):
    return str1 + " " + str2

# Defining list of strings
list_of_words = ["Today", "is", "a", "good", "day"]

# Reducing the list to only one string
final_string = reduce(concatenate, list_of_words)

print(final_string)
