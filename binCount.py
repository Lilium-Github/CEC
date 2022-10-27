def binComb(n):
    combList = []

    currBin = []

    isDone = False
    
    for _ in range(n):
        currBin.append('0')

    for _ in range(2 ** n):
        for i in (len(currBin) - 1, 0, -1):
            if currBin[i] == '1':
                currBin[i] = '0'
            else:
                currBin[i] = '1'
                break

        print(currBin)

        combList.append(currBin)

    return combList

print(binComb(3))
print("lily youre so cool")
