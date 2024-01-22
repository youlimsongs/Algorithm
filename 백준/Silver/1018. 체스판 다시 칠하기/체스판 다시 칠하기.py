import sys
# from collections import deque
input = sys.stdin.readline

n ,m=map(int, input().split(" "))
total = []
count=[]
for i in range(n):
    total.append(input().strip())

for i in range(n-7):
    for j in range(m-7):
        res1, res2 = 0, 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if(a+b) % 2 ==0: #흰색으로 시작
                    if total[a][b] != 'W': #흰색이 아니면
                        res1 += 1
                    if total[a][b] != 'B':
                        res2 += 1
                else:
                    if total[a][b] != 'B':
                        res1 += 1
                    if total[a][b] != 'W':
                        res2 += 1
        count.append(min(res1, res2))

print(min(count))