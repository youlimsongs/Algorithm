import sys
sys_input=sys.stdin.readline

length = int(sys_input())
n = int(sys_input())

cake = [0]*length
exp_num, real_num = 0, 0
prev, temp = 0, 0

for i in range(1,n+1):
    start, end = map(int, sys_input().split())

    # 가장 많은 조각을 받을 것으로 기대
    if(prev < end-start): 
        prev = end-start
        exp_num = i    

    
    # 실제로 가장 많은 조각
    cnt = 0
    for j in range(start-1, end):
        if(cake[j]==0): 
            cake[j]=i
            cnt += 1
    
    
    if(cnt > temp):
        # print(cnt)
        # print(temp)
        real_num =i
        temp = cnt
    
print(exp_num)
print(real_num)