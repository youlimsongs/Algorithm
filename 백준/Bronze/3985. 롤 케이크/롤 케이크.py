import sys

length = int(input())
n = int(input())
cake = [0]*length

prev = 0
exp_num = 0
real_num = 0

for i in range(1,n+1):
    start, end = map(int, sys.stdin.readline().split())

    # 가장 많은 조각을 받을 것으로 기대
    if(prev < end-start): 
        prev = end-start
        exp_num = i    

    # 실제로 가장 많은 조각
    for j in range(start-1, end):
        if(cake[j]==0): cake[j]=i
    
# print(cake)

temp=0

for k in range(1, n+1):
    cur = cake.count(k)
    if(temp < cur):
        real_num = k
        temp = cur
    
print(exp_num)
print(real_num)