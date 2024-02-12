import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
size = list(map(int, input().split(" ")))

#현재 인덱스와 눈 크기
def max_size(idx, snow, cnt):
    global res

    if idx == len(size)-1 or cnt == m:
        res = max(snow, res)
        return
    
    if idx+2 > len(size)-1:
        max_size(idx+1, snow+size[idx+1], cnt+1)
    else:
        max_size(idx+1, snow+size[idx+1], cnt+1)
        max_size(idx+2, snow//2+size[idx+2], cnt+1)

res = 1
max_size(-1, 1, 0)
print(res)