import sys
input = sys.stdin.readline
cnt=0
res=0

n , k = list(map(int,input().split(" ")))
numlist = []
for i in range(n):
    numlist.append(int(input()))

pointer = 0 #가리키는 사람

for i in range(n):
    target = numlist[pointer]
    cnt+=1
    if target == k :
        print(cnt)
        break
    pointer = target
else:
    print(-1)