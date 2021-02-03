def crown1 (length,hieght):
    for i in range (0,hieght):
        for j in range (0,length):
            if i==0:

                if (j==0 or j==hieght or j==length-1):
                    print("*" , end="")
                else:
                    print(" ", end="")
            elif i==hieght-1:
                print("*" , end="")
            elif (j<i or j>hieght -i) and (j<hieght +i or j>=length -i):
                print("#" , end="")
            else:
                print(" " , end="")
        print()
length=int(input("enter any integer above 12"))
hieght= int((length-1)/2)
crown1(length,hieght)
