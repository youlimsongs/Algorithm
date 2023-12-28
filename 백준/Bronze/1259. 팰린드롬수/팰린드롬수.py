while(1):
    num = (input())
    if(num=="0"):
        break
    elif(int(num) < 10):
        print("yes")

    num = list(num)
    check = len(num)//2

    for i in range(check):
        last = len(num)-1
        if(num[i] != num[last-i]):
            # print(str(i)+" and "+str(last-i))
            print("no")
            break
        elif(i==check-1):
            print("yes")