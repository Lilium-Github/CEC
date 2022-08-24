# 1:

num = input("Input Number: ")

if int(num) % 3 == 0:
    print("boogers")
else:
    print("squirrels")

# 2:

for i in range(5):
    print((i * 5) + 10)

# 3:

def midpoint(x1, y1, x2, y2):
    point = [] 

    point.append((x1 + x2) / 2)
    point.append((y1 + y2) / 2)

    return point

print(midpoint(2, 2, 6, 6))

# 4:

friendList = ["mossy", "mo", "cory", "zero", "mario"]

foundMo = False

for i in range(len(friendList)):
    if friendList[i] == "mo":
        foundMo = True
    
if foundMo:
    print("nerd alert")
else:
    print("cool kids only")