#TASK NUMBER 1:

# Variables for user inputs
str1 = input("Enter some string : ")
str2 = input("Enter some string : ")

#Comparing inputs
try:
  are_equal = False
  if str1 == str2:
    are_equal = True
    print(f'{are_equal}, the first string is equal to the second string')
  else:
    print(f'{are_equal}, the first string is NOT equal to the second string')
except Exception as e:
  print(e)



#TASK NUMBER 2:

# Variable for user input
weather = input("Describe the weather today: ")

# Spliting the input, so the empty spaces won't count in the final result
try:
  list_of_words = weather.split(" ")
  result = ""
  for word in list_of_words:
    if len(word) > len(result):
      result = word
  print(f"The longest word in this sentence is {result}. It has length of {len(result)} characters")
except Exception as e:
  print(e)



#TASK NUMBER 3:

#Variables for the user input and the empty list
numbers = input("Write at least 2 numbers separated by comma: ")

# Try-except block
try:
  list_of_numbers = numbers.split(",")
  count = 0
  # Iterating through the user input
  for number in list_of_numbers:    
    count += float(number)
  print(count)
except Exception as e:
  print(e)




# TASK NUMBER 4:

# Variable for user input:
pass_input = input("Write your password: ")

# Function that ckecks the password
def check_password (password):
# Removing empty spaces
  check_pass = ''.join(password.split())
  contains_lower = False
  contains_upper = False
  contains_number = False

# Iterating through the given password and checking if there is at least one lowercase letter, uppercase letter and digit:
  for key in check_pass:
    if key.islower():
      contains_lower = True
    if key.isupper():
      contains_upper = True
    if key.isdigit():
      contains_number = True
# Checking if the given password contains all requirements
  if not check_pass:
    print("Invalid password. Try again!")
  elif(len(check_pass) < 8 ):
    print("Your password must be at least 8 characters long")
  elif contains_lower == False:
    print("Your password must have at least one lowercase letter")
  elif contains_upper == False:
    print("Your password must have at least one uppercase letter")
  elif contains_number == False:
    print("Your password must have at least one number")
  else:
    print("Success login.Welcome back.")


try: 
  check_password(pass_input)
except Exception as e:
  print(e)
