# num = 1
#
# while (num<5000):
#     if (num % 7 == 0):
#         print(num)
#
#     num = num + 1

num = 1

while (num < 30):
    if (num % 2 != 0):
        print("weird")
    # else:
    #     if(2<=num and num<=5):
    #         print("not weird")
    #     elif(6<=num and num<=20):
    #         print("weird")
    #     else:
    #         print("not weird")
    elif(2<=num and num<=5):
        print("not weird")
    elif(6<=num and num<=20):
        print("weird")
    else:
        print("not weird")
    num = num + 1
