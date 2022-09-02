from curses import color_pair


class car:
    def __init__(self, make, color, miles):
        self.make = make
        self.color = color
        self.miles = miles

    def printSelf(self):
        print("I am a", color, make, "and I have driven", miles, "miles.")

    def honking(self):
        print("beep")

car1 = car("Honda Civic", "White", 1000000)
car2 = car("Toyota Rav4", "Blue", 1)
car3 = car("Tesla", "Black", -1000)

cars = [car1, car2, car3]

for i in range(len(cars)):
    cars[i].printSelf()
    cars[i].honking

userScore = int(input("What's your score? \n"))

if userScore < 100:
    print("you smell. git gud")
elif userScore > 800:
    print("you've spent too much time playing this game.")
else:
    print("you're pretty good, i guess")

inText = input("input a letter, q to quit \n")

while inText != "q":
    print("bonk")
    inText = input("input a letter, q to quit \n")

for i in range(8,24,4):
    print(i)

for i in range(80,71, -1):
    print(i)

