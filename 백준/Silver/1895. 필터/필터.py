import sys
sys_input = sys.stdin.readline

c_filter = []
r, c = map(int, sys_input().split())
for i in range(r):
    row = list(map(int, sys_input().split()))
    c_filter.append(row)

t = int(sys_input().strip())

filter=[]

len, height = r-2, c-2
for i in range(len):
    for j in range(height):
        tmp=[]
        for a in range(3):
            for b in range(3):
                tmp.append(c_filter[i+a][j+b])
        tmp.sort()
        filter.append(tmp[4])

cnt=0
for i in filter:
    if i>= t:
        cnt +=1

print(cnt)