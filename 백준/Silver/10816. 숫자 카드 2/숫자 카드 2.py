import sys
sys_input = sys.stdin.readline

n=int(sys_input())
num_list =list(map(int,sys_input().split()))

m=int(sys_input())
check_list =list(map(int,sys_input().split()))

result = {}

for num in num_list:
    if num in result:
        result[num] += 1
    else:
        result[num] = 1


#result[check]는 result 딕셔너리에서 check라는 키(key)에 해당하는 값을 출력

for check in check_list:
    if(check in result):
        print(str(result[check]), end=' ')
    else:
        print('0', end=' ')