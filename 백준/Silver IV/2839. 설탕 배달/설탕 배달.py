n = int(input())
five = n//5
for i in range(five,-1,-1):
    # print(five)
    sugar = n - 5*five
    if(sugar%3==0):
        print(five + sugar//3)
        quit()
    else:
        five -=1
print(-1)