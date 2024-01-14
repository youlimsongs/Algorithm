import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    temp = (list(map(int, input().split(" "))))
    arr.append(temp)

rank=[1]*n
for i in range(n):
    for j in range(n):
        if(arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]):
            rank[i]+=1

for i in rank:
    print(i, end=' ')