n = int(input())
for i in range(n):
    num = int(input())
    cnt=0

    for j in range(2,1000001):
        if num % j == 0:
            cnt += 1
            print("NO")
            break
    
    if cnt == 0:
        print("YES")