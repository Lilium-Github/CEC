import random
mapGrid = [[0 for i in range(10)] for j in range(10)]
x = random.randint(0,9) 
y = random.randint(0,9)

rooms = 0

while rooms < 10:

    direction  = random.randint(0,3)

    if direction == 0:
        direction = "up"

    elif direction == 1:
        direction = "down"

    elif direction == 2:
        direction = "right"

    else:
        direction = "left"

    if direction == "up":
        if y > 0 and mapGrid[x][y-1] == 0:
            mapGrid[x][y-1] = 2
            y-=1
            rooms +=1
        
    elif direction == "down":
        if y < 9 and mapGrid[x][y+1] == 0:
            mapGrid[x][y+1] = 3
            y+=1
            rooms +=1

    elif direction == "right":
        if x > 0 and mapGrid[x-1][y] == 0:
            mapGrid[x-1][y] = 4
            x-=1
            rooms +=1

    else:
        if x < 9 and mapGrid[x+1][y] == 0:
            mapGrid[x+1][y] = 5
            x+=1
            rooms +=1

mapGrid[x][y] = 1
for row in mapGrid:
    print(row)

