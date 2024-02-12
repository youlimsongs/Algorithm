n = int(input())
d = 0

while(n>0):
    #현재 위치(m)
    d=0

    #지점 0 에서 최대 4번 다시 출발
    for i in 1,2,3,4:
        #지점 0에서 콘 i번째까지 가는 경우
        # 출발 구간
        for j in range(i):
            
            n -= 5
            # 한 칸을 못간다면
            if n < 0:
                d += 5+n
                break
            d += 5
        
        if n <= 0:
            break

        # 복귀 구간
        for j in range(i):
            
            n -= 5
            # 한 칸을 못간다면
            if(n < 0):
                d -= 5+n
                break

            d -= 5
        
        if n <= 0:
            break

print(d//5 if d%5 == 0 else d//5+1)