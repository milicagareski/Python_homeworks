# TASK NUMBER 1

def outher_func(num1):
  def inner_func(num2):
    return num1 ** num2
  return inner_func
  

x = outher_func(4)
print(x(2))

# TASK NUMBER 2

def greet(func):
  def inner_func(*args):
    print("Hello")
    greet_person = func(*args)
    print("Goodbye")
    return greet_person
  return inner_func


@greet
def say_name(name):
  print(name)

say_name("Jane")
say_name("John")

# TASK NUMBER 3

def fibbonacci_sequence(limit):
  a = 0
  b = 1
  for i in range(limit):
    yield b
    a,b = b, a + b

for j in fibbonacci_sequence(10):
  print(j)
    
