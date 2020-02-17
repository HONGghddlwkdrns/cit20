num = 1
divider = 10
C = "clap"


while(num < 150):
    if (num // divider == 3):
        print("cccclap")
        if (num % divider == 3):
            print(C)
        elif (num % divider == 6):
            print(C)
        elif (num % divider == 9):
            print(C)
    elif (num // divider == 6):
        print("cccclap")
        if (num % divider == 3):
            print(C)
        elif (num % divider == 6):
            print(C)
        elif (num % divider == 9):
            print(C)
    elif (num // divider == 9):
        print("cccclap")
        if (num % divider == 3):
            print(C)
        elif (num % divider == 6):
            print(C)
        elif (num % divider == 9):
            print(C)
    else:
        if (num % divider == 3):
            print(C)
        elif (num % divider == 6):
            print(C)
        elif (num % divider == 9):
            print(C)
        else :
            print(num)
    num = num + 1
