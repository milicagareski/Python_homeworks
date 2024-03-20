# 1. What is a variable in Python and how do we assign a value to it?

print("In Python, a variable serves as a container for holding data. Using the assignment operator '=' we can assign a specific data value, located on the right side of the operator, to the variable named on the left side.")

# 2. How do you create and declare a string in Python? Please mention all the different ways.

# using single quotes
person1 = 'John'

# using double quotes
person2 = "Peter"

# using triple quotes for multiline strings
person3 = """Susan is new here"""

# using string formatting
greeting = f'Hello {person1} and {person2}. {person3}. Welcome!'

# using string concatenation
welcome = "Welcome" + " " + person1

# using raw strings
wave = r"Hello everyone, I am new here"

# using the str.format() method
salute = "Hello {} and {}. Welcome to both of you.".format(person1, person2)

# printing the variables in the terminal
print(person1)
print(person2)
print(person3)
print(greeting)
print(welcome)
print(wave)
print(salute)

# 3. Write a code to declare a numeric variable and print its value along with its type.

# declare variables
number1 = 23
number2 = 32.4

# printing the values and type of the variables
print(number1, type(number1))
print(number2, type(number2))

# 4. Declare and assign two variables with your name, age and city details and print each of them with proper descriptions.

# declare variables for name, age and city
first_name = "Milica"
age = 31
city = "Malmo"

# information about the firstname
print(first_name)

# information about the age
print(age)

# information about the city
print(city)

# 5. What is the difference between ‘/’ and ‘//’ operators in python?

print("The operator '/' represent division in Python and it returns floating-point result. The operator '//' return the integer of the result, and even the result is a float number, this operator will return only the integer from the result, and will ignore the decimals that come after the integer. In short, '/' gives results with decimals and '//' gives only the integer part")

# 6. Calculate and print the quotient and remainder when 10 is divided by 3. Please use proper variable assignment to solve this.

# declare variables
num1 = 10
num2 = 3

# calculate the quotient
quotient = 10 // 3

# calculate the remainder
remainder = 10 % 3

# print the results
print(quotient)
print(remainder)

# 7. Write a python code to print the area of a rectangle, where length = 3.5 and breadth = 10. Hint: Area of a rectangle = length x breadth

# declare variables for storing the length and breadth of rectangle
length = 3.5
breadth = 10

# calculate the area of rectanle
area_of_rectangle = length * breadth

# printing the result
print(area_of_rectangle)

# 8. What is the difference between ‘=’ and ‘==’ in Python?

print("The '=' operator in Python is the assignment operator. It assigns a value to a variable. On the other hand, the '==' operator is the equality operator. It compares two values to check if they are equal in both value and type.")

# 9. Declare the below variables a = 5, b = 3, c = 10.
# i. Check whether the value of a + b \* c equals 80 or not and print its boolean result
# ii. Check whether the value of a / b + c equals 15 and print the boolean result

# declaring variables
a = 5
b = 3
c = 10

# cheking for results of the tasks
result1 = a + b * c 
result3 = a / b + c

# printing the results
print(result1 == 80)
print(result3 == 15)





