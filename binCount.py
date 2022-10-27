def binComb(n):
    combList = []

    currBin = []

    isDone = False
    
    for _ in range(n):
        currBin.append('0')

    for _ in range(2 ** n):
        for i in range(len(currBin)):
            if currBin[i] == '1':
                currBin[i] = '0'
            else:
                currBin[i] = '1'
                break

            if currBin == '1':
                print("uh oh")

        strBin = ""
        
        for i in range(len(currBin)):
            strBin = strBin + currBin[i]

        strBin = strBin[::-1]

        combList.append(strBin)

    return combList

var = input("Enter size string: ")

while var != "0":
    print(binComb(int(var)))
    var = input("Enter size string: ")
