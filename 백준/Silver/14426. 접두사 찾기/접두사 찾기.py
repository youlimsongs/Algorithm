import sys
input = sys.stdin.readline

origin = []
check = []
cnt = 0

def is_prefix(s, origin):
    # 이분탐색을 사용하여 origin에서 s의 접두사인지 확인
    l, r = 0, len(origin) - 1

    while l <= r:
        mid = (l + r) // 2
        ori = origin[mid]

        if ori.startswith(s):
            global cnt  # 함수 내에서 전역 변수 cnt를 사용하기 위해 global 키워드 사용
            cnt += 1
            break

        elif ori < s:
            l = mid + 1
        else:
            r = mid - 1

    return cnt

n, m = map(int, input().split(" "))
for i in range(n):
    origin.append(input().strip())
origin.sort()

for j in range(m):
    check.append(input().strip()) 
check.sort()

res = 0

for c in check:
    res = is_prefix(c, origin)

print(res)