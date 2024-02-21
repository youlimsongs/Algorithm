import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input()
    a,b,c,d = map(int, input().split())

    for i in range(d):
        if max(a,b,c) == a :
            a -= 1
        elif max(a,b,c) == b :
            b -= 1
        else:
            c -= 1
    
    # print(a,b,c)
    print(a*b*c)