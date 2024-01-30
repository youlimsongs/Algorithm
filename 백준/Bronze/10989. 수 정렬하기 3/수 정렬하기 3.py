import sys
input = sys.stdin.readline
res=[0]*10001
n = int(input().strip())
for i in range(n):
    res[(int(input().strip()))] += 1

for i in range(10001):
    if(res[i] != 0):
        for j in range(res[i]):
            print(i)