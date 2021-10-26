import pygame
import random

room = "1"

def monster():
    num = random.randint(1,100)
    
    if num <= 30:
        return "vampire"
    elif num <= 50:
        return "mummy"
    else:
        return False
    
choice = "never gonna give you up"

while True:
    if room == "1":
        print("You're in room one. Placeholder text. \n")
        choice = input()
        if choice == "e":
            room = "2"
        elif choice == "n":
            room = "4"
        else:
            print("NOT SCIENTIFICALLY POSSIBLE \n\n")
    elif room == "2":
        print("You're in room two. Placeholder text. \n")
        var = monster()
        if var:
            print(var)
        choice = input()
        if choice == "w":
            room = "1"
        elif choice == "n":
            room = "3"
        else:
            print("NOT SCIENTIFICALLY POSSIBLE \n\n")
    elif room == "3":
        print("You're in room three. Placeholder text. \n")
        choice = input()
        if choice == "w":
            room = "4"
        elif choice == "s":
            room = "2"
        else:
            print("NOT SCIENTIFICALLY POSSIBLE \n\n")
    elif room == "4":
        print("You're in room four. Placeholder text. \n")
        choice = input()
        if choice == "e":
            room = "3"
        elif choice == "s":
            room = "1"
        elif choice == "w":
            room = "5"
        else:
            print("NOT SCIENTIFICALLY POSSIBLE \n\n")
    elif room == "5":
        print("You're in room five. Placeholder text. \n")
        var = monster()
        if var:
            print(var)
        choice = input()
        if choice == "e":
            room = "4"
        else:
            print("NOT SCIENTIFICALLY POSSIBLE \n\n")
            
        
