import sys
from itertools import permutations
sys_input = sys.stdin.readline
n = int(sys_input().rstrip())
price = list(map(int, sys_input().split(" ")))
sale_list = [[] for _ in range(n)]
res = float('inf')


for i in range(n):
    sale_num = int(sys_input().rstrip())
    for j in range(sale_num):
        # sale_info = list(map(int, sys_input().split()))
        # sale_list[i].append(sale_info)
        sale_list[i].append(list(map(int, sys_input().split())))


#모든 경우의 수 순열 생성
case_list = permutations(range(0,n),n)

#모든 경우의 수 탐색
for i in case_list:
    tmp_price = price[:]
    tmp_res=0
    for j in i:
        tmp_res += tmp_price[j]
        for a, b in sale_list[j]: #a는 할인품목, b는 그 품목의 할인가격
            tmp_price[a-1] = max(1, tmp_price[a-1]-b)
        
    res = min(res, tmp_res)

print(res)