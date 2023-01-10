cases = input()

for _ in range(int(cases)):
    line = input()

    arr = line.split(' ')

    D = arr[0] #number of words in dictionary
    W = arr[1] #number of typos to correct

    dictionary = []
    typos = []

    for _ in range(int(D)):
        dictionary.append(input())

    for _ in range(int(W)):
        typos.append(input())

    
    for i, val in enumerate(typos):
        typo = val #specific typo to assess in this iteration

        toCheck = {} #dict object, holds all the words in the dictionary with the same length as typo as well as the Hamming distance between typo and the word

        hamDist = len(typo) + 1 #the highest possible Hamming distance between typo and word is the length of typo; by adding one to that we guarantee the program prints something

        for j, val2 in enumerate(dictionary):
            if len(typo) == len(val2):
                toCheck[val2] = 0

        for j in toCheck:               # for every item in toCheck
            for k in range(len(j)):     # iterate over that word
                if typo[k] != j[k]:     # for every letter that's different from typo
                    toCheck[j] += 1     # increase that word's Hamming distance

        for j in toCheck:
            if toCheck[j] < hamDist:
                hamDist = toCheck[j]
                correction = j

        print(correction)
        
