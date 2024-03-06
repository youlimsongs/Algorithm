import sys
input = sys.stdin.readline
t = int(input())

for t in range(t):
    k = int(input())
    n = int(input())
    apt = [[0]*n for _ in range(k+1)]

    for i in range(n):
        apt[0][i] = i+1

    for i in range(1,k+1):
        for j in range(n):
            tmp=0
            for l in range(j+1):
                tmp += apt[i-1][l]
            apt[i][j] = tmp
            
    print(apt[k][n-1])