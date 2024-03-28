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

# Write the cooking time
cooking_time = int(input("How much time did you cook the steak? "))

# Printing the state of the steak depends on the cooking time
state_state = "burns"

if cooking_time < 2:
  print("The steak is rare")
elif cooking_time <= 4:
  print("The steak is medium")
elif cooking_time > 4 and cooking_time <= 8:
  print("The steak is well done")
else:
  print("The steak burns")


# Program that determines the state of a steak based on the time it was grilled.

def state_od_stake(cook_time):
  state = "burns"
  if cook_time < 2:
    state = "rare"
  elif cook_time <= 4:
    state = "medium"
  elif cook_time <= 8:
    state = "well done"
  return state
  
wantedSteak1 = "medium"
wantedSteak2 = "well done"

steak1 = state_od_stake(3)
steak2 = state_od_stake(10)

def resultOfCooking(stateStake, wantedSteak):
  if stateStake == wantedSteak:
    print("The steak is perfect!")
  else:
    print("You ruined the steak, your friend is furious!")

resultOfCooking(wantedSteak1, steak1)

resultOfCooking(wantedSteak2, steak2)

