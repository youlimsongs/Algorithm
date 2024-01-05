import sys
from collections import Counter
sys_input = sys.stdin.readline
n = int(sys_input())
sum=0
arr=[]
for i in range(n):
    tmp = int(sys_input().strip())
    arr.append(tmp)
    sum += tmp

arr.sort()

print(round(sum/n))

print(arr[n//2])

count = Counter(arr).most_common()
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

print(arr[n-1]-arr[0])