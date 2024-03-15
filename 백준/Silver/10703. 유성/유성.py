R, S = map(int, input().split())
before = [input() for _ in range(R)]    # 유성 충돌 전
arr = [['.'] * S for _ in range(R)]    # 유성 충돌 후

move = R    

for x in range(S):
    star = 0  
    ground = 9999  
    flag = False    
    for y in range(R):
        if before[y][x] == 'X':
            star = max(star, y)
            flag = True  
        elif before[y][x] == '#':
            ground = min(ground, y)
    if flag: 
        move = min(abs(star-ground)-1, move)
 
for x in range(R):
    for y in range(S):
        if before[x][y] == 'X':
            arr[x+move][y] = 'X'  
        if before[x][y] == '#':
            arr[x][y] = '#'
 
for a in arr:
    print(''.join(a))