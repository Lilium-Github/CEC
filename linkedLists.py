class Node:
    def __init__(self, data, next=None, last=None):
        self.data = data
        self.last = last
        self.next = next

class L_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, data):
        self.length += 1
        newNode = Node(data)
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
                print(current.data, end = " ")
                current = current.next
        elif order == 'b': #b for backwards
            current = self.tail
            while current:
                print(current.data, end = " ")
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

def swap_adj(link):
