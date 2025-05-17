# age = int(input("What is your age? "))
# bill = 0

# if age <= 12:
#     print("Pay $5")
#     bill = 5
# elif age <= 18:
#     print("Pay $12")
#     bill = 12
# elif age <= 60:
#     print("Pay $20")
#     bill = 20
# else:
#     print("Premium ticket")
#     bill = 25

# wants_photo = input("Do you want a photo? Y or N: ")

# if wants_photo.lower() == "y":
#     bill += 3

#     print("Your total bill is", bill)

# else:
#     print("Your total bill is", bill)



S_pizza= 15
M_pizza= 20
L_pizza= 25

size = input("What size pizza do you want? S, M, L: ").upper()
pepproni = input("Do you want pepperoni? Y or N: ").upper()
cheese = input("Do you want extra cheese? Y or N: ").upper()

if size =="S":
    bill= S_pizza
elif size=="M":
    bill=M_pizza
elif size=="L":
    bill=L_pizza
else:     
    print("Invalid size selected.")
    bill=0



if pepproni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if cheese == "Y":
    bill += 1

print(f"Your total bill is: ${bill}.")

