import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Solution 1

p_letters = []
for i in range(0, nr_letters):
    random_choice = random.choice(letters)
    p_letters.append(random_choice)


p_symbols = []
for i in range(0, nr_symbols):
    random_choice = random.choice(symbols)
    p_symbols.append(random_choice)


p_numbers = []
for i in range(0, nr_numbers):
    random_choice = random.choice(numbers)
    p_numbers.append(random_choice)

password_list = p_letters + p_symbols + p_numbers
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)




# Solution 2

password_1_list = []

for char in range(0, nr_letters):
    password_1_list += random.choice(letters)

for char in range(0, nr_symbols):
    password_1_list += random.choice(symbols)

for char in range(0, nr_numbers):
    password_1_list += random.choice(numbers)

random.shuffle(password_1_list)

password_1 = ""
for char in password_1_list:
    password_1 += char

print(password_1)
