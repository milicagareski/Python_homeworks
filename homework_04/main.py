# #TASK NUMBER 1 

# def true_or_false(status):
#   return not status

#TASK NUMBER 2


def answer():
  num = int(input( "Write some number : "))

  if num == 42:
    print("That's the answer!")
  else:
    print("The answer is NOT correct!")

answer()

#TASK NUMBER 3

# def ask_user():  
#   for i in range(10):
#     user_input = input(" What are you thinking: ")
#     if user_input:
#       if user_input == "leave me alone":
#         print("ok, bye :(")
#         break
#       print("Oh that's interesting but...", end="")

# ask_user()

# #TASK NUMBER 4

# # def for():
# #   print("better or worse")
   
# # for()

# # The code cannot be executed because 'for' is a reserved word in Python, and we cannot use it as the name of a function or variable. When I try to run the code, there is no result; instead, I get a syntax error, because od using keyword "for" for function name

# # TASK NUMBER 5

# print("ha")

# temp = print

# def print(some_val):
#     temp(f"{some_val}{some_val}{some_val}")
   
# print("ha")

# print = temp

# print("ha")


# # The interpreter in Python reads the code line by line, from top to bottom.
 
# # First, we call the built-in function print and give it the argument "ha". That's why we see "ha" printed in the terminal. 

# # Second, we define the variable temp and assign the print function as its value. 

# # Then, we have a second execution "hahaha" which is the result of the function named print. This function has one parameter, "some_val", and as a result, it prints this value three times. This happens because within the body of the function, temp is equal to the built-in print function, followed by parentheses containing the parameter "some_val". 

# # In the next line, we call this function named print, with the argument "ha", so the result we see in the terminal is "hahaha".

# # Next line, as I understand it, assigns the built-in function to be equal to temp, and on the other side, temp is equal to print. So, actually, nothing changes in this line of code. The function print remains print, and temp remains temp.

# # On the last line, we are again calling the built-in function print with the argument "hi". So actually, this is the same code as the first line, and the result will be the same.

