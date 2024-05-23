# TASK NUMBER 1
def create_file():
  file_name = input("What is your file's name? ")
  while file_name:
    user_name = input("What is your name? ")
    if user_name == " ":
      break
    else:
      file1 = open(f"{file_name}.txt", "a")
      file1.write(user_name + "\n")

# create_file()

# TASK NUMBER 2


# you have name,email,phone number,and address
# a. Write a python code which has a simple text file and read the data from the file.
# - First ask the user whether the user wanted to search or add a new entry .
# - After selecting the operation, the program will perform that operation.
# - Ask the user to enter an email address and extract all the name,phone number and
# address .
# - Also ask the user to enter the new entry.

def get_and_post_data():
  user_input = input("If you want to search for an entry answer with 'SEARCH'. If you want to add an entry answer with 'ADD'. ")
  
  if user_input == "SEARCH":
    found = False
    email = input("What is your email? ").strip()
    file1 = open("data.txt", "r")
    readed_file = file1.readlines()
    for i in readed_file:
      if f"email:{email}" in i:
        newList = i.split(" ")
        answer = f"The provided email has this informations: {newList[0]}, {newList[2]} and {newList[3]}"
        found = True
        print(answer)
        break 
    if not found:
      negative_answer = "Our database has no information about the email that you provided"
      print(negative_answer)

  elif user_input == "ADD":
    user_name = input("What is your name? ")
    user_email = input("What is your email? ")
    user_phone_number = input("What is your phone number? ")
    user_address = input("What is your address? ")

    new_entry = open("data.txt", "a")
    new_entry.write("\n" + f"name:{user_name} email:{user_email} phone_number={user_phone_number} address:street_{user_address}")
  
    answer = "Your information are saved in our database"
    print(answer)
  
  else:
    print("this keyword is unknown. Enter SEARCH if you want to search throught the database or ADD if you want to add new entry")

  




get_and_post_data()