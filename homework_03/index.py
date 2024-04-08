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
