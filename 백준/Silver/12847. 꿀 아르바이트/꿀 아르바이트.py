n,m = map(int, input().split())
day = list(map(int, input().split()))

res, ans=0, 0
arr=[]
for i in range(n):
    if i < m :
        res += day[i]
    else:
        ans = max(res,ans)
        res -= day[i-m]
        res += day[i]
print(ans)