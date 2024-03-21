import sys
input = sys.stdin.readline

def fix_round(num):
  if num - int(num) >= 0.5:
    return int(num)+1
  else:
    return int(num)
    
level=[]
n = int(input())
cut = fix_round(n*0.15)

if n == 0:
    print(0)
    exit(0)

for i in range(n):
    level.append(int(input()))

level.sort()

hap=0
for i in range(cut, n-cut):
    hap += level[i]

print(fix_round( hap/(n-(2*cut))))