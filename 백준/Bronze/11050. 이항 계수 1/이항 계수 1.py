import sys
n,k = map(int, sys.stdin.readline().split())
top=n
bottom=k
if(k==0):
    print(1)
else:    
    for i in range(1,k):
        # print(i)
        top *= (n-i)
        bottom *= (k-i)
    print(top//bottom)