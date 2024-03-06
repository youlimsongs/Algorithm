k, n = map(int, input().split())
length=[]
for _ in range(k):
    length.append(int(input()))

l=1
r= max(length)
res=0

while l<=r:
    mid = (l+r)//2
    cnt=0
    for i in length:
        cnt += i//mid
    if cnt < n :
        r = mid - 1
    else:
        l = mid + 1
        res = max(mid, res)
    
print(res)