import sys
input = sys.stdin.readline

n,m = map(int, input().split(" "))
rate = list(map(int, input().split(" ")))
cost = list(map(int, input().split(" ")))

rate.sort(reverse=True)
cost.sort()

sum=0
for i in range(min(n, m)):
    if(rate[i]-cost[i] >0):
        sum += rate[i]-cost[i]

print(sum)