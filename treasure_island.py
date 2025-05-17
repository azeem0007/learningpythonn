print("welcome to treasure island.\n")
print("your mission is to find the treasure.\n")

direction = input("you are at a crossroad. where do you want to go? type 'left' or 'right'.\n").lower()

if direction=="left":
    u1=input("do you want to swim or wait?\n").lower()
    if u1=="wait":
        u2=input("which door you want to open? red or blue or yellow?. \n").lower()
        if u2=="yellow":
            print("you win!!")
        elif u2=="red" or u2=="blue":
            print("you got eaten by a beast. game over.")
    elif u1=="swim":
        print("you got attacked by an angry trout. game over.")
        
else:
    print("you fell into a hole. game over.")
