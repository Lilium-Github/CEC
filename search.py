import random
import math
import pyjokes


def linearSearch(targetlist, targetnum):
    print("Trying linear search...")
    found = False
    
    for i in range(len(targetlist)):
        if targetlist[i] == targetnum:
            print("Found your target number in", i+1, "steps, and I found it in slot", i)
            found = True
            break
    
    if not found:
        print("Sorry, couldn't find that.")
        
def binarySearch(targetList, targetNum, counter = 0):
    counter = counter + 1
    searchIndex = len(targetList) // 2
    
    if searchIndex < 1:
        print("Not found, sry!!!!!")
    elif targetList[searchIndex] == targetNum:
        print("Found target number", targetNum, "in", counter, "steps.")
    elif targetList[searchIndex] > targetNum:
        binarySearch(targetList[:searchIndex], targetNum, counter)
    elif targetList[searchIndex] < targetNum:
        binarySearch(targetList[searchIndex:], targetNum, counter)
    
print(pyjokes.get_joke(language = "en", category = "neutral"))
random.seed()



alist = []

for i in range(100):
    alist.append(random.randint(1,50))
    
alist.sort()

searchFor = random.randint(1,50)

linearSearch(alist, searchFor)

print("Trying binary search...")
binarySearch(alist, searchFor)
    

        

