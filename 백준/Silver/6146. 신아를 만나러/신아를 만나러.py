#O(4V) V:1000*1000
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    #시작 좌표, 이동거리 설정
    queue.append((500, 500, 0))
    
    while queue:
        num = queue.popleft()
        #상하좌우로 모두 이동
        for i in range(4):
            a = num[0] + dx[i]
            b = num[1] + dy[i]
            if not visited[a][b]:
                visited[a][b] = True
                if a == x and b == y:
                    print(num[2] + 1)
                    return
                queue.append((a, b, num[2] + 1))

x, y, n = map(int, input().split())
#좌표 음수 처리
x += 500
y += 500

visited = [[False] * 1001 for _ in range(1001)]

#물 웅덩이 방문처리
for _ in range(n):
    a, b = map(int, input().split())
    visited[a + 500][b + 500] = True

bfs()