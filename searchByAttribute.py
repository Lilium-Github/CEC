import random

random.seed()

speciesList = ["Trout", "Pike", "Sturgeon", "Cod", "Tuna", "Marlin"]

class fish:
    def __init__(self):
        coin = random.randint(0,5)
        self.species = speciesList[coin]
        if coin < 3:
            self.salinity = "Freshwater"
        else:
            self.salinity = "Saltwater"
        self.sex = random.randint(0,1) # the two genders, 0 and 1
        self.size = random.randint(6, 48) #anywhere from six inches to four feet

    def report(self):
        print("Species:", self.species)
        print("Salinity:", self.salinity)
        if self.sex == 0:
            print("Sex: Male")
        else:
            print("Sex: Female")
        print("Size:", self.size, "in.")
        print("\n\n")

fishes = []

for i in range(300):
    fishes.append(fish())

counter = 0
troutCount = 0

while counter < len(fishes):
    fishes[counter].report()

    if fishes[counter].species == "Trout":
        troutCount = troutCount + 1

    counter = counter + 1

print("\n\n\nCurrent Trout Population:", troutCount)

if troutCount < (len(fishes) / 6) - 1:
    print("The trout population is in danger!")
elif troutCount > (len(fishes) / 6) + 1:
    print("The trout population is exploding!")
else:
    print("The trout population is acting as normal.")
