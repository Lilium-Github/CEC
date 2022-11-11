import random
import winsound

class Node:
    def __init__(self, carType, isFull, next=None, last=None):
        self.type = carType
        self.isFull = isFull

        self.ID = random.randint(100, 999)

        self.last = last
        self.next = next

        if self.type == "locomotive":
            self.hornMs = random.randint(100, 3000)
            self.hornHz = random.randint(50, 5000)

    def printSelf(self):
        print("\n------------\n" + self.type, "\nID:", self.ID, "\nFill Status:", self.isFull, "\n------------\n")
        
    def beep(self):
        if self.type == "locomotive":
            winsound.Beep(self.hornHz, self.hornMs)

class L_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, carType, isFull):
        self.length += 1
        newNode = Node(carType, isFull)
        if self.head: 
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.last = current
        else:
            self.head = newNode
        self.tail = newNode

    def print(self, order='f'):
        if order == 'f': #f for forwards
            current = self.head
            while current:
                current.printSelf()
                current = current.next
        elif order == 'b': #b for backwards
            current = self.tail
            while current:
                current.printSelf()
                current = current.last

    
    def search(self, name):
        current = self.head
        while current:
            if current.name == name:
                return True
            current = current.next 
        return False

    def index(self, index_num):
        if index_num > self.length:
            print("error: index out of range")
            return False
        else:
            current = self.head
            while current:
                if index_num == 0:
                    return current
                index_num -= 1
                current = current.next 

    def IDSearch(self, ID):
        current = self.head
        while current:
            if current.ID == ID:
                return current.type
            current = current.next 

    def pop(self):
        self.length -= 1

        self.head.next.last = None
        self.head = self.head.next

    def snip(self):
        self.length -= 1

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        self.tail = current

    def remove(self, index_num):
        if index_num > self.length:
            print("error: index out of range")
            return False
        else:
            current = self.head
            while current:
                if index_num == 0:
                    current.next = current.next.next
                    break
                index_num -= 1
                current = current.next

train = L_List()

print("Hello! Welcome to the Milady Express!")

while True:
    print("\n\nPlease select an action: \ntype 1 to add a car, \n2 to print out the entire train, \n3 to search for a car by its ID, \nor 4 to see how many of a certain type of car exist.\n\n")

    var = input()

    if var == "1":
        var = input("Car Full? (y/n):\n")
        if var == "y":
            full = True
        elif var == "n":
            full = False

        train.insert(input("Car Type:\n"), full)
    elif var == "2":
        train.print()
    elif var == "3":
        var = int(input("ID: \n"))
        print(train.IDSearch(var))
    elif var == "4":
        var = input("Car Type:\n")
        cars = 0

        currCar = train.head

        while currCar:
            if currCar.type == var:
                cars += 1
            currCar = currCar.next

        print(cars, "\n")
    elif var == "chugga chugga":
        print("Choo choo!")
        
        currCar = train.head

        while currCar:
            currCar.beep()
            currCar = currCar.next
