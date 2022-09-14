def NumberCrunch(num):
    num = str(num)

    if len(num) > 4:
        print("too big, sorry!")
    if len(num) == 4:
        print(num[0], "thousand")
        num = num[1:]
    if len(num) == 3:
        print(num[0], "hundred")
        num = num[1:]
    if len(num) == 2:
        if num[0] == "9":
            print("ninety ")
        elif num[0] == "8":
            print("eighty ")
        elif num[0] == "7":
            print("seventy ")
        elif num[0] == "6":
            print("sixty ")
        elif num[0] == "5":
            print("fifty ")
        elif num[0] == "4":
            print("forty ")
        elif num[0] == "3":
            print("thirty ")
        elif num[0] == "2":
            print("twenty ")
        elif num[0] == "1":
            if num[1] == "0":
                print("ten")
            elif num[1] == "9":
                print("nineteen")
            elif num[1] == "8":
                print("eighteen")
            elif num[1] == "7":
                print("seventeen")
            elif num[1] == "6":
                print("sixteen")
            elif num[1] == "5":
                print("fifteen")
            elif num[1] == "4":
                print("fourteen")
            elif num[1] == "3":
                print("thirteen")
            elif num[1] == "2":
                print("twelve")
            elif num[1] == "1":
                print("eleven")
            num = "foo"
        num = num[1:]
    if len(num) == 1:
        if num == "9":
            print("nine")
        elif num == "8":
            print("eight")
        elif num == "7":
            print("seven")
        elif num == "6":
            print("six")
        elif num == "5":
            print("five")
        elif num == "4":
            print("four")
        elif num == "3":
            print("three")
        elif num == "2":
            print("two")
        elif num == "1":
            print("one")
        

NumberCrunch(input("Input Number: "))