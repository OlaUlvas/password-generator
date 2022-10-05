import random

print("Welcome to Password Generator!")

letters = ['a', 'b', 'c,' ,'d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'A', 'B', 'C', 'D', 'E']
numbers =['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['#', '%', '/', ')', '('] 

nr_symbols = int(input("How many symbols?"))
nr_numbers = int(input("How many numbers?"))
nr_letters = int(input("How many letters?"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
  

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)  
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char
print(f"Your password: {password}.")
