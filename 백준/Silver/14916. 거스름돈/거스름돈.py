change = int(input())
five=0
two=0

if (change%5 != 0 ):

    five += change//5
    change %= 5
    if( change%2 ==0):
        two += change//2
        print(two+five)
    else:
        five -= 1
        if(five<0):
            print(-1)
        else:    
            change += 5
            two += change//2
            print(two+five)
else:
    five += change //5
    print(five)