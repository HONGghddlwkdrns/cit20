
# divider = 10
# C = "clap"
num = 1
arr369 = [3,6,9]
limit = 100


while(num < limit):
    divider = 1
    count369 = 0
    while (num % divider != num):
        for i in arr369:
            if ((num % (divider*10) - num % divider )/ divider == i):
                count369 = count369 + 1
        divider = divider * 10

    if ( count369 == 0 ):
        print(num)
    else :
        while (count369 > 0):
            print("clap!" , end='')
            count369 = count369 -1
        print(" ")
    num = num + 1






    # if (num // divider == 3):
    #     print("cccclap")
    #     if (num % divider == 3):
    #         print(C)
    #     elif (num % divider == 6):
    #         print(C)
    #     elif (num % divider == 9):
    #         print(C)
    # elif (num // divider == 6):
    #     print("cccclap")
    #     if (num % divider == 3):
    #         print(C)
    #     elif (num % divider == 6):
    #         print(C)
    #     elif (num % divider == 9):
    #         print(C)
    # elif (num // divider == 9):
    #     print("cccclap")
    #     if (num % divider == 3):
    #         print(C)
    #     elif (num % divider == 6):
    #         print(C)
    #     elif (num % divider == 9):
    #         print(C)
    # else:
    #     if (num % divider == 3):
    #         print(C)
    #     elif (num % divider == 6):
    #         print(C)
    #     elif (num % divider == 9):
    #         print(C)
    #     else :
    #         print(num)

    # ======

        # clap = False
        # for x in arr369:
        #     if (num // divider == x) :
        #         print("cccclap")
        #         for y in arr369:
        #             if (num % divider == y):
        #                 print(C)
        #                 clap = clap or True
        #         clap = clap or True
        #     for y in arr369:
        #         if (num % divider == y):
        #             print(C)
        #             clap = clap or True
        # if (not (clap) ):
        #     print(num)
