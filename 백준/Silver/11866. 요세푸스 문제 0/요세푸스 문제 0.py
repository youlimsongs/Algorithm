import sys
n,k = map(int, sys.stdin.readline().split())
arr=list(range(1, n+1))
res = []
idx=0

for i in range(n):
    idx = (idx + k-1)% len(arr)
    res.append(str(arr.pop(idx)))

print('<'+', '.join(res)+'>')