#TASK NUMBER 1:

# Variables for user inputs
first_name = input("Write your first name: ")
last_name = input("Write your last name: ")
are_equal = False

#comparing inputs
try:
  if(first_name == last_name):
    are_equal = True
    print(f'{are_equal}, Your first name is the same as your last name')
  else:
    print(f'{are_equal}, Your first name and your last name are not the same')
except Exception as e:
  print(e)



#TASK NUMBER 2:

# Variable for user input
weather = input("Describe the weather today: ")

#Spliting the input, so the empthy spaces won't count in the final result
try:
  list_of_words = weather.split(" ")
  result = 0
  for word in list_of_words:
    if len(word) > result:
      result = len(word)
  print(result)
except Exception as e:
  print(e)


#TASK NUMBER 3:

#Variables for the user input and the empty list
numbers = input("Write at least 2 numbers separated by comma: ")

# try and except block
try:
  list_of_numbers = numbers.split(",")
  new_list = []
  #iterating throught the user input and append every user number in the list
  for number in list_of_numbers:
    new_list.append(float(number))
  print(new_list)
  # defining variables that add every number from the new list
  count = 0
  for number in new_list:
    count += number
    print(count)
except Exception as e:
  print(e)

#TASK NUMBER 4:

#Variable for user input:
pass_input = input("Write your password: ")

#function that ckeck the password
try:
  def check_password (password):
  #removing emthy spaces
    check_pass = ''.join(password.split())
    contains_lower = False
    contains_upper = False
    contains_number = False

  #iterating throught the given password and checking if there is at least one lower key, upper key and digit key:
    for key in check_pass:
      if key.islower():
        contains_lower = True
      if key.isupper():
        contains_upper = True
      if key.isdigit():
        contains_number = True
  #Checking if the given password contains all requirement
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
except Exception as e:
  print(e)

check_password(pass_input)
