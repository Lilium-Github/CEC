import random

#ant farm base code!
#written by Dr. Mo, Jan 22

colony=[] #list to hold all the ants

random.seed()

#parent class---------------------------------------
class ant:
    def __init__(self, age, food):
        self.age = age
        self.food = food
    def eat(self):
        self.food+=1

    def update(self):
        self.food-=1
        self.age+=1
        

#child class--------------------------
class worker(ant):
    def __init__(self, age, food):
        self.name = "worker"
        ant.__init__(self, age, food)
    
    def printInfo(self):
        print("I am a worker and I am ", self.age, " days old. My food level is ", self.food)
        
    def search(self, colony):
        count = random.randint(1,10)
        if count == 1:
            print("I found some food for the colony!")
            for ant in colony:
                ant.eat()
#child class--------------------------
class larva(ant):
    def __init__(self, age, food):
        self.name = "larva"
        ant.__init__(self, age, food)
    def printInfo(self):
        print("I am a larva and I am ", self.age, " days old. My food level is ", self.food)
    def metamorphosis(self):
        var = random.randint(1,20)
        if var == 1:
            NewQueen = queen(self.age - 1, self.food)
            colony.append(NewQueen)
            print("This larva has become a queen! Wow!")
        else:
            NewWorker = worker(self.age - 1, self.food)
            colony.append(NewWorker)
            print("This larva has become a worker.")
            
            
#child class--------------------------
class queen(ant):
    def __init__(self, age, food):
        self.name = "queen"
        ant.__init__(self, age, food)
        
    def printInfo(self):
        print("I am a queen and I am ", self.age, " days old. My food level is ", self.food)
        
    def egg(self):
        print("queen has laid an egg!")
        
        BabyLarva = larva(0,10)
        colony.append(BabyLarva)
        
#start of "main"########################################
q1 = queen(0,5)
colony.append(q1)
w1 = worker(0,5)
colony.append(w1)
w2 = worker(0,5)
colony.append(w2)
l1 = larva(0,5)
colony.append(l1)

#game loop

doExit = False
while doExit == False:


#print info for each ant in colony
    i = 0
    while i != len(colony):
        colony[i].printInfo()
        colony[i].update()
        if colony[i].name == "queen":
            colony[i].egg()
        if colony[i].name == "larva" and colony[i].age > 1:
            colony[i].metamorphosis()
            del colony[i]
        if colony[i].name == "worker":
            colony[i].search(colony)
        if colony[i].age > random.randint(5,10):
            print("This ", colony[i].name, " has died of old age.")
            del colony[i]
            i-=1
            if len(colony) == 0:
                break
        if colony[i].food < 1:
            print("This ", colony[i].name, " has died of starvation.")
            del colony[i]
            i-=1

        i += 1    
    
    
    
    print("------------")

    userInput = input("press any key to continue, q to quit")
    if userInput == "q" or len(colony) == 0:
        doExit = True
