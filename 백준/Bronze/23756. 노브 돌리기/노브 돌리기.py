import sys
input = sys.stdin.readline

n = int(input().strip())
loc=[]
sum=0

for i in range(n+1):
    loc.append(int(input().strip()))

for i in range(n):
    if(abs(loc[i]-loc[i+1])>180):
        res = 360-abs(loc[i+1]-loc[i])
    else:
        res = abs(loc[i+1]-loc[i])
    
    sum += res

print(sum)