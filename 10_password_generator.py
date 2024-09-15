import random
print("Welcome to password generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_length= int(input("How many letters would you like in your password?\n"))
symbol_lenght = int(input("How many symbols would you like in your password?\n"))
number_lenght = int(input("How many numbers would you like in your password?\n"))

password = ""
for char in range(password_length):
    password+=random.choice(letters)
for char in range(symbol_lenght): 
    password+=random.choice(symbols)
for char in range(number_lenght):
    randomnumber = random.choice(numbers)
    password+=randomnumber
# print(password)    
finalpass = ""
passwordlist= []
for pas in password:
    passwordlist.append(pas)
# print(passwordlist)    
for char in range(0, len(passwordlist)):
    a = passwordlist.pop(random.randint(0, len(passwordlist)-1))
    finalpass += a
print(f"Your password is: {finalpass}")