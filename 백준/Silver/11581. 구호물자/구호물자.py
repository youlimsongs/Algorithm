n = int(input())
route = [[0 for _ in range(n)] for _ in range(n)]

#입력 처리
for i in range(n-1):
    cnt = int(input())
    row = (list(map(int, input().split())))
    for r in row:
        route[i][r-1]=1

#방문처리 0:미방문, 1:방문, 2:탐색 완료
visited = [0 for _ in range(n)]
is_cycle=False

def dfs(v):
    global is_cycle

    # 방문 처리
    visited[v]=1
    
    # 자식 탐색
    for i in range(n):
        if(route[v][i]):
            if visited[i]==0:
                dfs(i)
            elif visited[i]==1:
                is_cycle=True
                return
    
    #모든 자식 탐색 완료
    visited[v]=2
        
dfs(0)

print("CYCLE" if is_cycle else "NO CYCLE")