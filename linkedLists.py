class Student:
    def __init__(self, name, ID, cool, next=None):
        self.name = name
        self.ID = ID
        self.next = next
        self.cool = cool

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, name, ID, cool):
        self.length += 1
        newStudent = Student(name, ID, cool)
        if self.head: 
            current = self.head
            while current.next:
                current = current.next
            current.next = newStudent
        else:
            self.head = newStudent

    def printList(self):
        current = self.head
        while current:
            print("Student name:", current.name + ", ID:", current.ID, end=". ")
            if current.cool:
                print("They're very cool.")
            else:
                print("They're kinda lame.")
            current = current.next

    def search(self, name):
        current = self.head
        while current:
            if current.name == name:
                return True
            current = current.next 
        return False

    def index(self, index_num):
        if index_num >= self.length:
            print("error: index out of range")
            return False
        else:
            current = self.head
            while current:
                if index_num == 0:
                    return current
                index_num -= 1
                current = current.next 

    def pop(self):
        self.length -= 1

        self.head = self.head.next

    def snip(self):
        self.length -= 1

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def remove(self, index_num):
        if index_num >= self.length:
            print("error: index out of range")
            return False
        else:
            current = self.head
            while current:
                if index_num == 1:
                    current.next = current.next.next
                    break
                index_num -= 1
                current = current.next

sLine = LinkedList()

sLine.insert("Lily", 889681, False)
sLine.insert("Kyle", 666666, True)
sLine.insert("Mossy", 123456, True)
sLine.insert("Cory", 4, True)

print(sLine.printList(), "\n\n")
sLine.remove(1)
print(sLine.printList())
