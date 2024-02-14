n = int(input())
hint = [list(map(int, input().split())) for _ in range(n)]
res=0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if (a==b or b==c or c==a):
                continue

            cnt = 0
            for arr in hint:
                num = arr[0]
                strike = arr[1]
                ball = arr[2]

                ball_count = 0
                strike_count = 0

                #비교로직
                if str(a) in str(num):
                    if str(a) == str(num)[0]:
                        strike_count+=1
                    else:
                        ball_count+= 1

                if str(b) in str(num):
                    if str(b) == str(num)[1]:
                        strike_count+=1
                    else:
                        ball_count+= 1
                
                if str(c) in str(num):
                    if str(c) == str(num)[2]:
                        strike_count+=1
                    else:
                        ball_count+= 1
                

                if(ball == ball_count and strike == strike_count):
                    cnt += 1

                

            #질문의 답과 모두 동일하다면
            if cnt == n:
                res += 1
                
print(res)