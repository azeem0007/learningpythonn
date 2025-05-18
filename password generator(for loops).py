

# import numpy as np
# scores = np.random.randint(0,101,size=10)
# print(scores)

# import random


# studnets_score = [random.randint(0,100) for _ in range (10)]
# print(studnets_score)


# max_score =0 

# for score in studnets_score:
#     if score > max_score:
#         max_score = score   

# print(max_score)

# total = 0
# for number in range(1,101):
#     total = total + number

# print(total)

import string
import random
letters_lower = list(string.ascii_lowercase)
digits=list(string.digits)
symbols = list(string.punctuation)

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symboles= int(input("How many symbols would you like?\n"))
nr_digits = int(input("How many numbers would you like?\n"))

print("easy password generator\n")
password_len = nr_letters + nr_symboles + nr_digits

password =[]
for i in range(0, nr_letters):
    password.append(random.choice(letters_lower))

for i in range(0, nr_symboles):
    password.append(random.choice(symbols))

for i in range(0, nr_digits):
    password.append(random.choice(digits))
print("your password is: ", password)


random.shuffle(password)
print("your password is: ", password)


final_pass = ""

for i in password:
    final_pass += i 
    print("your password is: ", final_pass)

    





