stage = [[1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 2, 2],
        [5, 5, 5, 10, 4, 4],
        [6, 6, 7, 6, 5, 5]]

def thisIsAFunction(stage):

    for i in range(len(stage) - 1, 0 ,-1):
        row = stage[i]
        nextRow = stage[i - 1]

        for j in range(len(row)):
            if nextRow[j] >= row[j]:
                return False

    return True

print(thisIsAFunction(stage))
