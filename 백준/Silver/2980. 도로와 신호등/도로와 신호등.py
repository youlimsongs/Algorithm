import sys
input = sys.stdin.readline

n,l = map(int, input().split(" "))
# print(n, l)
sec=0
loc = 0
for i in range(n):
    d,r,g = map(int, input().split(" "))
    sec += d-loc
    # print("1",sec)
    loc=d
    if sec % (r+g) >= 0 and sec % (r+g) < r:
        sec += ((r) - (sec % (r+g))) #기다림
    else:
        continue

    # print("2",sec)

# print("3",sec)
sec += l-loc
print(sec)