from functools import reduce

# 1. Map Function: Given a list of numbers, use the map function to square each number in the list.

numbers = [1, 2, 3, 4, 5]
def squared_numbers(num):
  return num*num

final_result = list(map(squared_numbers, numbers))
print(final_result)




# 2. Reduce Function: Use the reduce function to find the product of all numbers in a list.

numbers = [1, 2, 3, 4, 5]
def product_of_numbers(x,y):
  return x*y

final_product = reduce(product_of_numbers, numbers)
print(final_product)




# 3. Filter Function: Use the filter function to remove all the odd numbers from a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def remove_odd_numbers(x):
  return x % 2 == 0

final_list = list(filter(remove_odd_numbers, numbers))
print(final_list)




# 4. Lists: Given a list, swap the first and last elements of the list.

my_list = [1, 2, 3, 4, 5]

def swappedNumbers(arr):
  new_number = arr[0]
  arr[0] = arr[len(arr)-1]
  arr[len(arr)-1] = new_number
  print(arr)

swappedNumbers(my_list)




# 5. Tuples: Given a tuple, reverse the tuple.

my_tuple = (1, 2, 3, 4, 5)

def reversed_tuple(given_tuple):
  my_list = list(given_tuple)
  my_list.reverse()
  given_tuple = tuple(my_list)
  return given_tuple

  

my_reversed_tuple = reversed_tuple(my_tuple)
print(my_reversed_tuple)

# 6. Dictionaries: Given a dictionary, remove a specific key-value pair and add a new one.

my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict.pop("c")
my_dict["d"] = 5

print(my_dict)