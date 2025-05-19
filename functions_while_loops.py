import random
from tkinter import Place
words =["arizonea","california","new york","florida","texas"]
chosen_word= random.choice(words)
lives =len(chosen_word)
print(chosen_word)


print("Welcome to the game of hangman!")
placeholder =""
display=""

for i in range(0,lives):
        placeholder += "_"
print(placeholder)
     
game_over=False
coorect_list=[]
while game_over != True:
    guess = input("Guess a letter: ").lower()    
    for i in chosen_word:
        if i == guess:
            display = display + guess
            coorect_list.append(guess)
            print(coorect_list)
        else:
            display = display + "_"
            lives-= 1


    if "_" not in display:
        print("You win!")
        game_over = True
                   
        