n,m = map(int, input().split())
colors = []
for _ in range(m):
    colors.append(int(input())) 

l = 1
r = max(colors)

while l <= r:
    mid = (l+r) // 2
    people = 0
    for color in colors:
        if color % mid == 0:
            people += color//mid
        else:
            people += (color//mid) + 1

    #받은 사람이 많으면 인당 받는 보석 수를 증가
    if people > n:
        l = mid + 1
    #조건 충족시 보석 수를 감소해서 최소 개수 찾음
    else:
        r = mid - 1

print(l)