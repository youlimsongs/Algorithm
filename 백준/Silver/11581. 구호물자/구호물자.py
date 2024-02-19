import sys
input = sys.stdin.readline

n = int(input())
route = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n-1):
    cnt = int(input())
    row = (list(map(int, input().split())))
    for r in row:
        # print(i,r)
        route[i][r-1]=1


# print(route)
        
for k in range(n-1):
    for i in range(n-1):
        for j in range(n-1):
            # 시작점이 중간지점과 연결되어있고 중간지점과 도착지점이 연결되어 있다면
            if(route[i][k] and route[k][j]):
                route[i][j]=1 #출발, 도착지점을 연결표시

for i in range(n-1):
    if route[0][i] and route[i][i]:
        print("CYCLE")
        quit()
    
print("NO CYCLE")