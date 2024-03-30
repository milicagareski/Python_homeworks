# TASK NUMBER 1:

# Write the numbers
num1 = int(input("Write your first number: "))
num2 = int(input("Write your second number: "))

# Flags for even or odd numbers
are_even = False
are_odd = False
is_multiple_of_five = False

  # Checking if both numbers are even 
if num1 % 2 == 0 and num2 % 2 == 0:
  are_even = True
  print(f'{are_even}, Both numbers are even.')
else:
  print(f'{are_even}, Both numbers are NOT even.')
  

  # Checking if both numbers are odd 
if num1 % 2 != 0 and num2 % 2 != 0:
  are_odd = True
  print(f'{are_odd}, Both numbers are odd.')
else:
  print(f'{are_odd}, Both numbers are NOT odd.')


# Checking is it at least one of the numbers multiple of 5
if num1 % 5 == 0 or num2 % 5 == 0:
  is_multiple_of_five = True
  print(f'{is_multiple_of_five}. One of the numbers is multiple of 5 or both numbers are multiple of 5.')
else:
  print(f'{is_multiple_of_five}. None of the numbers is a multiple of 5.')

# TASK NUMBER 2:
  
# Write the temperature
temp = int(input("How many degrees is the temperature today: ?"))

#Check the state of the temperature
if temp < 4:
  print("You must wear a pair of gloves.")
elif temp < 8:
  print("You must wear scarf.")
elif temp < 12:
  print("You must wear a jacket.")
elif temp > 25:
  print("You must wear sunglasses.")
else:
  print("The weather is fine today.")

# TASK NUMBER 3:

# Program that determines the state of a steak based on the time it was grilled.

def check_steak_state(grill_time, desired_state): 
  if grill_time < 2: 
    state = "rare"      
  elif grill_time <= 4: 
    state = "medium" 
  elif grill_time < 8: 
    state = "well done" 
  else:
    state = "burnt" 

  if state == desired_state: 
    print("The steak is perfect!") 
  else: 
    print("You ruined the steak, your friend is furious!") 
  
 
# Test cases 
steak1_time = 3 
steak1_desired_state = "medium" 
check_steak_state(steak1_time, steak1_desired_state)
 
steak2_time = 10 
steak2_desired_state = "well done" 
check_steak_state(steak2_time, steak2_desired_state)

